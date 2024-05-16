from .BaseController import BaseController
from .ProjectControllers import ProjectController
from fastapi import UploadFile
from models import ResponceSiginal
import os
import re

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes

    def validate_uploaded_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponceSiginal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponceSiginal.FILE_SIZE_EXCEEDED.value

        return True, ResponceSiginal.FILE_VALIDATED_SUCCESS.value
    
    def generate_unique_filepath(self, project_id: str, orig_filename: str):

        random_key = BaseController().generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_filename = self.get_clean_filename(orig_filename = orig_filename)

        new_file_path = os.path.join(project_path, random_key+'_'+cleaned_filename)

        while os.path.exists(new_file_path):
            random_key = BaseController.generate_random_string()
            new_file_path = os.path.join(project_path, random_key+'_'+cleaned_filename)

        return new_file_path, random_key+'_'+cleaned_filename
    def get_clean_filename(self, orig_filename: str):

        cleaned_filename = re.sub(r'\w.', '', orig_filename.strip())

        cleaned_filename = cleaned_filename.replace(' ', '_')
        return cleaned_filename





from enum import Enum

class ResponceSiginal(Enum):

    FILE_VALIDATED_SUCCESS = 'file validated successfully'

    FILE_TYPE_NOT_SUPPORTED = 'file type not supported'
    FILE_SIZE_EXCEEDED = 'file size exceeded'
    FILE_UPLOAD_SUCCESS = 'file upload succeeded'
    FILE_UPLOAD_FAILED = 'file upload failed'
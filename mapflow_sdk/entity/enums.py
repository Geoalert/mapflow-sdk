from enum import Enum

class ProcessingStatus(str, Enum):
    OK = "OK"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    UNPROCESSED = "UNPROCESSED"

from enum import Enum

class JobStatus(str, Enum):
    open = 'open'
    closed = 'closed'
    paused = 'paused'

class ApplicationStatus(str, Enum):
    pending = 'pending'
    reviewed = 'reviewed'
    rejected = 'rejected'
    accepted = 'accepted'

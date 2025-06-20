from enum import Enum

class UserRole(str, Enum):
    job_seeker = 'job_seeker'
    employer = 'employer'
    admin = 'admin'

class UserStatus(str, Enum):
    active = 'active'
    suspended = 'suspended'
    deleted = 'deleted'
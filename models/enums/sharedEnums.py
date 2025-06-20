from enum import Enum

class EmploymentType(str, Enum):
    full_time = 'full-time'
    contract = 'contract'
    part_time = 'part-time'
    everything = 'everything'

class ExperienceLevel(str, Enum):
    junior = 'junior'
    mid = 'mid'
    senior = 'senior'
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Education(BaseModel):
    institution: str
    degree: str
    fieldOfStudy: str
    startDate: datetime
    endDate: Optional[datetime]
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Experience(BaseModel):
    company: str
    title: str
    startDate: datetime
    endDate: Optional[datetime]
    description: Optional[str]
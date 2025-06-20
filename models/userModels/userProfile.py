from pydantic import BaseModel, Field
from typing import List, Optional, Annotated

from models.userModels.userEducation import Education
from models.userModels.userExperience import Experience


class Profile(BaseModel):
    skills: Annotated[List[str], Field(default_factory=list)]
    experience: Annotated[List["Experience"], Field(default_factory=list)]
    education: Annotated[List["Education"], Field(default_factory=list)]
    resumeUrl: Optional[str] = None
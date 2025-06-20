from datetime import datetime, UTC
from typing import Optional

from pydantic import BaseModel, Field, EmailStr

from models.enums.userEnums import UserRole, UserStatus
from models.modelHelpers.idHandler import PyObjectId
from models.userModels.userProfile import Profile


class BaseUser(BaseModel):
    role: UserRole = Field(...)
    names: str = Field(..., min_length=2, max_length=30)
    surnames: str = Field(..., min_length=2, max_length=30)
    email: EmailStr


#Add password to base user model on registration
class CreateUser(BaseUser):
    password:str


class HasHashedPassword(BaseModel):
    passwordHash:str


class SafeStoredUser(BaseUser):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    profile: Optional[Profile] = None
    createdAt: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(UTC))
    status: UserStatus = UserStatus.active
    model_config = {
        "populate_by_name": True,
        "json_encoders": {
            PyObjectId: lambda v: str(v)
        }
    }




class StoredUser(SafeStoredUser, HasHashedPassword):
    pass
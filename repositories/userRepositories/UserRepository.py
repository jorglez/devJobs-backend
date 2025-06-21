from datetime import datetime, UTC
from typing import Optional, List, override

from pydantic import EmailStr
from pymongo.collection import Collection

from interfaces.userInterfaces.IUserRepository import IUserRepository
from core.db import db
from models.enums.userEnums import UserStatus
from models.userModels.user import StoredUser, CreateUser
from utils.security.password import hash_password


class UserRepository(IUserRepository):

    def __init__(self):
        self.collection:Collection = db["users"]


    @override
    def get_all_users(self) -> List[StoredUser]:
        users_cursor = self.collection.find()
        return [StoredUser(**user) for user in users_cursor]

    @override
    def get_user_by_id(self, id: str) -> Optional[StoredUser]:
        pass

    @override
    def get_user_by_email(self, email: EmailStr) -> Optional[StoredUser]:
        return self.collection.find_one({"email":email})

    @override
    def create_user(self, user: CreateUser) -> dict:
        signup_time = datetime.now(UTC)
        user_to_store = {
            "names" : user.names,
            "surnames" : user.surnames,
            "createdAt" : signup_time,
            "updatedAt" : signup_time,
            "role" : user.role,
            "passwordHash" : hash_password(user.password),
            "email" : user.email,
            "status" : UserStatus.active
        }
        result = self.collection.insert_one(user_to_store)
        return result.inserted_id

    @override
    def update_user(self, user: StoredUser) -> dict:
        pass
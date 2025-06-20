from typing import Optional, List, override

from pydantic import EmailStr
from pymongo.collection import Collection

from interfaces.userInterfaces.IUserRepository import IUserRepository
from core.db import db
from models.userModels.user import StoredUser, CreateUser


class UserRepository(IUserRepository):

    def __init__(self):
        self.collection:Collection = db["users"]


    @override
    def get_all_users(self) -> List[StoredUser]:
        print(self.collection.find().to_list())
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
        result = self.collection.insert_one(dict(user))
        return result.inserted_id

    @override
    def update_user(self, user: StoredUser) -> dict:
        pass
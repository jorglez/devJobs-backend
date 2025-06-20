from abc import ABC, abstractmethod
from typing import List, Optional

from models.userModels.user import StoredUser, CreateUser


class IUserRepository(ABC):
    @abstractmethod
    def get_all_users(self) -> List[StoredUser]:
        pass

    @abstractmethod
    def get_user_by_id(self, id:str) -> Optional[StoredUser]:
        pass

    @abstractmethod
    def get_user_by_email(self, email:str) -> Optional[StoredUser]:
        pass

    @abstractmethod
    def create_user(self, user:CreateUser) ->dict:
        pass

    @abstractmethod
    def update_user(self, user: StoredUser) -> dict:
        pass
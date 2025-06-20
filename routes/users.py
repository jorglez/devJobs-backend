from fastapi import APIRouter, HTTPException

from models.generics.genericResponse import GenericResponse
from models.userModels.user import CreateUser, StoredUser
from repositories.userRepositories.UserRepository import UserRepository
from typing import List
router = APIRouter(prefix="/users", tags=["Users"])
col = UserRepository()

@router.get("/", response_model=GenericResponse[List[StoredUser]])
def get_all_users():
    data = col.get_all_users()
    return  #Falta esta parte

@router.post("/")
def create_user(user:CreateUser):
    try:
        if col.get_user_by_email(user.email):
            raise HTTPException(status_code=400, detail="email already exists")
        return col.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
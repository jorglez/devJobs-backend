from fastapi import APIRouter, HTTPException, status

from models.generics.genericResponse import GenericResponse
from models.userModels.user import CreateUser, StoredUser, SafeStoredUser
from repositories.userRepositories.UserRepository import UserRepository
from typing import List, Optional
from utils.queryManagement.apiResponse import custom_response
from utils.security.password import hash_password

router = APIRouter(prefix="/users", tags=["Users"])
col = UserRepository()

@router.get("/", response_model=GenericResponse[List[SafeStoredUser]])
def get_all_users():
    data = col.get_all_users()
    print(f"data obtenida en get all users: {data}")
    if len(data) > 0:
        return custom_response(
            status_code=status.HTTP_200_OK,
            data=[]
        )
    return  custom_response(
        status_code=status.HTTP_200_OK,
        data= [SafeStoredUser(**user.model_dump()) for user in data]
    )

@router.post("/", response_model=GenericResponse[Optional[dict]], status_code=201,
                 responses={
                     400: {
                         "model": GenericResponse[Optional[dict]],
                         "description": "Email already exists"
                     },
                     500: {
                         "description": "Internal server error"
                     }
                 }
             )
def create_user(user:CreateUser):
    try:
        if col.get_user_by_email(user.email):
            return custom_response(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Email already exists",
                status="error"
            )

        response = col.create_user(user)
        print(f"response of create new user = {response}")
        return custom_response(status_code=status.HTTP_201_CREATED, data={"success":True})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
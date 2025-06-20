from fastapi import FastAPI
from routes.users import router as users_router
app = FastAPI()

app.include_router(router=users_router)
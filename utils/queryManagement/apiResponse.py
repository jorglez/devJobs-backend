from fastapi.responses import JSONResponse

from models.generics.genericResponse import GenericResponse
from models.generics.genericResponse import T

def custom_response(
    *,
    status: str = "ok",
    status_code:int = 200,
    message:str = "",
    response:bool = True,
    data: T | None = None
)->JSONResponse:
    content = GenericResponse(
        status = status,
        status_code = status_code,
        message = message,
        response = response,
        data = data
    )
    return JSONResponse(status_code=status_code, content=content.model_dump())
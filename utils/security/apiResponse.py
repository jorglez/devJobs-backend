from models.generics.genericResponse import GenericResponse
from models.generics.genericResponse import T

def custom_response(
    *,
    status: str = "ok",
    status_code:int = 200,
    message:str = "",
    response:bool = True,
    data: T | None = None
)->GenericResponse[T]:
    return GenericResponse(
        status = status,
        status_code = status_code,
        message = message,
        response = response,
        data = data
    )
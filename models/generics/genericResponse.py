from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class GenericResponse(BaseModel, Generic[T]):
    status: str
    status_code: int
    message:str
    response:bool
    data: T | None = None


class PaginatedResponse(GenericResponse):
    page: int
    page_size: int
    total_items: int
    total_pages: int

from pydantic import BaseModel


class ExceptionResponse(BaseModel):
    error: str

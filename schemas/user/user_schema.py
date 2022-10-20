from pydantic import BaseModel, Field

EMAIL_REGEX = "^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$"

class LoginRequest(BaseModel):
    email: str = Field(..., description="Email")
    password: str = Field(..., description="Password")


class LoginResponse(BaseModel):
    token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh token")


class GetUserListResponse(BaseModel):
    id: int = Field(..., description="ID")
    email: str = Field(..., description="Email")
    nickname: str = Field(..., description="Nickname")

    class Config:
        orm_mode = True


class CreateUserRequest(BaseModel):
    email: str = Field(min_length=6, max_length=255, regex=EMAIL_REGEX, description="Email", example="a@a.com")
    password1: str = Field(..., description="Password1")
    password2: str = Field(..., description="Password2")
    nickname: str = Field(..., description="Nickname")
    phone: str = Field(..., description="Phone")


class CreateUserResponse(BaseModel):
    email: str = Field(..., description="Email")
    nickname: str = Field(..., description="Nickname")
    phone: str = Field(..., description="Phone")

    class Config:
        orm_mode = True

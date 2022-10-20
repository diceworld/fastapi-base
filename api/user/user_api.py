from typing import List

from fastapi import APIRouter, Depends, Query

from app.user.services import UserService
from core.fastapi.dependencies import (
    PermissionDependency,
    IsAdmin,
)
from schemas.base import ExceptionResponse
from schemas.user.user_schema import (
    LoginRequest,
    LoginResponse,
    GetUserListResponse,
    CreateUserResponse,
    CreateUserRequest
)

user_router = APIRouter(prefix="/users", tags=["User"])


@user_router.get(
    "",
    response_model=List[GetUserListResponse],
    response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponse}},
    dependencies=[Depends(PermissionDependency([IsAdmin]))],
)
async def get_user_list(
        limit: int = Query(10, description="Limit"),
        prev: int = Query(None, description="Prev ID"),
):
    return await UserService().get_user_list(limit=limit, prev=prev)


@user_router.post(
    "",
    response_model=CreateUserResponse,
    responses={"400": {"model": ExceptionResponse}},
)
async def create_user(request: CreateUserRequest):
    await UserService().create_user(**request.dict())
    return CreateUserResponse(
        **request.dict()
    )


@user_router.post(
    "/login",
    response_model=LoginResponse,
    responses={"404": {"model": ExceptionResponse}},
)
async def login(request: LoginRequest):
    token = await UserService().login(email=request.email, password=request.password)
    return {"token": token.token, "refresh_token": token.refresh_token}

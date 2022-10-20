from fastapi import APIRouter, Response, Depends

from app.auth.services.jwt_service import JwtService
from core.fastapi.dependencies import PermissionDependency, AllowAll
from schemas.auth.auth_schema import RefreshTokenRequest, VerifyTokenRequest, RefreshTokenResponse
from schemas.base import ExceptionResponse

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post(
    "/refresh",
    response_model=RefreshTokenResponse,
    responses={"400": {"model": ExceptionResponse}},
)
async def refresh_token(request: RefreshTokenRequest):
    token = await JwtService().create_refresh_token(
        token=request.token,
        refresh_token=request.refresh_token
    )
    return token


@auth_router.post("/verify", dependencies=[Depends(PermissionDependency([AllowAll]))])
async def verify_token(request: VerifyTokenRequest):
    await JwtService().verify_token(token=request.token)
    return Response(status_code=200)

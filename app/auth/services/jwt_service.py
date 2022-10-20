from sqlalchemy import select, and_

from core.db import session
from core.exceptions.token import RefreshTokenNotRegisteredException
from core.utils.token_helper import TokenHelper
from models.user import User
from schemas.auth.auth_schema import RefreshTokenResponse


class JwtService:
    async def verify_token(self, token: str) -> None:
        TokenHelper.decode(token=token)

    async def create_refresh_token(
        self,
        token: str,
        refresh_token: str,
    ) -> RefreshTokenResponse:
        token = TokenHelper.decode_expired_token(token=token)

        result = await session.execute(
            select(User).where(and_(User.id == token.get("user_id"), User.refresh_token == refresh_token))
        )
        user = result.scalars().first()
        if not user:
            raise RefreshTokenNotRegisteredException

        refresh_token = TokenHelper.encode(payload={"sub": "refresh"}, expire_period=60 * 60 * 24 * 7)
        user.refresh_token = refresh_token

        response = RefreshTokenResponse(
            token=TokenHelper.encode(payload={"user_id": token.get("user_id")}),
            refresh_token=refresh_token,
        )
        return response

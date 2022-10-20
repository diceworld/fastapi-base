from typing import Optional, List

from sqlalchemy import or_, select, and_

from core.db import Transactional, Propagation, session
from core.exceptions import (
    PasswordDoesNotMatchException,
    DuplicateEmailOrNicknameException,
    UserNotFoundException,
)
from core.utils.hash_helper import HashHelper
from core.utils.token_helper import TokenHelper
from models.user import User
from schemas.user.user_schema import LoginResponse


class UserService:
    def __init__(self):
        ...

    async def get_user_list(
        self,
        limit: int = 12,
        prev: Optional[int] = None,
    ) -> List[User]:
        query = select(User)

        if prev:
            query = query.where(User.id < prev)

        if limit > 12:
            limit = 12

        query = query.limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

    @Transactional(propagation=Propagation.REQUIRED)
    async def create_user(
        self, email: str, password1: str, password2: str, nickname: str, phone: str
    ) -> None:
        if password1 != password2:
            raise PasswordDoesNotMatchException

        query = select(User).where(or_(User.email == email, User.nickname == nickname))
        result = await session.execute(query)
        is_exist = result.scalars().first()
        if is_exist:
            raise DuplicateEmailOrNicknameException

        user = User(email=email,
                    password=HashHelper.encode(plaintext=password1),
                    nickname=nickname,
                    phone=phone)
        session.add(user)

    async def is_admin(self, user_id: int) -> bool:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            return False

        if user.is_admin is False:
            return False

        return True

    @Transactional(propagation=Propagation.REQUIRED)
    async def login(self, email: str, password: str) -> LoginResponse:
        result = await session.execute(
            select(User).where(and_(User.email == email, User.password == HashHelper.encode(plaintext=password)))
        )
        user = result.scalars().first()
        if not user:
            raise UserNotFoundException

        refresh_token = TokenHelper.encode(payload={"sub": "refresh"}, expire_period=60 * 60 * 24 * 7)
        user.refresh_token = refresh_token

        response = LoginResponse(
            token=TokenHelper.encode(payload={"user_id": user.id}),
            refresh_token=refresh_token,
        )
        return response

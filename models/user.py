from sqlalchemy import Column, BigInteger, Boolean, String, func, DATETIME

from core.db import Base
from core.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    """
    회원
    """
    __tablename__ = "user"
    __bind_key__ = "schema"
    __table_args__ = {"mysql_engine": "InnoDB", "schema": "schema"}

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False, comment="회원 id")
    email = Column(String(255), nullable=False, unique=True, comment="회원 이메일 (ID)")
    password = Column(String(255), nullable=False, comment="회원 비밀번호")
    refresh_token = Column(String(255), nullable=True, comment="리프레시 토큰")
    nickname = Column(String(20), nullable=False, unique=True, comment="별칭")
    phone = Column(String(20), nullable=False, comment="연락처")
    is_admin = Column(Boolean, default=False, comment="관리자 여부 (0: 일반, 1: 관리자)")
    status = Column(Boolean, nullable=False, default=True, index=True, comment="상태 (0: 탈퇴, 1: 활성")

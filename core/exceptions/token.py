from core.exceptions import CustomException


class DecodeTokenException(CustomException):
    code = 400
    error_code = "TOKEN_DECODE_ERROR"
    message = "token decode error"


class ExpiredTokenException(CustomException):
    code = 400
    error_code = "TOKEN_EXPIRE_TOKEN"
    message = "expired token"


class RefreshTokenNotRegisteredException(CustomException):
    code = 400
    error_code = "TOKEN_NOT_REGISTERED"
    message = "refresh token not registered"

from api.auth.auth_api import auth_router
from api.user.user_api import user_router

router_list = [
    user_router,
    auth_router,
]

__all__ = ["router_list"]

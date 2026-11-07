"""Phụ thuộc dùng chung cho router: người dùng hiện tại, kiểm tra vai trò (RBAC – FR-AD-02, NFR-08).

TODO(C2-07): giải mã JWT thật (app/core/security.py), nạp User từ CSDL, kiểm quyền theo lớp.
"""

from collections.abc import Callable
from dataclasses import dataclass
from uuid import UUID

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.errors import AppError
from app.models.enums import Role

bearer = HTTPBearer(auto_error=False)


@dataclass
class CurrentUser:
    id: UUID
    role: Role
    full_name: str = ""


def get_current_user(
    creds: HTTPAuthorizationCredentials | None = Depends(bearer),
) -> CurrentUser:
    if creds is None:
        raise AppError(401, "UNAUTHORIZED", "Thiếu token đăng nhập")
    # TODO(C2-07): from app.core.security import decode_access_token
    raise AppError(501, "NOT_IMPLEMENTED", "Xác thực chưa cài đặt – xem thẻ C2-07", {"card": "C2-07"})


def require_role(*roles: Role) -> Callable[[CurrentUser], CurrentUser]:
    def checker(user: CurrentUser = Depends(get_current_user)) -> CurrentUser:
        if user.role not in roles:
            raise AppError(403, "FORBIDDEN", "Vai trò không được phép")
        return user

    return checker


Lecturer = Depends(require_role(Role.LECTURER))
Student = Depends(require_role(Role.STUDENT))
Admin = Depends(require_role(Role.ADMIN))
AnyUser = Depends(get_current_user)
LecturerOrStudent = Depends(require_role(Role.LECTURER, Role.STUDENT))
LecturerOrAdmin = Depends(require_role(Role.LECTURER, Role.ADMIN))

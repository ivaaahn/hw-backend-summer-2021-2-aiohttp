import base64
import typing
from hashlib import sha256
from typing import Optional

from app.base.base_accessor import BaseAccessor
from app.admin.models import Admin
import bcrypt

if typing.TYPE_CHECKING:
    from app.web.app import Application


class AdminAccessor(BaseAccessor):
    async def connect(self, app: "Application"):
        first_admin = await self.create_admin(app.config.admin.email, app.config.admin.password)
        self.app.database.admins.append(first_admin)

    async def get_by_email(self, email: str) -> Optional[Admin]:
        for admin in self.app.database.admins:
            if admin.email == email:
                return admin
        return None

    async def create_admin(self, email: str, password: str) -> Admin:
        return Admin(self.app.database.next_admins_id, email, self._password_hasher(password))

    @staticmethod
    def _password_hasher(raw_password: str) -> str:
        hash_binary = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
        encoded = base64.b64encode(hash_binary)
        return encoded.decode('utf-8')

from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(primary_key=True, unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    registrated_at: Mapped[str] = mapped_column(default=datetime.now)
    roleid: Mapped[int] = mapped_column(ForeignKey("roles.id"))
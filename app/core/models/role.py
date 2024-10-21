from sqlalchemy import JSON

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

class Role(Base):
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(primary_key=True, unique=True, nullable=False, index=True)
    permissions: Mapped[str] = mapped_column(nullable=False)
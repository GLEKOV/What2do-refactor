from .base import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Article(Base):
    __tablename__ = "articles"

    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    body: Mapped[str] = mapped_column(unique=True)
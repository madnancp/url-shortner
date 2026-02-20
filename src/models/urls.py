from sqlalchemy import (
    Column,
    TEXT,
    INTEGER,
    VARCHAR,
    DATETIME,
    UUID,
    ForeignKey,
    Integer,
)
from src.database import Base


class Url(Base):
    __tablename__ = "urls"
    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    uuid = Column(UUID, unique=True, index=True)
    original_url = Column(TEXT, unique=True, index=True)
    stored_url = Column(VARCHAR(255), unique=True, index=True)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DATETIME, default="now()")
    updated_at = Column(DATETIME, default="now()")

    def __repr__(self) -> str:
        return f"<Url(id={self.id}, email='{self.stored_url}')"

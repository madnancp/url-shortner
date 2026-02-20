from sqlalchemy import Column, TEXT, INTEGER, VARCHAR, BOOLEAN, DATETIME, UUID
from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    uuid = Column(UUID, unique=True, index=True)
    email = Column(VARCHAR(255), unique=True, index=True)
    password = Column(TEXT)
    is_active = Column(BOOLEAN, default=True)
    created_at = Column(DATETIME, default="now()")
    updated_at = Column(DATETIME, default="now()")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email='{self.email}')"

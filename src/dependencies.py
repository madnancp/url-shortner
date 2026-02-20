from src.database import SessionLocal


def get_session():
    session = SessionLocal()
    try:
        return session

    finally:
        session.close()

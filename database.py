import os
import shutil
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    if os.getenv("VERCEL"):
        # Vercel serverless filesystem is read-only; /tmp is writable
        tmp_db = "/tmp/rangmanch.db"
        local_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rangmanch.db")
        if not os.path.exists(tmp_db) and os.path.exists(local_db):
            try:
                shutil.copyfile(local_db, tmp_db)
            except Exception:
                pass
        DATABASE_URL = f"sqlite:///{tmp_db}"
    else:
        DATABASE_URL = "sqlite:///./rangmanch.db"
elif DATABASE_URL.startswith("postgres://"):
    # SQLAlchemy requires postgresql://
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    echo=os.getenv("SQL_ECHO", "false").lower() == "true",
    connect_args=connect_args
)

def create_tables():
    """Create all tables defined by SQLModel Classes"""
    SQLModel.metadata.create_all(engine)  

def get_session():
    """Dependency that provides a database session per request"""
    with Session(engine) as session:
        yield session
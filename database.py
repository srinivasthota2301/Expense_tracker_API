from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = (
    "mysql+pymysql://avnadmin:AVNS__4H6kfF2w-YkG0mi2bY@"
    "mysql-4e56d22-srinivasthota2301-e69a.c.aivencloud.com:22292/defaultdb"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {}}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

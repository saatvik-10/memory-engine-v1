from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Memory(Base):
    __tablename__ = "memories"

    id = Column(String, primary_key=True)
    memory = Column(String, nullable=False)
    type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(DateTime)

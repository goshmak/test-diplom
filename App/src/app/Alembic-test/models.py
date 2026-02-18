from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    password  = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())
    role = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id!r}, name={self.name!r}, role={self.role!r})>"
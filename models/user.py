from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, String


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    username = Column(String)
    health_balance = Column(Float, default=0)

    tasks = relationship(
        "DailyTask", back_populates="user", cascade="all, delete-orphan"
    )
    user_levels = relationship("UserLevel", back_populates="user")

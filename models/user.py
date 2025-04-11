from sqlalchemy import Column, Integer, Float, String
from models.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    username = Column(String)
    health_balance = Column(Float, default=0)

from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float


class UserLevel(Base):
    __tablename__ = "user_levels"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    head_level = Column(Float, nullable=False)
    body_level = Column(Float, nullable=False)
    legs_level = Column(Float, nullable=False)
    arms_level = Column(Float, nullable=False)

    user = relationship("User", back_populates="user_levels")

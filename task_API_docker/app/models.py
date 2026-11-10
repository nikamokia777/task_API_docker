from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    title: Mapped[str] = mapped_column(String, index = True)
    description: Mapped[str] = mapped_column(String, index = True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default = False)
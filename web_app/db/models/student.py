from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from web_app.db.models.base import Base


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(length=20))
    last_name: Mapped[str] = mapped_column(String(length=25))

    def __repr__(self):
        return (f'Student(first_name={self.first_name}, '
                f'last_name={self.last_name})')

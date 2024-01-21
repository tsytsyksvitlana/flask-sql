from sqlalchemy import select, Sequence

from web_app.db.session import s
from web_app.db.models.course import Course


def get_courses() -> Sequence[Course]:
    query = select(Course)
    return s.users_db.scalars(query).all()

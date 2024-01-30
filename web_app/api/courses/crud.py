import typing as t
from sqlalchemy import select, insert, update
from sqlalchemy.orm import selectinload, joinedload

from web_app.db.session import s
from web_app.db.models.course import Course
from web_app.bl.models import CourseRequest


def get_courses() -> t.Sequence[Course]:
    query = select(Course).options(
        selectinload(Course.groups),
        selectinload(Course.students)
    )
    return s.users_db.scalars(query).all()


def get_course(course_id: int) -> Course | None:
    query = (
        select(Course)
        .options(
            joinedload(Course.groups),
            selectinload(Course.students)
        )
        .where(Course.id == course_id)
    )
    courses = s.users_db.scalar(query)
    return courses


def save_course(course: CourseRequest) -> int | None:
    insert_stmt = (
        insert(Course).values(**course.to_dict()).returning(Course.id)
    )
    _id = s.users_db.execute(insert_stmt).first()
    assert _id
    return _id[0]


def update_course_by_id(course: CourseRequest, course_id: int) -> int:
    update_stmt = update(Course).where(
        Course.id == course_id).values(**course.to_dict())
    result = s.users_db.execute(update_stmt)
    return result.rowcount

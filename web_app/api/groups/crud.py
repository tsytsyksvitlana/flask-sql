from sqlalchemy import select, func, Sequence, insert, update
from sqlalchemy.orm import joinedload, selectinload

from web_app.db.session import s
from web_app.db.models.group import Group
from web_app.db.models.student import Student
from web_app.db.models.course import Course
from web_app.bl.models import GroupRequest


def get_groups(
        course_id: int | None,
        student_id: int | None,
        count_students: int | None,
) -> Sequence[Group]:
    query = (
        select(Group).options(
            selectinload(Group.course),
            selectinload(Group.students))
    )
    if course_id:
        query = query.where(Group.course_id == course_id)
    if student_id:
        query = query.where(Group.students.any(Student.id == student_id))
    if count_students:
        query = query.join(Group.students).group_by(
            Group.id, Student.id, Group.course_id
        )
        query = query.having(func.count(Student.id) <= count_students)
    return s.users_db.scalars(query).all()


def get_group(group_id: int) -> Group | None:
    query = (
        select(Group)
        .options(
            joinedload(Group.course),
            selectinload(Group.students)
        )
        .where(Group.id == group_id)
    )
    groups = s.users_db.scalar(query)
    return groups


def save_group(group: GroupRequest) -> int | None:
    insert_group = (
        insert(Group).values(**group.to_dict()).returning(Group.id)
    )
    _id = s.users_db.execute(insert_group).first()
    assert _id
    return _id[0]


def update_group_by_id(group: GroupRequest, group_id: int) -> int:
    update_stmt = update(Group).where(
        Group.id == group_id).values(**group.to_dict())
    result = s.users_db.execute(update_stmt)
    return result.rowcount

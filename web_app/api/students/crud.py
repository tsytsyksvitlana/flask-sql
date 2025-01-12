import typing as t
from sqlalchemy import select, insert, update, delete

from web_app.db.session import s
from web_app.db.models.group import Group
from web_app.db.models.student import Student
from web_app.bl.models import StudentRequest


def get_students(group_name: str) -> t.Sequence[Student]:
    query = select(Student).where(Student.group.and_(Group.name == group_name))
    students = s.users_db.scalars(query).all()
    return students


def save_student(student: StudentRequest) -> int:
    insert_student = (
        insert(Student).values(**student.to_dict()).returning(Student.id)
    )
    _id = s.users_db.execute(insert_student).first()
    assert _id
    return _id[0]


def update_student_by_id(student: StudentRequest, student_id: int) -> int:
    update_stmt = update(Student).where(
        Student.id == student_id).values(**student.to_dict())
    result = s.users_db.execute(update_stmt)
    return result.rowcount


def delete_student_by_id(student_id: int) -> int:
    delete_stmt = delete(Student).where(Student.id == student_id)
    result = s.users_db.execute(delete_stmt)
    return result.rowcount

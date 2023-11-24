from flask import Blueprint, jsonify, Response

from web_app.db.session import s
from sqlalchemy import select, func
from web_app.db.models.group import Group
from web_app.db.models.student import Student


api_router = Blueprint('api_router', __name__)


@api_router.route('/groups/<int:students>', methods=["GET"])
def get_groups(students: int):
    subquery = s.users_db.query(Group.id, func.count(Group.student)
                                .label('student_count')).join(Group.student).group_by(Group.id)\
        .subquery()

    groups = s.users_db.query(Group).join(subquery, Group.id == subquery.c.id) \
        .filter(subquery.c.student_count <= students).all()

    if groups is None:
        return Response(f'Group with {students} students not exist.', status=404)
    return jsonify([group.to_dict() for group in groups])


@api_router.route('/students/<int:group_name>', methods=["GET"])
def get_student(group_name: str):
    students = s.users_db.scalars(
        select(Student).where(Student.groups == group_name)).all()

    if students is None:
        return Response(f'Student with group {group_name} not exist.', status=404)
    return jsonify([student.to_dict() for student in students])

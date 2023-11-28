from flask import Blueprint, jsonify, Response, request

from web_app.services.crud import get_groups, get_students, save_student
from web_app.bl.models import StudentRequest


api_router = Blueprint('api_router', __name__)


@api_router.route('/groups/<int:students>', methods=['GET'])
def groups(students: int) -> Response:
    groups = get_groups(students)
    if groups is None:
        return Response(f'Group with {students} or less students not exist.', status=404)
    return jsonify([group.to_dict() for group in groups])


@api_router.route('/students/<string:group_name>', methods=['GET'])
def students(group_name: str) -> Response:
    students = get_students(group_name)
    if students is None:
        return Response(f'Student with group {group_name} not exist.', status=404)
    return jsonify([student.to_dict() for student in students])


@api_router.route('/student', methods=['POST'])
def create_student() -> tuple | Response:
    try:
        student = StudentRequest(**(request.get_json()))
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)

    try:
        student_id = save_student(student)
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)
    return jsonify(dict(id=student_id)), 201

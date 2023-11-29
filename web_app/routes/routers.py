from flask import Blueprint, jsonify, Response, request

from web_app.services.crud import get_groups, get_students, save_student, delete_student_by_id, update_student_by_id
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
def create_student() -> tuple[Response, int] | Response:
    try:
        student = StudentRequest(**(request.get_json()))
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)

    try:
        student_id = save_student(student)
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)
    return jsonify(dict(id=student_id)), 201


@api_router.route('/student/<int:group_id>', methods=['POST'])
def student_to_group(group_id: int):
    try:
        request_data = request.get_json()
        request_data['group_id'] = group_id
        student = StudentRequest(**(request_data))
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)
    try:
        student_id = save_student(student)
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)
    return jsonify(dict(id=student_id)), 201


@api_router.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id: int) -> tuple[str, int]:
    res = delete_student_by_id(student_id)
    if res == 0:
        return f'Student with id={student_id} not fount', 404
    return '', 204


@api_router.route('/student/<int:student_id>', methods=['PUT'])
def update_student(student_id: int) -> tuple[str, int]:
    try:
        student = StudentRequest(**(request.get_json()))
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)
    res = update_student_by_id(student, student_id)
    if res == 0:
        return f'Student with id={student_id} not fount', 404
    return '', 204

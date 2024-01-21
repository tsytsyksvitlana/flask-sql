from flask import Blueprint, jsonify, Response, request

from web_app.students.crud import (
    get_students, save_student, delete_student_by_id, update_student_by_id)
from web_app.bl.models import StudentRequest


students_router = Blueprint('students_router', __name__)


@students_router.route('/students', methods=['GET'])
def students() -> Response:
    group_name = request.args.get('group_name')
    students = get_students(group_name)
    if students is None:
        return Response(f'Students not exist.', status=404)
    return jsonify([student.to_dict() for student in students])


@students_router.route('/student', methods=['POST'])
def create_student() -> tuple[Response, int] | Response:
    group_id = request.args.get('group_id')
    if group_id:
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
    else:
        try:
            student = StudentRequest(**(request.get_json()))
        except TypeError as e:
            return Response(f'Not valid data {e}', status=422)

        try:
            student_id = save_student(student)
        except TypeError as e:
            return Response(f'Not valid data {e}', status=422)
        return jsonify(dict(id=student_id)), 201


@students_router.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id: int) -> tuple[str, int]:
    res = delete_student_by_id(student_id)
    if res == 0:
        return f'Student with id={student_id} not exist', 404
    return '', 204


@students_router.route('/student/<int:student_id>', methods=['PUT'])
def update_student(student_id: int) -> tuple[str, int]:
    try:
        student = StudentRequest(**(request.get_json()))
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)
    res = update_student_by_id(student, student_id)
    if res == 0:
        return f'Student with id={student_id} not exist', 404
    return '', 204

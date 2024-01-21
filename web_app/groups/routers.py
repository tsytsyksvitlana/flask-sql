from flask import Blueprint, jsonify, Response, request
from web_app.groups.crud import get_groups, get_group

groups_router = Blueprint('groups_router', __name__)


@groups_router.route('/groups', methods=['GET'])
def groups() -> Response:
    course_id = request.args.get('course_id')
    student_id = request.args.get('student_id')
    count_students = request.args.get('count_students')

    groups = get_groups(course_id, student_id, count_students)
    if groups is None:
        return Response(f'Groups not exist.', status=404)
    return jsonify([group.to_dict() for group in groups])


@groups_router.route('/groups/<int:group_id>', methods=['GET'])
def group(group_id: int) -> Response:
    groups = get_group(group_id)
    if groups is None:
        return Response(f'Group with group_id = {group_id} not exist.', status=404)
    return jsonify([group.to_dict() for group in groups])

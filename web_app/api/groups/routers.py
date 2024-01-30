from flask import Blueprint, jsonify, Response, request

from web_app.bl.models import GroupRequest
from web_app.api.groups.crud import get_groups, get_group, save_group, update_group_by_id


groups_router = Blueprint('groups_router', __name__)


@groups_router.route('/groups/', methods=['GET'])
def get_route_groups() -> Response:
    course_id = request.args.get('course_id')
    student_id = request.args.get('student_id')
    count_students = request.args.get('count_students')

    groups = get_groups(course_id, student_id, count_students)
    if not groups:
        return Response(f'Groups not exist.', status=404)
    return jsonify([group.to_dict() for group in groups])


@groups_router.route('/group/<int:group_id>', methods=['GET'])
def get_route_group(group_id: int) -> Response:
    group = get_group(group_id)
    if group is None:
        return Response(f'Group with id = {group_id} not exist.', status=404)
    return jsonify([group.to_dict()])


@groups_router.route('/group', methods=['POST'])
def create_group() -> tuple[Response, int] | Response:
    try:
        group = GroupRequest(**request.get_json())
    except (TypeError, ValueError) as e:
        return Response(f'Not valid data {e}', status=422)

    try:
        group_id = save_group(group)
    except (TypeError, ValueError) as e:
        return Response(f'Not valid data {e}', status=422)
    return jsonify(id=group_id), 201


@groups_router.route('/group/<int:group_id>', methods=['PUT'])
def update_group(group_id: int) -> tuple[str, int] | Response:
    try:
        group = GroupRequest(**(request.get_json()))
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)
    res = update_group_by_id(group, group_id)
    if res == 0:
        return f'Group with id={group_id} not exist', 404
    return '', 200

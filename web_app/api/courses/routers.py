from flask import Blueprint, jsonify, Response, request

from web_app.api.courses.crud import get_courses, get_course, save_course, update_course_by_id
from web_app.bl.models import CourseRequest

courses_router = Blueprint('courses_router', __name__)


@courses_router.route('/courses', methods=['GET'])
def get_route_courses() -> Response:
    courses = get_courses()
    return jsonify([course.to_dict() for course in courses])


@courses_router.route('/course/<int:course_id>', methods=['GET'])
def get_route_course(course_id: int):
    course = get_course(course_id)
    if course is None:
        return Response(f'Course with id = {course_id} not exist.', status=404)
    return jsonify([course.to_dict()])


@courses_router.route('/course', methods=['POST'])
def create_course() -> tuple[Response, int] | Response:
    try:
        group = CourseRequest(**request.get_json())
    except (TypeError, ValueError) as e:
        return Response(f'Not valid data {e}', status=422)

    try:
        group_id = save_course(group)
    except (TypeError, ValueError) as e:
        return Response(f'Not valid data {e}', status=422)
    return jsonify(id=group_id), 201


@courses_router.route('/course/<int:course_id>', methods=['PUT'])
def update_course(course_id: int) -> tuple[str, int] | Response:
    try:
        course = CourseRequest(**(request.get_json()))
    except TypeError as e:
        return Response(f'Not valid data {e}', status=422)
    res = update_course_by_id(course, course_id)
    if res == 0:
        return f'Course with id={course_id} not exist', 404
    return '', 200

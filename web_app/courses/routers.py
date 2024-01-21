from flask import Blueprint, jsonify, Response
from web_app.courses.crud import get_courses

courses_router = Blueprint('courses_router', __name__)


@courses_router.route('/courses', methods=['GET'])
def courses() -> Response:
    courses = get_courses()
    return jsonify([course.to_dict() for course in courses])

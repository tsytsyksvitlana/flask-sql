from web_app.db.models.student import Student
from web_app.db.models.group import Group
from web_app.db.models.course import Course
from web_app.db.session import s
import json
from config import JSON_PATH


import logging

log = logging.getLogger(__name__)


def load_data_to_db(json_path: str = JSON_PATH) -> None:
    with open(json_path) as fp:
        data = json.load(fp)
    students = data["students"]
    groups = data["groups"]
    courses = data["courses"]

    students_res = []
    for i in range(len(students)):
        student = students[i]
        course = courses[i]
        course = Course(name=course["name"], description=course["description"])
        group = Group(name=groups[i], course=course)
        student = Student(
            first_name=student["first_name"], last_name=student["last_name"], group=group)
        students_res.append(student)
    s.users_db.add_all(students_res)
    s.users_db.commit()
    log.info('Data loaded successfully.')

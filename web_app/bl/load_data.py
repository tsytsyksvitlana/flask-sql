from tests.test_data.data import STUDENTS, GROUPS, COURSES
from web_app.db.models.student import Student
from web_app.db.models.group import Group
from web_app.db.models.course import Course
from web_app.db.session import s


import logging

log = logging.getLogger(__name__)


def load_data_to_db(
    groups: list[str], courses: list[(str, str,)], students: list[(str, str,)]
) -> None:
    i = 0
    students_res = []
    for first_name, last_name in students:
        i = +1
        student = Student(first_name=first_name, last_name=last_name)
        for course_name, course_desc in courses[i % 3]:
            course = Course(name=course_name, description=course_desc)
        group = Group(name=groups[i % 3])
        student = Student(first_name=first_name,
                          last_name=last_name, course=course, group=group)
        students_res.append(student)
    s.users_db.add_all(students_res)
    s.users_db.commit()
    log.info('Data loaded successfully.')

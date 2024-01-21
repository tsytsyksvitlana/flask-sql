from sqlalchemy import select

from web_app.db.session import s
from web_app.db.models.student import Student
from web_app.db.models.group import Group


def test_students(client):
    group_name = 'PZ-26'
    response = client.get(f'/students/?group_name={group_name}')
    assert response.status_code == 200
    query = select(Student).where(Student.group.has(Group.name == group_name))
    students = s.users_db.scalars(query).all()
    data = [student.to_dict() for student in students]
    response_data = response.get_json()
    assert response_data == data


def test_create_student(client):
    data = {
        "first_name": "Oleh",
        "last_name": "Franko",
        "group_id": "2"
    }
    response = client.post('/student', json=data)
    assert response.status_code == 201


def test_student_to_group(client):
    data = {
        "first_name": "Oleh",
        "last_name": "Franko",
    }
    response = client.post('/student/?group_id=2', json=data)
    assert response.status_code == 201


def test_delete_student(client):
    response = client.delete('/student/1')
    assert response.status_code == 204


def test_update_student(client):
    data = {
        "first_name": "Oleksii",
        "last_name": "Kovalenko",
        "group_id": "3"
    }
    response = client.put('/student/1', json=data)
    assert response.status_code == 204

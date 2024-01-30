import pytest


test_get_route_student_cases = [("PZ-26", "Oleksandr", "Kovalenko"),
                                ("TY-44", "Oleksii", "Melnyk")]


@pytest.mark.parametrize('group_name, first_name, last_name', (test_get_route_student_cases))
def test_get_route_students(client, group_name, first_name, last_name):
    response = client.get(f'/students/{group_name}')
    response_data = response.get_json()[0]
    assert response_data['first_name'] == first_name
    assert response_data['last_name'] == last_name
    assert response.status_code == 200


test_create_student_cases = [
    {
        "first_name": "Oleh",
        "last_name": "Franko",
        "group_id": "2"
    },
    {
        "first_name": "Victoria",
        "last_name": "Symonenko",
        "group_id": "6"
    }
]


@pytest.mark.parametrize('student_data', (test_create_student_cases))
def test_create_student(client, student_data):
    response = client.post('/student', json=student_data)
    assert response.status_code == 201


test_update_student_cases = [
    ({
        "first_name": "Oleh",
        "last_name": "Franko",
        "group_id": "2"
    }, '/student/1'),
    ({
        "first_name": "Victoria",
        "last_name": "Symonenko",
        "group_id": "6"
    }, '/student/5')
]


@pytest.mark.parametrize('student_data, route', (test_update_student_cases))
def test_update_student(client, student_data, route):
    response = client.put(route, json=student_data)
    assert response.status_code == 200


test_delete_student_cases = [('/student/1', 204),
                             ('/student/5', 204),
                             ('/student/12', 404)]


@pytest.mark.parametrize('student_route, status_code', (test_delete_student_cases))
def test_delete_student(client, student_route, status_code):
    response = client.delete(student_route)
    assert response.status_code == status_code

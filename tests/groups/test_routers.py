import pytest

test_groups_routes_status_cases = [
    ('/groups/?course_id=2', 200),
    ('/groups/?course_id=5', 200),
    ('/groups/?count_students=1', 200),
    ('/groups/?count_students=0', 404),
    ('/groups/?student_id=3', 200),
    ('/groups/?student_id=40', 404)
]


@pytest.mark.parametrize('route, code', (test_groups_routes_status_cases))
def test_groups_status(client, route, code):
    response = client.get(route)
    assert response.status_code == code


test_get_groups_routes_cases = [
    ('/groups/?course_id=2', 'YN-50'),
    ('/groups/?course_id=5', 'JK-50'),
    ('/groups/?count_students=3', 'PZ-26'),
    ('/groups/?student_id=3', 'CR-44')
]


@pytest.mark.parametrize('route, group', (test_get_groups_routes_cases))
def test_get_groups_routes(client, route, group):
    response = client.get(route)
    assert response.get_json()[0]['name'] == group


test_group_routes_status_cases = [
    ('/group/5', 200),
    ('/group/13', 404)
]


@pytest.mark.parametrize('route, code', (test_group_routes_status_cases))
def test_group_status(client, route, code):
    response = client.get(route)
    assert response.status_code == code


test_group_routes_cases = [
    ('/group/5', 'JK-50'),
    ('/group/2', 'YN-50')
]


@pytest.mark.parametrize('route, group_name', (test_group_routes_cases))
def test_get_group(client, route, group_name):
    response = client.get(route)
    assert response.get_json()[0]['name'] == group_name


test_create_group_cases = [
    {"name": "GH-23", "course_id": "2"},
    {"name": "KM-34", "course_id": "4"}
]


@pytest.mark.parametrize('group_data', (test_create_group_cases))
def test_create_group(client, group_data):
    response = client.post('/group', json=group_data)
    assert response.status_code == 201


test_update_group_cases = [
    ({"name": "GH-23", "course_id": "2"}, "/group/2"),
    ({"name": "KM-34", "course_id": "4"}, "/group/4")
]


@pytest.mark.parametrize('group_data, route', (test_update_group_cases))
def test_update_group(client, group_data, route):
    response = client.put(route, json=group_data)
    assert response.status_code == 200

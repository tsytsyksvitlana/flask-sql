import pytest

test_courses_routes_status_cases = [
    ('/course/1', 200),
    ('/course/5', 200),
    ('/course/32', 404)
]


@pytest.mark.parametrize('route, code', (test_courses_routes_status_cases))
def test_get_courses_status(client, route, code):
    response = client.get(route)
    assert response.status_code == code


test_courses_routes_cases = [
    (
        '/course/1',
        'Math',
        'The course includes the study of algebra and the beginnings of analysis.'
    ),
    (
        '/course/5',
        'Physics',
        'Master such areas of physics as mechanics, optics, electricity, '
        'molecular and quantum physics.'
    )
]


@pytest.mark.parametrize('route, name, description', (test_courses_routes_cases))
def test_get_courses(client, route, name, description):
    response = client.get(route)
    assert response.get_json()[0]['name'] == name
    assert response.get_json()[0]['description'] == description


test_create_course_cases = [
    {
        "name": "Biology",
        "description": "Discover life forms on Earth, from microorganisms "
                       "to complex organisms."
    },
    {
        "name": "Computer Science",
        "description": "Explore algorithms, data structures, and software"
                       " development."
    }
]


@pytest.mark.parametrize('course_data', (test_create_course_cases))
def test_create_course(client, course_data):
    response = client.post('/course', json=course_data)
    assert response.status_code == 201


test_update_course_cases = [
    (
        {
            "name": "Geometry",
            "description": "Explore basics of stereometry and geometric principles."
        },
        "/course/2"
    ),
    (
        {
            "name": "Integrated Science",
            "description": "Explore an integrated science course that blends "
                           "physics, natural sciences, and various scientific disciplines."
        },
        "/course/4"
    )
]


@pytest.mark.parametrize('course_data, route', (test_update_course_cases))
def test_update_course(client, course_data, route):
    response = client.put(route, json=course_data)
    assert response.status_code == 200

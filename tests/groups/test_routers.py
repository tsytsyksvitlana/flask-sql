import pytest

test_group_routes_status_cases = [('/groups/5', 200),
                                  ('/groups/133', 404)]


@pytest.mark.parametrize('route, code', (test_group_routes_status_cases))
def test_groups_status(client, route, code):
    response = client.get(route)
    assert response.status_code == code

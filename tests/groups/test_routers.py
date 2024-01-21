def test_groups(client):
    response = client.get('/groups/5')
    assert response.status_code == 200

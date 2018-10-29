def test_home_page(client,init_database):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/')
    assert response.status_code  == 200
    assert b'Jobplus' in response.data
    assert b'shiyanlou' in response.data

def test_login_logout(client,init_database):
    response = client.post('/login',data=dict(email='user@qq.com',password='123456'))
    assert response.status_code == 200
    assert b'Jobplus' in response.data
    assert b'x' in response.data

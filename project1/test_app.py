import pytest
import requests

def test_jwks_endpoint():
    response = requests.get('http://localhost:8080/jwks')
    assert response.status_code == 200
    assert 'keys' in response.json()

def test_auth_endpoint():
    response = requests.post('http://localhost:8080/auth')
    assert response.status_code == 200
    assert 'access_token' in response.json()

def test_expired_auth_endpoint():
    response = requests.post('http://localhost:8080/auth?expired=123')
    assert response.status_code == 200
    assert 'access_token' in response.json()

if __name__ == '__main__':
    pytest.main(['-s', __file__])

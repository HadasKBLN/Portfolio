import pytest
import json

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from server import app_factory


# Test GET method - get all the contacts
def test_get1_method_succes(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET) 
    THEN check that the response is valid
    """
    
    response = test_client.get('/')
    assert response.status_code == 200


# Test GET method - get person with specific id - SUCCES
def test_get2_method_succes(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person/<:id>' page is requested (GET) 
    THEN check that the response is valid
    """
    data = {"name":"Yisca Kablan", "number":"0246859736", "city":"Rehovot"}
    test_client.post('/person/1', json=data)
    response = test_client.get('/person/1')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "Yisca Kablan" in  data['name']


# Test GET method - get person with specific id - FAIL
def test_get2_method_fail(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person/<:id>' page is requested (GET) 
    THEN check that the response is valid
    """
    
    response = test_client.get('/person/33')
    assert response.status_code == 200
    data = response.json
    assert "Contact with such ID is not exist" in  data['message']
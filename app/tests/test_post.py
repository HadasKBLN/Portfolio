import pytest
import json

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from server import app_factory


# Test POST method - add new contact succesfully
def test_post_method_succes(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person' page is requested (POST) with full body
    THEN check that the response is valid
    """
    test_client.delete('/person/1')
    data = {"name":"Yisca Kablan", "number":"0246859736", "city":"Rehovot"}
    response = test_client.post('/person/1', json=data)
    assert response.status_code == 200
    data = response.json
    assert "New contact added succesfully!" in  data['message']
    
# Test POST method - try adding contact that already exist
def test_post_method_fail1(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person' page is requested (POST) with existing contact
    THEN check that the response is valid
    """
    data = {"name":"Yisca Kablan", "number":"0246859736", "city":"Rehovot"}
    response = test_client.post('/person/1', json=data)
    assert response.status_code == 200
    data = response.json
    assert "Contact with such ID already exist" in  data['message']

    
# Test POST method - try adding contact with missing fields
def test_post_method_fail2(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person' page is requested (POST) with missing fields in the body
    THEN check that the response is valid
    """
    data = {"name":"Yisca Kablan", "number":"0246859736"}
    response = test_client.post('/person/2', json=data)
    assert response.status_code == 200
    data = response.json
    assert "Some details are missing. Fill them and try again." in  data['message']
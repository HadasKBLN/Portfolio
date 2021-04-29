import pytest
import json

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from server import app_factory


# Test PUT method - update contact succesfully
def test_put_method_succes(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person' page is requested (PUT) with full body
    THEN check that the response is valid
    """
    data = {"city":"Jerusalem"}
    response = test_client.put('/person/1', json=data)
    assert response.status_code == 200
    data = response.json
    assert "Contact updated succesfully" in  data['message']

# Test PUT method - update contact succesfully
def test_put_method_failer(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person' page is requested (PUT) with id that not exist
    THEN check that the response is valid
    """
    data = {"city":"Jerusalem"}
    response = test_client.put('/person/3', json=data)
    assert response.status_code == 200
    data = response.json
    assert "No such contact. Enter id again" in  data['message']
    
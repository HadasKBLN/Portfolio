import pytest
import json

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from server import app_factory


# Test DELETE method - delete contact succesfully
def test_delete_method_succes(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person' page is requested (DELETE) with id of existing contact
    THEN check that the response is valid
    """
    data = {"name":"test", "number":"test", "city":"test"}
    test_client.post('/person/33', json=data)
    response = test_client.delete('/person/33')
    assert response.status_code == 200
    data = response.json
    assert "Contact deleted succesfully" in  data['message']


# Test DELETE method - not delete contact
def test_delete_method_fail(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/person' page is requested (DELETE) with id that not exist
    THEN check that the response is valid
    """
    # test_client.delete('/person/33')                           # validate contact with id 33 will not be exist
    response = test_client.delete('/person/333')
    assert response.status_code == 200
    data = response.json
    assert "Contact with such ID is not exist" in  data['message']
import pytest
import json

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from server import app_factory

# Setup
def test_setup(test_client):
    """ Testing seting up an app instance """
    assert test_client != None

# Test Home Page
def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"WELCOME!" in response.data
    assert b"you can add, delete, update and get a contact." in response.data


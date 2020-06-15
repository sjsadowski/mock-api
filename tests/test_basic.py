import sys, os, json

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")

import pytest
import falcon
from falcon import testing
from mockapi.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)

def test_assert_true(client):
    rdoc = {'status': '200 OK'}
    response = client.simulate_get('/')

    assert rdoc == json.loads(response.content)
    assert response.status == falcon.HTTP_OK
    assert True

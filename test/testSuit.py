import requests
import json
import jsonpath
import pytest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir))

from proto import *

testSuitRules = readJson("test/testCase.json")

baseUrl = testSuitRules["Setting"]["AppURL"]
testCase = testSuitRules["TestCase"]

@pytest.mark.parametrize("data", testCase)
def test_fetch_video(data):
    path = data["Route"]
    params = data["Params"]
    test_fetch_video.__doc__ = data["TestCase"]

    fetchURL = "{}{}".format(baseUrl,path)
    response = requests.get(url=fetchURL, params=params)
    responseJson = json.loads(response.text)

    assert response.status_code == data["StatusCode"]
    assert responseJson == data["ExceptedResponse"]
    

    
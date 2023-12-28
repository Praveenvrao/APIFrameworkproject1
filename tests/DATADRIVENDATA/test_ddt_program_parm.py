# Creating data driven test program

import requests
import pytest
import openpyxl

from source.Helpers.utils import verify_common_headers_json
from source.Helpers.api_requests_wrapper import post_request
from source.constants.Api_constants1 import fun_create_token


# read the file

def read_creds_from_xl(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=fun_create_token(), headers=verify_common_headers_json(), json=payload)
    return response

@pytest.mark.parametrize("user_cred",read_creds_from_xl("testdata_ddt_new.xlsx.xlsx"))
def test_post_create_token(user_cred):
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)

        response = make_request_auth(username, password)
        print(response)

        assert response.status_code == 200

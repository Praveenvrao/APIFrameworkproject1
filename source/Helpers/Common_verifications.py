#Verifying the HTTP Code and Json and Token
import requests
import pytest

def verify_status_code(response_data: object, expect_data: object) -> object:
    assert response_data.status_code == expect_data, "Expected status code is" + expect_data


def verify_json_key_for_notnull(key):
    assert key != 0, "key is not an empry" + key
    assert key > 0, "Key should be greater than zero"


def verify_response_key_should_not_be_none(key):
    assert key is not None


def verify_time():
    pass

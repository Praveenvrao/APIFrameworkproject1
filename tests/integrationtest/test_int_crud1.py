# Creating total crud program using Framework

import requests
import pytest

from source.constants.Api_constants1 import APIConstants_class, fun_create_booking, fun_create_token
from source.Helpers.utils import verify_common_headers_json
from source.Helpers.api_requests_wrapper import post_request
from source.Helpers.Common_verifications import verify_status_code, verify_response_key_should_not_be_none
from source.Helpers.Payload_manager import payload_create_booking, payload_create_token


# class test_crud1(object):
def test_create_token1():
    response = post_request(url=fun_create_token(), auth=None, headers=verify_common_headers_json(),
                            Payload=payload_create_token(), in_json=False)
    verify_status_code(response, expect_data=200)
    print(response.json())
    token = response.json()["token"]
    verify_response_key_should_not_be_none(token)
    print(token)
    return token

    def test_create_book1():
        response = post_request(url=fun_create_booking(), auth=None, headers=verify_common_headers_json(),
                                Payload=payload_create_booking(), in_json=False)
        print(response)
        verify_status_code(response, 200)
        bookid = response.json()["bookingid"]
        verify_response_key_should_not_be_none(bookid)
        print(bookid)

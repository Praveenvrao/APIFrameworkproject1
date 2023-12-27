# Create booking using framework

import requests
import pytest

from source.constants.Api_constants1 import APIConstants_class, fun_create_booking
from source.Helpers.utils import verify_common_headers_json
from source.Helpers.api_requests_wrapper import post_request
from source.Helpers.Common_verifications import verify_status_code, verify_response_key_should_not_be_none
from source.Helpers.Payload_manager import payload_create_booking


#class test_create_booking_tc1(object):
@pytest.mark.positive
def test_create_book1():
        response = post_request(url=fun_create_booking(), auth=None, headers=verify_common_headers_json(),
                                Payload=payload_create_booking(), in_json=False)
        print(response)
        verify_status_code(response, 200)
        bookid = response.json()["bookingid"]
        verify_response_key_should_not_be_none(bookid)
        print(bookid)
@pytest.mark.negative
def test_create_book2():
        response = post_request(url=fun_create_booking(), auth=None, headers=verify_common_headers_json(), Payload={},
                                in_json=False)
        print(response)
        verify_status_code(response, 500)
        # bookid = response.json()["bookingid"]
        # verify_response_key_should_not_be_none(bookid)
        # print(bookid)

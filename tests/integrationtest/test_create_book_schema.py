# Create booking using framework

import requests
import pytest

from source.constants.Api_constants1 import APIConstants_class, fun_create_booking
from source.Helpers.utils import verify_common_headers_json
from source.Helpers.api_requests_wrapper import post_request
from source.Helpers.Common_verifications import verify_status_code, verify_response_key_should_not_be_none
from source.Helpers.Payload_manager import payload_create_booking
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json
import os

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
        response_json = response.json()

        schema = {
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "default": {},
    "properties": {
        "bookingid": {
            "type": "integer",
            "default": 0
        },
        "booking": {
            "type": "object",
            "default": {},
            "properties": {
                "firstname": {
                    "type": "string",
                    "default": ""
                },
                "lastname": {
                    "type": "string",
                    "default": ""
                },
                "totalprice": {
                    "type": "integer",
                    "default": 0
                },
                "depositpaid": {
                    "type": "boolean",
                    "default": False
                },
                "bookingdates": {
                    "type": "object",
                    "default": {},
                    "properties": {
                        "checkin": {
                            "type": "string",
                            "default": ""
                        },
                        "checkout": {
                            "type": "string",
                            "default": ""
                        }
                    }
                },
                "additionalneeds": {
                    "type": "string",
                    "default": ""
                }
            }
        }
    }
}

        try:
            validate(response_json, schema=schema)
        except ValidationError as e:
            print(e.message)

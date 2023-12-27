import requests
import pytest

from source.constants.Api_constants1 import APIConstants_class, fun_create_booking, fun_create_token
from source.Helpers.utils import verify_common_headers_json, verify_common_headers_for_put_patch_delete
from source.Helpers.api_requests_wrapper import post_request, put_request, Delete_request
from source.Helpers.Common_verifications import verify_status_code, verify_response_key_should_not_be_none
from source.Helpers.Payload_manager import payload_create_booking, payload_create_token


class Test_full_crud():
    @pytest.fixture()
    def create_token1(self):
        response = post_request(url=fun_create_token(), auth=None, headers=verify_common_headers_json(),
                                Payload=payload_create_token(), in_json=False)
        verify_status_code(response, expect_data=200)
        print(response.json())
        token = response.json()["token"]
        verify_response_key_should_not_be_none(token)
        print(token)
        return token

    @pytest.fixture()
    def create_book1(self):
        response = post_request(url=fun_create_booking(), auth=None, headers=verify_common_headers_json(),
                                Payload=payload_create_booking(), in_json=False)
        print(response)
        verify_status_code(response, 200)
        bookid = response.json()["bookingid"]
        verify_response_key_should_not_be_none(bookid)
        print(bookid)
        return bookid

    def test_update_booking(self, create_token1, create_book1):
        put_url = fun_create_booking()+"/"+str(create_book1)
        response = put_request(url=put_url, auth=None, headers=verify_common_headers_for_put_patch_delete(),Payload=payload_create_booking(),in_json=False)
        print(response.json())


    def test_delete_booking(self,create_token1, create_book1):
        Del_url = fun_create_booking()+"/"+str(create_book1)
        response = Delete_request(url=Del_url,auth=None,headers=verify_common_headers_for_put_patch_delete(),Payload=None,in_json=False)
        print(response.status_code)


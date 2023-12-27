# Verifying common headers
import requests
import pytest

def verify_common_headers_json():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def verify_common_headers_xml():
    headers = {
        "Content-Type": "application/xml"
    }
    return headers

def verify_common_headers_for_put_patch_delete():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=",
    }
    return headers
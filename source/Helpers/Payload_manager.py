#Payload manager
import requests
import pytest
from faker import Faker
import json

faker = Faker
def payload_create_booking():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload



def dynamic_payload_create_booking():
    json_payload = {
        "firstname": faker.firstname(),
        "lastname": faker.lastname(),
        "totalprice": faker.random_int(min=1, max = 100),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2020-01-01"
        },
        "additionalneeds": faker.random_element(elements = ("Breakfast", "Parking", "WiFi", "Extra Bed"))
    }
    return json_payload



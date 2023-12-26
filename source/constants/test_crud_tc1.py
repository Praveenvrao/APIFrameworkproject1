from source.constants.Api_constants1 import Base_url, fun_base_url, APIConstants_class, fun_create_booking

def test_crud():
    print(Base_url)

    print(fun_create_booking())
    print(fun_base_url())
    url_class1 = APIConstants_class()
    print(url_class1.update_booking(5))

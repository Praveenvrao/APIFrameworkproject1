Base_url = "https://restful-booker.herokuapp.com"


def fun_base_url():
    return "https://restful-booker.herokuapp.com"


def fun_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def fun_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def fun_update_booking(self, booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)


class APIConstants_class(object):
    def __init__(self):
        self.booking_id = None

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def create_token():
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    def update_booking(self, bookid):
        return "https://restful-booker.herokuapp.com/booking/" + str(self.booking_id)

from dotenv import load_dotenv
import os

def test_auth_creds():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username, password)
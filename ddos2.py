import requests
import json
import uuid
import time
import random
from user_agent import generate_user_agent

def header():
    headers = {
        'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))
    }
    return headers

def generate_uuid():
    return str(uuid.uuid4())

def main():
    # Here, a series of requests are sent, aimed at logging into the site, by providing a username and password.
    # After the transactions are complete, a request is sent to keep the session open.
    username = input("Kullanıcı adı: ")
    password = input("Şifre: ")

    with requests.Session() as session:
        login_url = 'https://examplesite.com/login'
        data = {
            'username': username,
            'password': password,
            'remember_me': 'true'
        }
        headers = header()
        response = session.post(login_url, headers=headers, data=data)
        print(response.status_code)

        #stay logged in
        url = 'https://examplesite.com/profile'
        headers = header()
        response = session.get(url, headers=headers)
        print(response.status_code)

    while True:
        vpn_url = 'https:examplevpnsite.com//vpn/api//login'
        data = {
            'email': '',
            'password': ''
        }
        headers = header()
        response = requests.post(vpn_url, headers=headers, data=data)
        print(response.status_code)

        # send request
        url = 'https://examplesite/profil'
        headers = header()
        response = session.get(url, headers=headers)
        print(response.status_code)

        wait_time = random.randint(60, 300)
        print(f"Bir sonraki işlem {wait_time} saniye sonra yapılacak.")
        time.sleep(wait_time)

if __name__ == "__main__":
    main()


import requests
import json

encrypted_pass = "ENCRYPTED PASSWORD"


def authenticate(endpoint):

    base_url = "https://netmrioc2.marriott.com/api/3.7/"

    url = f"{base_url}{endpoint}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Basic  {encrypted_pass}",
    }
    try:
        response = requests.get(url, headers=headers, verify=False)

        if "status" in response.json() and response.json().get("status") != 200:
            raise Exception(response.json())

    except Exception as ex:
        f"Failure while getting device inventory => {ex}"

    return response


def get_devices():

    endpoint = "devices/?limit=10000"

    response = authenticate(endpoint)

    models = response.json()

    return models


def main():
    models = get_devices()
    with open("netmri_devices.json", "w") as f:
        f.write(json.dumps(get_devices(), indent=4))


if "__main__" == __name__:
    main()
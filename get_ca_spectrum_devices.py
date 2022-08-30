import requests
import json

encrypted_pass = "ENCRYPTED PASSWORD"


def authenticate(endpoint):

    base_url = "https://spctrm-oneclk-cnsl-marr-1.aws-use1.cloud.marriott.com:8443/spectrum/restful/"

    url = f"{base_url}{endpoint}"

    headers = {
        "Accept": "application/json",
        "Authorization": f"Basic  {encrypted_pass}",
    }
    try:
        response = requests.get(url, headers=headers,  verify=False)

        if "status" in response.json() and response.json().get("status") != 200:
            raise Exception(response.json())

    except Exception as ex:
        f"Failure while getting device inventory => {ex}"

    return response


def get_devices():

    endpoint = "devices?attr=0x1006e&attr=0x10000&throttlesize=100000"

    response = authenticate(endpoint)

    models = response.json()["model-response-list"]["model-responses"]["model"]

    return models


def main():
    models = get_devices()
    with open("ca_devices.json", "w") as f:
        f.write(json.dumps(get_devices(), indent=4))


if "__main__" == __name__:
    main()
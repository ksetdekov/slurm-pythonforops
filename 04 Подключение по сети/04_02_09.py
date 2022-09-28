import json
import requests


def main():
    base_url = "https://httpbin.org"

    payload = {
        "name": "Alexey",
        "job": "developer",
        "experience": 9
    }

    headers = {
        "X-Shop-Token": "vfhnsirf",
        "User-Agent": "Mega-Browser"
    }

    # response = requests.get(base_url +"/get", params=query_parms, headers=headers)
    try:
        response = requests.post(url=base_url + "/post",
                                 data=payload,
                                 headers=headers,
                                 timeout=3)

        jsonified_response_2 = json.loads(response.text)
        print(jsonified_response_2)

    except requests.exceptions.ConnectTimeout:
        print("Ресурс недоступен")


if __name__ == '__main__':
    main()

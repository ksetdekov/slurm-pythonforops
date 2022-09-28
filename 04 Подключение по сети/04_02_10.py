import json
import requests


def main():
    session = requests.Session()
    base_url = "https://httpbin.org"

    query_params = {
        "order": "votes",
        "sort": "desc"
    }

    headers = {
        "X-Shop-Token": "vfhnsirf",
        "User-Agent": "Mega-Browser"
    }

    # response = requests.get(base_url +"/get", params=query_parms, headers=headers)
    try:
        response = session.post(url=base_url + "/post",
                                params=query_params,
                                headers=headers,
                                timeout=3)

        jsonified_response_2 = json.loads(response.text)
        print(jsonified_response_2)

    except requests.exceptions.ConnectTimeout:
        print("Ресурс недоступен")


if __name__ == '__main__':
    main()

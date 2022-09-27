import json
import requests
def main():
    session = requests.Session()
    base_url = "https://httpbin.org"

    query_params = {
        "param1": "foo",
        "param2": "bar"
    }

    headers = {
        "User-Agent": "Chrome",
        "Authorization": "Bearer: sfsdfsfd"
    }

    payload = {
        "id": 12313,
        "name": "python"
    }
    
    with open("README.md") as text_file:
        files = {
            "text_file": text_file
        }

    # response = requests.get(base_url +"/get", params=query_parms, headers=headers)
        try:
            response = session.post(url=base_url + "/post",
                                    params=query_params,
                                    headers=headers,
                                    data=payload,
                                    files=files,
                                    timeout=3)

            response_2 = session.get(url=base_url + "/get",
                                     params=query_params,
                                     headers=headers,
                                     timeout=0.01)
            print(response.status_code)
            print(response.text)
            jsonified_response_2 = json.loads(response_2.text)
            print(jsonified_response_2)
        except requests.exceptions.ConnectTimeout:
            print("Ресурс недоступен")




if __name__ == '__main__':
    main()
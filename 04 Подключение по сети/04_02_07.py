import requests
def main():
    base_url = "https://httpbin.org"

    response = requests.get(base_url +"/get")
    print(response)

if __name__ == '__main__':
    main()
from os import getenv
import json
from requests import Session


class Credentials:
    """credentials for trello for REST API
    """

    def __init__(self) -> None:
        with open('04 Подключение по сети/secret_info.json') as f:
            secrets = json.load(f)
        self.__api_token = secrets["TRELLO_API_TOKEN"]
        self.__api_key = secrets["TRELLO_API_key"]

        # self.__api_token = getenv("TRELLO_API_TOKEN")
        # self.__api_key = getenv("TRELLO_API_key")

    def get_creds_as_query_params(self):
        return {
            "key": self.__api_key,
            "token": self.__api_token
        }


def get_boards(session: Session, creds: Credentials):
    boards = session.get("https://api.trello.com/1/members/me/boards",
                         params=creds.get_creds_as_query_params()).json()
    return {board["name"]: {
        "id": board["id"],
        "columns": get_board_columns(session, creds, board["id"])
    } for board in boards}


def get_board_columns(session: Session, creds: Credentials, board_id: str):
    columns = session.get(
        f"https://api.trello.com/1/boards/{board_id}/lists", params=creds.get_creds_as_query_params()).json()
    return {column["name"]: column["id"] for column in columns}

def create_task(session: Session, creds: Credentials, board_id: str):
    url = "https://api.trello.com/1/cards"

    query = {
        'key': '23432',
        'token': 'sdfsdfd',
        'idList': 'sdfsdf'
    }


def main():
    trello_creds = Credentials()
    trello_sessions = Session()
    boards_dict = get_boards(trello_sessions, trello_creds)
    for board_name, board_info in boards_dict.items():
        print(f"Доска {board_name}")
        for column_name in board_info["columns"].keys():
            print(f"Колонка {column_name}")
    task_name = input("ввести называние задачи")
    col_name = input("ввести называние колонки")
    description = input("ввести описание задачи")
    print(task_name)
    print(col_name)
    print(description)


if __name__ == '__main__':
    main()

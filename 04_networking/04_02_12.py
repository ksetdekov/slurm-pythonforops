# from os import getenv
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


def create_task(session: Session, creds: Credentials, column_id: str, task_details: dict):
    params = {**creds.get_creds_as_query_params(),
              **task_details,
              "idList": column_id
              }
    results = session.post("https://api.trello.com/1/cards", params=params)
    print(results.status_code)
    print(results.text)


def main():
    trello_creds = Credentials()
    trello_sessions = Session()
    boards_dict = get_boards(trello_sessions, trello_creds)
    for board_name, board_info in boards_dict.items():
        print(f"Доска {board_name}")
        for column_name in board_info["columns"].keys():
            print(f"Колонка {column_name}")
    task_details = {
        "name": input("ввести называние задачи"),
        "desc": input("ввести описание задачи")

    }
    col_name = input("ввести называние колонки")
    print(col_name)

    used_column_id = None
    for board_name, board_info in boards_dict.items():
        for column_name, column_id in board_info["columns"].items():
            if column_name == col_name:
                used_column_id = column_id

    create_task(trello_sessions, trello_creds, used_column_id, task_details)


if __name__ == '__main__':
    main()

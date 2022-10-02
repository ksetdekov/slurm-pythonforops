import json


class Credentials:
    def __init__(self):
        self.postgres_url = "http://localhost:8080/"
        self.postgres_cred = {"host": "localhost",
                              "user": "postgres",
                              "password": "q1w2e3",
                              "database": "postgres",
                              "port": 5432
                              }
        self.open_ssh_cred = {"host": "localhost",
                              "port": 2222,
                              "user": "service_user",
                              "password": "q1w2e3"
                              }

    def __str__(self):
        return json.dumps({"url": self.postgres_url,
                           "postgres_cred": self.postgres_cred,
                           "ssh_cred": self.open_ssh_cred}, indent=4)

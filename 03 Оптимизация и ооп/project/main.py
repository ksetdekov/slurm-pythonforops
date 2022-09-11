# running
# $ curl localhost:21122/monitoring/infrastructure/using/summary/1 | python main.py
def main():
    a = input()
    teams = a.split("$")
    # 4 teams
    team_name, resources = teams[0].split("|")
    print(team_name)
    list_of__resources = resources.split(";")
    print(list_of__resources[0])
    # (SZY1417,CPU,2022-09-03 14:44:28,7)
    res_name, metric, _, value = list_of__resources[0].strip(")(").split(',')
    value = int(value)
    print(res_name, metric, value)


if __name__ == '__main__':
    main()

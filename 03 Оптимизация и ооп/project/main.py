import pandas as pd

# running
# $ curl localhost:21122/monitoring/infrastructure/using/summary/1 | python main.py
final_dict = {}
def main():
    a = input()
    teams = a.split("$")
    for team in teams:
        # 4 teams
        team_name, resources = team.split("|")
        # print(team_name)
        list_of__resources = resources.split(";")
        for row in list_of__resources:
            # print(row)
            # (SZY1417,CPU,2022-09-03 14:44:28,7)
            res_name, metric, time, value = row.strip(")(").split(',')
            value = int(value)
            final_dict[(team_name, res_name, metric, time)] = value

            # print(team_name, res_name, metric, time,  value)

    index_complex = pd.MultiIndex.from_tuples(final_dict.keys(), names=["team", "resource", "metric", "time"])
    result_df = pd.DataFrame(data={'value':final_dict.values()}, index=index_complex)
    
    print(result_df.groupby(level=[0,1,2]).agg(['mean', 'median']))

if __name__ == '__main__':
    main()

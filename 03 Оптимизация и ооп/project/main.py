import re
from sys import orig_argv
from types import MemberDescriptorType
from unittest import result
import pandas as pd

# running
# $ curl localhost:21122/monitoring/infrastructure/using/summary/1 | python main.py
TEST_ON_TXT = True

def createDictFromPandas(df):
    if (df.index.nlevels==1):
        return df.to_dict(orient='index')
    dict_f = {}
    for level in df.index.levels[0]:
        if (level in df.index):
            dict_f[level] = createDictFromPandas(df.xs([level]))
    return dict_f



def calculate_direction(mean, median):
    """решение задачи сравнения среднего и медианы

    :param mean: среднее
    :type mean: float
    :param median: медиаана
    :type median: float
    :return: строка результата сравнения
    :rtype: str
    """
    # usage_type - тип нагрузки: скачки, стабильная, и снижения.
    # Если среднее загрузки ресурса по измерению (CPU/RAM/NetFlow) составляет менее 75% от медианы, тип нагрузки: снижения
    # Если среднее составляет более 125% от медианы, тип нагрузки: скачки
    # Если среднее между 75% и 125% от медианы включительно, типа нагрузки: стабильная
    direction = mean / median - 1
    if direction > 0.25:
        directions_result = "Spikes"
    elif direction < -0.25:
        directions_result = "Drops"
    else:
        directions_result = "Stable"
    return directions_result

def assess_intesity(value):
    # Если медиана загрузки ресурса по измерению больше нуля и меньше или равна 30, то интенсивность низкая.
    # Если медиана загрузки ресурса по измерению больше 30 и меньше или равна 60, то интенсивность умеренная. 
    # Если медиана загрузки ресурса по измерению больше 60 и меньше или равна 90, то интенсивность высокая.
    # Если медиана загрузки ресурса по измерению больше 90, то интенсивность запредельная. 
    if 0<value<=30:
        intensity = 'Low'
    elif value <=0:
        intensity = None
    elif value <=60:
        intensity = 'Medium'
    elif value <=90:
        intensity = 'High'
    else:
        intensity = 'Overwhelming'
    return intensity

def get_decision(intensity, usage_type):
# delete resource|
# |APT-323|RAM|74|43.0|Stable|Medium|normal using|
# |DHH-HW1|RAM|52.56|55.5|Stable|Extreme|extend resource|
    if intensity=='Low' or (intensity=='Medium' and usage_type=='Drops') or intensity is None:
        decision = 'delete resource'
    elif intensity=='Overwhelming' or (intensity=='High' and usage_type=='Spikes'):
        decision = 'extend resource'
    else:
        decision = 'normal using'
    return decision
    # Ресурс используется с низкой интенсивностью и тип загрузки - снижения. От такого ресурса нужно отказаться.
    # Ресурс используется с низкой интенсивностью и тип загрузки - стабильная. От такого ресурса нужно отказаться.
    # Ресурс используется с низкой интенсивностью и тип загрузки - скачки. От такого ресурса нужно отказаться.
    # Ресурс используется с умеренной интенсивностью и тип загрузки - снижения. От такого ресурса нужно отказаться.
    # Ресурс используется с умеренной интенсивностью и тип загрузки - стабильная. Такой ресурс остается у команды в неизменном виде.
    # Ресурс используется с умеренной интенсивностью и тип загрузки - скачки. Такой ресурс остается у команды в неизменном виде.
    # Ресурс используется с высокой интенсивностью и тип загрузки - снижения. Такой ресурс остается у команды в неизменном виде.
    # Ресурс используется с высокой интенсивностью и тип загрузки - стабильная. Такой ресурс остается у команды в неизменном виде.
    # Ресурс используется с высокой интенсивностью и тип загрузки - скачки. Такой ресурс остается у команды и его необходимо усилить.
    # Ресурс используется с запредельной интенсивностью и тип загрузки - снижения. Такой ресурс остается у команды и его необходимо усилить
    # Ресурс используется с запредельной интенсивностью и тип загрузки - стабильная. Такой ресурс остается у команды и его необходимо усилить
    # Ресурс используется с запредельной интенсивностью и тип загрузки - скачки. Такой ресурс остается у команды и его необходимо усилить.



def metric_estimator(row):
    row['usage_type'] = calculate_direction(row['mean'], row['mediana'])
    row['intensity'] = assess_intesity(row['mediana'])
    row['decision'] = get_decision(row['intensity'], row['usage_type'])
    return row
    
def main():
    final_dict = {}
    if TEST_ON_TXT:
        with open('03 Оптимизация и ооп/project/test.txt', 'r') as file:
            a = file.read()
    else:
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
    # получаем из словаря мультииндекс и создаем df из исходных данных
    index_complex = pd.MultiIndex.from_tuples(final_dict.keys(), names=["team", "resource", "metric", "time"])
    result_df = pd.DataFrame(data={'value':final_dict.values()}, index=index_complex)
    # считаем аггрегаты
    transformed_df = result_df.groupby(level=[0,1,2]).agg(['mean', 'median'])

    transformed_df.columns = ['mean', 'mediana']
    print(transformed_df)

    transformed_df = transformed_df.apply(metric_estimator, axis=1)

    print(transformed_df)
    
    print(createDictFromPandas(transformed_df))


if __name__ == '__main__':
    main()

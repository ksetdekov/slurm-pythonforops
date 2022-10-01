import json
import pandas as pd
import os
import logging
import requests

# running
# $ curl localhost:21122/monitoring/infrastructure/using/summary/1 | python main.py
URL_TO_ACCESS = "http://localhost:21122/monitoring/infrastructure/using/summary/1"
TEST_ON_TXT = False
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
if TEST_ON_TXT:
    logging.info("Тестовый режим - работа с файлом test.txt")


def create_dict_from_pandas(df):
    """рекурсивная функция для создания словаря в нужном формате

    :param df: df с мульри индексом
    :type df: pd.DataFrame
    :return: словарь с рекурсивными ключами
    :rtype: dict
    """
    if df.index.nlevels == 1:
        return df.to_dict(orient='index')
    dict_f = {}
    for level in df.index.levels[0]:
        if level in df.index:
            dict_f[level] = create_dict_from_pandas(df.xs(level))
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
    direction = mean / median - 1
    if direction > 0.25:
        directions_result = "Spikes"
    elif direction < -0.25:
        directions_result = "Drops"
    else:
        directions_result = "Stable"
    return directions_result


def assess_intesity(value):
    if 0 < value <= 30:
        intensity = 'Low'
    elif value <= 0:
        intensity = None
    elif value <= 60:
        intensity = 'Medium'
    elif value <= 90:
        intensity = 'High'
    else:
        intensity = 'Overwhelming'
    return intensity


def get_decision(intensity, usage_type):
    """оценка того что делать с ресурсом

    :param intensity: интерсивность
    :type intensity: str
    :param usage_type: использование
    :type usage_type: str
    :return: решение
    :rtype: str
    """
    # delete resource|
    # |APT-323|RAM|74|43.0|Stable|Medium|normal using|
    # |DHH-HW1|RAM|52.56|55.5|Stable|Extreme|extend resource|
    if intensity == 'Low' or (intensity == 'Medium' and usage_type == 'Drops') or intensity is None:
        decision = 'delete resource'
    elif intensity == 'Overwhelming' or (intensity == 'High' and usage_type == 'Spikes'):
        decision = 'extend resource'
    else:
        decision = 'normal using'
    return decision


def add_aggregates_to_row(row):
    """функция для записи расчитанных метрик в колонки

    :param row: строка датафрейма
    :type row: pd.Series
    :return: возвращает модифицированную строку
    :rtype: pd.Series
    """
    row['usage_type'] = calculate_direction(row['mean'], row['mediana'])
    row['intensity'] = assess_intesity(row['mediana'])
    row['decision'] = get_decision(row['intensity'], row['usage_type'])
    return row


def calculate_aggregates(df):
    """считает средние и медиану и оценивает тип загрузки, интенсивности и принятия решений

    :param df: df c информацей до агрегации
    :type df: pd.DataFrame
    :return: df с форматом, как хотят на вывод
    :rtype: pd.DataFrame
    """
    df_transformed = df.groupby(level=[0, 1, 2]).agg(['mean', 'median'])
    df_transformed.columns = ['mean', 'mediana']
    df_transformed = df_transformed.apply(add_aggregates_to_row, axis=1)
    return df_transformed


def save_to_md(df_to_save, filename):
    """сохраняем и форматируем отчет в .md

    :param df_to_save: таблицу, которую сохранять
    :type df_to_save: pd.DataFrame
    :param filename: путь для сохранения
    :type filename: str
    """
    logging.info(
        f"сохраняем отчеты для этих команд :{', '.join(list(df_to_save.index.get_level_values(0).unique()))}")
    with open(filename, "w") as markdown_results:
        markdown_results.write("# Отчет по ресурсам по командам")
        for team_name in df_to_save.index.get_level_values(0).unique():
            markdown_results.write("\n\n")
            subset_df = df_to_save.loc[team_name]
            markdown_results.write(f"## Команда {team_name}")
            markdown_results.write("\n\n")
            markdown_results.write(
                subset_df.reset_index().to_markdown(index=False))
        markdown_results.write("\n")


def get_raw_input_data(url):
    if TEST_ON_TXT:
        logging.info("считываем данные из файла")
        logging.info(
            f"мы в директории с этими файлами {os.listdir(os.curdir)}")
        with open('test.txt', 'r') as file:
            raw_input_string = file.read()
        logging.info("закончили читать файл")
    else:
        logging.info("получаем информацию по сети")
        response = requests.get(url)
        raw_input_string = response.text
    return raw_input_string


def parse_string_to_dict(raw_input_string):
    logging.info("начали парсинг")
    final_dict = {}
    for team in raw_input_string.split("$"):
        # 4 teams
        team_name, resources = team.split("|")
        list_of__resources = resources.split(";")
        for row in list_of__resources:
            # (SZY1417,CPU,2022-09-03 14:44:28,7)
            res_name, metric, time, value = row.strip(")(").split(',')
            final_dict[(team_name, res_name, metric, time)] = int(value)
    logging.info("закончили парсинг")
    return final_dict


def write_dict_to_disk(dictionary_required, dict_location="dict.json"):
    with open(dict_location, "w") as json_output_file:
        json_output_file.write(json.dumps(dictionary_required, indent=4))


def main():
    raw_input_string = get_raw_input_data(url=URL_TO_ACCESS)
    final_dict = parse_string_to_dict(raw_input_string)
    # получаем из словаря мультииндекс и создаем df из исходных данных
    index_complex = pd.MultiIndex.from_tuples(
        final_dict.keys(), names=["team", "resource", "metric", "time"])
    result_df = pd.DataFrame(
        data={'value': final_dict.values()}, index=index_complex)
    # считаем аггрегаты
    aggregated_df = calculate_aggregates(result_df)

    # готов словарь
    dictionary_required = create_dict_from_pandas(aggregated_df.drop(columns="decision"))

    # записали на диск
    write_dict_to_disk(dictionary_required)
    logging.info("вывод нужного словаря")
    print(dictionary_required)

    # готовы таблички сохраняем на диск
    save_to_md(df_to_save=aggregated_df, filename="reports.md")


if __name__ == '__main__':
    main()

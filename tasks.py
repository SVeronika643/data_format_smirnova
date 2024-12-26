# 15. Запишите в файл формата CSV следующую информацию из YAML-файла `gitlab-ci.yml`: 
# Посчитайте количество состояний `stage` каждого типа, которые встречаются в файле.

import yaml
import csv
from collections import Counter

def count_stages_in_yaml(yaml_file, csv_file):
    # Чтение YAML файла
    with open(yaml_file, 'r') as file:
        content = yaml.safe_load(file)

    # Счетчик для хранения количества состояний stage
    stage_counter = Counter()

    # Проход по всем заданиям в YAML
    if 'stages' in content:
        for stage in content['stages']:
            stage_counter[stage] += 1

    # Запись результатов в CSV файл
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Stage Type', 'Count'])  # Заголовки столбцов
        for stage_type, count in stage_counter.items():
            writer.writerow([stage_type, count])

# Пример использования функции
count_stages_in_yaml('gitlab-ci.yml', 'stages_count.csv')

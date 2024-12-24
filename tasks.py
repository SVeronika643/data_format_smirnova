# 15. Запишите в файл формата CSV следующую информацию из YAML-файла `gitlab-ci.yml`: 
# Посчитайте количество состояний `stage` каждого типа, которые встречаются в файле.

import yaml
import json

# Чтение данных из YAML файла
with open('mkdocs.yml', 'r', encoding='utf-8') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Извлечение информации о социальных сетях
social_links = yaml_data.get('social', {})

# Запись данных в JSON файл
with open('social_links.json', 'w', encoding='utf-8') as json_file:
    json.dump(social_links, json_file, ensure_ascii=False, indent=4)

print("Информация о ссылках на социальные сети успешно записана в social_links.json.")

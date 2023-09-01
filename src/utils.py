import json
from datetime import datetime
from operator import itemgetter
from src.main import file_json_setup


def load_file(file_json):
    """Функция возвращает список операций из файла json"""
    with open(file_json) as file:
        file = json.load(file)
        return file


def successful_operations():
    """Функция возвращает список успешных операций"""
    file = load_file(file_json_setup)
    executed_operations = []
    for item in file:
        if not item:
            continue
        if item['state'] == "EXECUTED":
            executed_operations.append(item)
    return executed_operations


def sorting_date_list():
    """Функция возвращает отсортированный по дате список"""
    date_operations = successful_operations()
    number_of_operations = 5
    return sorted(date_operations, key=itemgetter('date'), reverse=True)[0:number_of_operations]


def required_date_format(date_time):
    """Функция возвращает требуемый формат даты"""
    date_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(date_obj.date(), '%d.%m.%Y')


def required_card_format(card_number):
    """Функция возвращает требуемый формат номера карты"""
    if card_number:
        numbers = ""
        for item in card_number:
            if item.isdigit():
                numbers += item
        string_out = card_number[:card_number.find(numbers) - 1]  # символьный раздел
        numbers_out = card_number[card_number.find(numbers):]  # цифровой раздел
        if len(numbers_out) == 16:
            numbers_out = numbers_out[:4] + ' ' + numbers_out[4:6] + "**" + " " + "****" + " " + numbers_out[-4:]
        elif len(numbers_out) == 20:
            numbers_out = "**" + numbers_out[-4:]
        return f"{string_out} {numbers_out}"
    else:
        return "VVVVVVVV"

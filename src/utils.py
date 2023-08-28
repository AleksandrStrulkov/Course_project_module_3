import json
import datetime


def load_file(file_json):
    """Функция возвращает список операций из файла json"""
    with open(file_json, 'r', encoding="utf-8") as file:
        file = json.load(file)
        return file


def successful_operations():
    """Функция возвращает список успешных операций"""
    pass


def sorting_date_list():
    """Функция возвращает отсортированный по дате список"""
    pass


def required_date_format():
    """Функция возвращает требуемый формат даты"""
    pass


def required_card_format():
    """Функция возвращает требуемый формат номера карты"""
    pass


from src.utils import *

file_json_setup = 'C:/Users/astru/PycharmProjects/Coursework module 3/json_files/operations.json'


def start_programs():
    out_operations = sorting_date_list()
    for item in out_operations:
        print(required_date_format(item['date']) + ' ' + ' ' + item["description"])
        print(f"{required_card_format(item.get('from'))} ---> {required_card_format(item.get('to'))}")
        print(f"{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}")
        print()


if __name__ == "__main__":
    start_programs()

from src.utils import *


filename = '../json_files/operations.json'
json_file = load_file(filename)


def test_load_file():
    assert type(json_file) == list


def test_successful_operations():
    for item in successful_operations():
        assert item['state'] == "EXECUTED"


def test_sorting_date_list():
    pass
    # operations_list_five = sorting_date_list()
    # assert sorting_date_list(operations_list_five) ==


def test_required_date_format():
    assert required_date_format('2019-12-08T22:46:21.935582') == "08.12.2019"



def test_required_card_format():
    assert required_card_format("Счет 90424923579946435907") == "Счет **5907"
    assert required_card_format("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"
    assert required_card_format(None) == "VVVVVVVV"
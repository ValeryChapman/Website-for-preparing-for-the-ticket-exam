import json
import requests


def service_on(url: str) -> bool:
    try:
        requests.head(url)
        return True
    except:
        return False


def is_dict(data: dict) -> bool:
    return isinstance(data, dict)


def is_list(data: list) -> bool:
    try:
        if isinstance(json.loads(str(data)), list):
            return True
        else:
            return False
    except:
        return False


def is_none(value) -> int:
    if not value:
        return 0
    else:
        return value


def is_integer(num: int) -> bool:
    return str(num).isdigit()


def is_digits(data: list) -> bool:
    if is_list(data):
        return all(map(lambda x: str(x).isdigit(), data))
    else:
        return False


def str_to_bool(string: str) -> bool:
    if isinstance(string, bool):
        return string

    return string.lower() in ("yes", "true", "1")


def check_num_argument(data: dict, key='') -> bool:
    return bool(is_dict(data) and is_integer(data.get(key)))


def check_list_argument(data: dict, key='') -> bool:
    return bool(is_dict(data) and is_list(data.get(key)))


def check_digits_in_list(data: dict, key='') -> bool:
    return bool(is_dict(data) and is_digits(data.get(key)))


def check_key_and_argument(data: dict, key='') -> bool:
    return bool(is_dict(data) and data.get(key))


def check_key(data: dict, key='') -> bool:
    return bool(is_dict(data) and [' ' if data.get(key) is not None else False][0])
def JsonKeyDeletor(json_data: dict, needed_data: list) -> None:
    """
    Delete all keys that are not in needed_data
    :param json_data: JSON data
    :param needed_data: List of needed data
    :return: None
    """
    if isinstance(json_data, dict):
        for k, v in list(json_data.items()):
            if k not in needed_data:
                json_data.pop(k, None)
            else:
                JsonKeyDeletor(v, needed_data)
    elif isinstance(json_data, list):
        for item in json_data:
            JsonKeyDeletor(item, needed_data)
    else:
        return None
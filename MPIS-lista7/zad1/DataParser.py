import os
import json


def parse_data(dir_name: str) -> dict:
    parsed_data = dict()
    for filename in os.listdir(os.path.join("logs", dir_name)):
        parsed_n_data = dict()
        with open(os.path.join("logs", dir_name, filename), "r") as file:
            data = json.loads(file.read())
            for k_try in data:
                for key, value in list(k_try.items()):
                    if parsed_n_data.get(key) is None:
                        parsed_n_data[key] = 0
                    parsed_n_data[key] += value
        for key, value in list(parsed_n_data.items()):
            parsed_n_data[key] = value / 50

        parsed_data[filename.split(".")[0]] = parsed_n_data
    print(parsed_data)
    return parsed_data

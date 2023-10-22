import json

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    


def avgAgeCountry(data, country_name, transform_func):
    age_sum = 0
    count = 0

    for person in data:
        if person["country"] == country_name:
            age_sum += transform_func(person["age"])
            count += 1

    if count == 0:
        return None

    avg_age = age_sum / count
    return avg_age

def most_common_name_by_country(country_name, data, transform_func):
    names = {}

    for person in data:
        if person["country"] == country_name:
            name = transform_func(person["name"])
            if name in names:
                names[name] += 1
            else:
                names[name] = 1

    if len(names) == 0:
        return None

    most_common_name = max(names, key=names.get)
    return most_common_name

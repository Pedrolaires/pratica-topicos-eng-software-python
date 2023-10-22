import os
import unittest
from dataProcessor import read_json_file, avgAgeCountry, most_common_name_by_country, age_pyramid

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1500)
        self.assertEqual(data[0]['name'], 'Zachary Green')
        self.assertEqual(data[1]['age'], 30)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("./data/invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("./data/invalid.json")

## Novos testes

    def test_read_empty_json(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)
        self.assertIsNotNone(data, "O arquivo não pode ser vazio")


    def test_country_and_age_not_empty_or_null(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)


        for person in data:
            self.assertIsNotNone(person["country"], f"Country is None for {person}")
            self.assertNotEqual(person["country"], "", f"Country is empty for {person}")
            self.assertIsNotNone(person["age"], f"Age is None for {person}")

    def test_avg_age_by_country(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)
        avg_age = avgAgeCountry(data, "BR", lambda x: x)

        self.assertEqual(avg_age, 38.30769230769231, "Média brasileira de idade deve ser de 38.30769230769231")
    
    def test_avg_age_by_country_missing_age(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users_missing_data.json")
        data = read_json_file(file_path)
        avg_age = avgAgeCountry(data, "UK", lambda x: x)

        self.assertEqual(avg_age, 28.5)

    def test_avg_age_nonexistent_country(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)

        avg = avgAgeCountry(data, "ZZ", lambda x: x)
        self.assertIsNone(avg)

    def test_avg_age_in_months_by_country(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)

        avg = avgAgeCountry(data, "UK", lambda x: x*12)
        self.assertEqual(avg, 465.08670520231215, "A média de meses de idade dos britânicos deve ser de 465.08670520231215")

    def test_avg_age_in_months_by_country(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)

        avg = avgAgeCountry(data, "UK", lambda x: x*12)
        # Não achei o assert equals com delta no python :/
        self.assertEqual(avg, 465.08670520231215, "A média de meses de idade dos britânicos deve ser de 465.08670520231215")

    def test_common_name_in_uk(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)
        name = most_common_name_by_country("UK", data, lambda x: x.split(" ")[0])
        self.assertEqual(name, "Maria", "O nome mais comum no Reino Unido é Maria")


    def test_common_last_name_in_uk(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)
        last_name = most_common_name_by_country("UK", data, lambda x: x.split(" ")[1])
        self.assertEqual(last_name, "Johnson", "O sobrenome mais comum no Reino Unido é Johnson")


    def test_age_pyramid(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users.json")
        data = read_json_file(file_path)
        pyramid = age_pyramid("UK", data, lambda x: x)
        self.assertEqual(pyramid, [0, 15, 44, 34, 40, 40, 0, 0, 0, 0, 0], "A pirâmide etária do Reino Unido deve ser [0, 15, 44, 34, 40, 40, 0, 0, 0, 0]")

    def test_age_pyramid_missing_age_json(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "./data/users_missing_data.json")
        data = read_json_file(file_path)
        pyramid = age_pyramid("UK", data, lambda x: x)
        self.assertEqual(pyramid, [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0])









if __name__ == '__main__':
    unittest.main()
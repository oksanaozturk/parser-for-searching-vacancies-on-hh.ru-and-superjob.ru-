from abc import ABC, abstractmethod
import json


class JSONStorage(ABC):
    """Класс для координации работы с json-файлом полученных вакансий"""

    @abstractmethod
    def add_vacancies(self, vacancies):
        """Метод, обеспечивающий запись оакансий в json-файл"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Метод, обеспечивающий получение оакансий из json-файла"""
        pass

    @abstractmethod
    def selected_vacancies(self, criterion):
        """Метод, обеспечивающий сортировку вакансий в json-файле"""
        pass

    @abstractmethod
    def delete_vacancies(self, criterion):
        """Метод, обеспечивающий удаление оакансий из json-файл"""
        pass


class JSONStorageVacancy(JSONStorage):
    """Класс для координации работы с json-файлом полученных вакансий"""

    def __init__(self, file_path: str) -> None:
        """Инициализация объекта класса JSONStorageVacancy"""
        self.file_path = file_path

    def add_vacancies(self, vacancies: list[dict]):
        """Метод, обеспечивающий запись оакансий в json-файл"""

        with open(self.file_path, "w", encoding='UTF-8') as file:
            json.dump(vacancies, file, indent=2, ensure_ascii=False)

    def get_vacancies(self):
        """Метод, обеспечивающий получение оакансий из json-файла"""
        with open(self.file_path, "r", encoding='UTF-8') as file:
            vacancies = json.load(file)
            return vacancies

    def selected_vacancies(self, criterion):
        """Метод, обеспечивающий сортировку вакансий в json-файле по заданному критерию"""

        result = []
        with open(self.file_path, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            for vacancy in vacancies:
                for value in vacancy.values():
                    if criterion in str(value):
                        result.append(vacancy)

        with open(self.file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(result, json_file, ensure_ascii=False, indent=2)
            json_file.write('\n')

        return result

    def delete_vacancies(self, criterion):
        """Метод, обеспечивающий удаление оакансий из json-файл по заданному критерию"""
        with open(self.file_path, "r", encoding='UTF-8') as file:
            data = json.load(file)
        for vacancy in data:
            if vacancy != criterion:
                data.remove(vacancy)

        with open(self.file_path, "w", encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def len_vacancies(self) -> int:
        """Подсчет количества вакансий в json-файле"""
        with open(self.file_path, "r", encoding='UTF-8') as file:
            vacancies = json.load(file)

        vacancies_count = len(vacancies)
        return vacancies_count

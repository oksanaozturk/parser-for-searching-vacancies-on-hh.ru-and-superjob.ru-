from src.job_board import JobBoard
import requests


class HeadHunter(JobBoard):
    """Класс для получения списка вакансий по API с сайта HeadHunter.ru"""

    url = "https://api.hh.ru/vacancies"

    def __init__(self) -> None:
        """
        Инициализирует объект класса к API HeadHunter

        """
        self.url = HeadHunter.url

    def get_vacancies(self, keyword: str):
        """
        Метод, осуществляющий подключение  и запрос, по АПИ к сайту HeadHunter.ru
        params (dict): Параметры запроса к API HeadHunter.
                        per_page: количество вакансий на странице.
                        page: номер страницы результатов.
                        text: keyword - ключевое слово для поиска вакансии.
                        area: код региона
        headers (dict): Заголовки запроса к API HeadHunter.
        Итоговые значения записываются в json-файл.
        """
        params = {
            "per_page": 100,  # количество вакансий на странице.
            "page": None,  # номер страницы результатов.
            "text": keyword,  # строка поиска по названию вакансии.
            "area": 113,  # Код региона (113 - Россия)
        }
        headers = {
            "HH-User-Agent": "PyCharm_Parsing"
        }
        response = requests.get(self.url, params=params, headers=headers)
        if response.ok:
            data = response.json()
            vacancies_list = []
            try:
                for vacancy in data["items"]:
                    vacancy_info = {
                        "employer": vacancy["employer"].get("name"),
                        "title": vacancy.get("name"),
                        "location": vacancy["area"].get("name"),
                        "url": vacancy.get("apply_alternate_url"),
                        "salary_from": vacancy["salary"].get("from") if vacancy["salary"] else None,
                        "salary_to": vacancy["salary"].get("to") if vacancy["salary"] else None,
                        "description": vacancy.get("snippet", {}).get("requirement")
                    }
                    if vacancy_info["salary_from"] is None:
                        vacancy_info["salary_from"] = 0

                    if vacancy_info["salary_to"] is None:
                        vacancy_info["salary_to"] = 0

                    if vacancy_info["salary_to"] == 0:
                        vacancy_info["salary_to"] = vacancy_info["salary_from"]

                    vacancies_list.append(vacancy_info)
                # with open(f"{params['text']}_hh_ru.json", "w", encoding='UTF-8') as file:
                #     json.dump(vacancies_list, file, indent=2, ensure_ascii=False)
                return vacancies_list
            except (ValueError, KeyError):
                print("Запрос не удался, вакансии не получены, ошибки ключа или значения")
        else:
            print("Запрос не выполнен")
            quit()

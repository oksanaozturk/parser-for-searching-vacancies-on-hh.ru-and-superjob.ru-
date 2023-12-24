from src.job_board import JobBoard
import os
import requests


class SuperJob(JobBoard):
    """Класс для получения списка вакансий по API с сайта  Superjob.ru"""

    url = "https://api.superjob.ru/2.0/vacancies/"
    API_KEY: str = os.getenv('API_FOR__SUPERJOB')

    def __init__(self):
        """
        Инициализирует объект класса к API Superjob.ru

        """
        self.url = SuperJob.url
        self.API_KEY = SuperJob.API_KEY

    def get_vacancies(self, keyword: str):
        """
        Метод, осуществляющий подключение  и запрос, по АПИ к сайту Superjob.ru
        params (dict): Параметры запроса к API HeadHunter.
                        count: количество вакансий на странице.
                        page: номер страницы результатов.
                        text: keyword - ключевое слово для поиска вакансии.
                        area: код региона
        headers (dict): Заголовки запроса к API HeadHunter.
        Итоговые значения записываются в json-файл.
        """
        params = {
            "count": 100,  # количество вакансий на странице.
            "page": None,  # номер страницы результатов.
            "keyword": keyword,  # строка поиска по названию вакансии.
            "c": 1,  # Код страны (1 - Россия)
        }
        headers = {
            "HH-User-Agent": "parser-for-searching-vacancies-on-superjob.ru",
            "X-Api-App-Id": self.API_KEY

        }
        response = requests.get(self.url, params=params, headers=headers)

        if response.ok:
            data = response.json()
            vacancies_list = []
            try:
                for vacancy in data["objects"]:
                    vacancy_info = {
                        "employer": vacancy.get("firm_name"),
                        "title": vacancy.get("profession"),
                        "location": vacancy.get("client", {}).get("town", {}).get("title"),
                        "url": vacancy.get("link"),
                        "salary_from": vacancy.get("payment_from") if vacancy["payment_from"] else None,
                        "salary_to": vacancy.get("payment_to") if vacancy["payment_to"] else None,
                        "description ": vacancy.get("candidat")
                    }
                    if vacancy_info["salary_from"] is None:
                        vacancy_info["salary_from"] = 0

                    if vacancy_info["salary_to"] is None:
                        vacancy_info["salary_to"] = 0

                    if vacancy_info["salary_to"] == 0:
                        vacancy_info["salary_to"] = vacancy_info["salary_from"]
                    vacancies_list.append(vacancy_info)
                # with open(f"{params['keyword']}_superjob_ru.json", "w", encoding='UTF-8') as file:
                #     json.dump(vacancies_list, file, indent=2, ensure_ascii=False)
                return vacancies_list
            except (ValueError, KeyError):
                print("Запрос не удался, вакансии не получены, ошибки ключа или значения")
        else:
            print("Запрос не выполнен")
            quit()

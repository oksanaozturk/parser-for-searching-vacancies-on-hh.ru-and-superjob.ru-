from abc import ABC, abstractmethod


class JobBoard(ABC):
    """Класс для получения списка вакансий по API с сайта """
    @abstractmethod
    def get_vacancies(self, keyword: str):
        """
        Метод, осуществляющий подключение и запрос к сайту, по АПИ,
        далее форматирующий полученные данные и записывающий их в list[dict]
        """
        pass

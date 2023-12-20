from dataclasses import dataclass


@dataclass
class Vacancy:
    """
    Класс для работы с вакансиями.

    employer (str): Название работодателя.
    title (str): Название вакансии.
    location (str): Регион или локация вакансии.
    url (str): Ссылка на вакансию.
    salary_from (float): Зарплата от.
    salary_to (float): Зарплата до.
    description (str): Требования и описание вакансии.
    """
    __slots__ = ("employer", "title", "location", "url", "salary_from", "salary_to",
                 "description")

    employer: str
    title: str
    location: str
    url: str
    salary_from: float
    salary_to: float
    description: str

    def __repr__(self):
        return f"""
        Работодатель:{self.employer}
        Вакансия: {self.title}
        Город: {self.location}
        Ссылка {self.url}
        Описание/требования {self.description}
        Зарплата от {self.salary_from} до {self.salary_to}"""

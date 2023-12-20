from src.hh import HeadHunter
from src.super_job import SuperJob
from src.json_storage import JSONStorageVacancy
from src.vacancy import Vacancy


def choose_platform():
    """Функция выбора платформы для парсинга"""

    # Создаем объект Класса JSONStorageVacancy
    storage = JSONStorageVacancy("vacancies.json")

    while True:
        platform_selection = input("\nДавайте определимся, где будем искать вакансии.\n"
                                   "1 - 'HeadHunter', 2 - 'SuperJob', 3 - 'На обоих сайтах'\n"
                                   "\nВведите выбранный Вами вариант: ")

        if platform_selection == '1':
            print("\nДля поиска вакансий Вы выбрали платформу 'HeadHunter'.\n")
            keyword = input("Введите название вакансии для поиска: ")
            print(f"\nДелаем запрос, это может занять некоторое время. Идет сбор информации.\n")
            hh = HeadHunter()
            hh_vacancies = hh.get_vacancies(keyword)
            json_vacancies_hh = storage.add_vacancies(hh_vacancies)
            if storage.len_vacancies() == 0:
                print("К сожалению по данному запросу вакансий не найдено.\n"
                      "Попробуйте еще раз!\n")
                continue
            return json_vacancies_hh
        elif platform_selection == '2':
            print("\nДля поиска вакансий Вы выбрали платформу 'SuperJob'.\n")
            keyword = input("Введите название вакансии для поиска: ")
            print(f"\nДелаем запрос, это может занять некоторое время. Идет сбор информации.\n")
            sj = SuperJob()
            sj_vacancies = sj.get_vacancies(keyword)
            json_vacancies_sj = storage.add_vacancies(sj_vacancies)
            return json_vacancies_sj
        elif platform_selection == '3':
            print("\nДля поиска вакансий Вы выбрали обе платформы.\n")
            keyword = input("Введите название вакансии для поиска: ")
            print(f"\nДелаем запрос, это может занять некоторое время. Идет сбор информации.\n")
            hh = HeadHunter()
            sj = SuperJob()
            hh_vacancies = hh.get_vacancies(keyword)
            sj_vacancies = sj.get_vacancies(keyword)
            all_vacancies = hh_vacancies + sj_vacancies
            json_vacancies_all = storage.add_vacancies(all_vacancies)
            if storage.len_vacancies() == 0:
                print("К сожалению по данному запросу вакансий не найдено.\n"
                      "Попробуйте еще раз!\n")
                continue
            return json_vacancies_all
        else:
            print("К сожалению, Вы указали некорректное значение.\n"
                  "Попробуйте еще раз!\n")


def sort_vacancies() -> list[dict]:
    """Функцмия для сортировки полученных вакансий по зарпоате (от большего к меньшему)"""

    storage = JSONStorageVacancy("vacancies.json")

    vacancies = storage.get_vacancies()
    sorted_vacancies = sorted(vacancies, key=lambda vacancy: vacancy["salary_from"], reverse=True)
    storage.add_vacancies(sorted_vacancies)
    return sorted_vacancies


def top_vacancies():
    """Выводит top-n вакансий по зарплате"""

    while True:
        user_input = input("Хотите получить топ-N вакансий по зарплате? Да/Нет ")
        if user_input.title() == 'Да':
            storage = JSONStorageVacancy("vacancies.json")
            vacancies = storage.get_vacancies()
            sorted_vacancies = sorted(vacancies, key=lambda vacancy: vacancy["salary_from"], reverse=True)
            print("\nВведите количество вакансий для топ-N по зарплате (Например: 5) ")
            try:
                user_num = int(input())
                if 1 <= user_num <= storage.len_vacancies():
                    print(f"Отлично! Вот топ - {user_num} вакансий по зарплате от большего к меньшему: ")
                    # vacancies = [Vacancy(**vacancy) for vacancy in sorted_vacancies[:user_num]]
                    top_sorted_vacancies = sorted_vacancies[:user_num]
                    for vacancy in top_sorted_vacancies:
                        vac = Vacancy(vacancy['employer'], vacancy['title'], vacancy['location'], vacancy['url'],
                                      vacancy['salary_from'], vacancy['salary_to'], vacancy.get('description'))
                        print(repr(vac))
                    break
                else:
                    print("Некорректное значение")
            except ValueError:
                print("Некорректный ввод, введите целое число")

        elif user_input.title() == 'Нет':
            storage = JSONStorageVacancy("vacancies.json")
            vacancies = storage.get_vacancies()

            print("\nВведите количество вакансий для просмотра (Например: 5) ")
            try:
                vac_num = int(input())
                if 1 <= vac_num <= storage.len_vacancies():
                    print(f"Отлично! Вот {vac_num} запрашиваемых Вами вакансий: ")
                    # vacancies = [Vacancy(**vacancy) for vacancy in sorted_vacancies[:user_num]]
                    vacancies_1 = vacancies[:vac_num]
                    for vacancy in vacancies_1:
                        vac = Vacancy(vacancy['employer'], vacancy['title'], vacancy['location'], vacancy['url'],
                                      vacancy['salary_from'], vacancy['salary_to'], vacancy.get('description'))
                        print(repr(vac))
                    break
                else:
                    print("Некорректное значение")
            except ValueError:
                print("Некорректный ввод, введите целое число")

        else:
            print("Некорректный ввод, повторите попытку")

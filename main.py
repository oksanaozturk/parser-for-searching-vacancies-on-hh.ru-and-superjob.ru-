from utils.interaction_functions import choose_platform, top_vacancies
from src.json_storage import JSONStorageVacancy


def main():
    """Функция для взаимодействия с пользователем"""

    storage = JSONStorageVacancy("vacancies.json")
    while True:
        print('Привет! Данная программа производит поиск вакансий на платформах hh.ru и superjob.ru')
        choose_platform()
        print(f'По вашему запросу найдено {storage.len_vacancies()} вакансий')
        top_vacancies()
        input_user = input("\nВы хотите продолжить поиск интересующих Вас вакансий? Да/Нет: ")
        if input_user.lower() == 'да':
            continue
        elif input_user.lower() == 'нет':
            print("\nРады, что Вы воспользовались нашим сервисом поиска вакансий! До встречи!")
            break
        else:
            print("Вы ввели некорректный ответ. Рады, что Вы воспользовались нашим сервисом поиска вакансий!")


if __name__ == "__main__":
    main()

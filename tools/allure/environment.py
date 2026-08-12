from config import settings


def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # Здесь мы формируем список из ключей и значений наших настроек.
    # Метод settings.model_dump() вернет нам настройки в формате словаря, что позволит удобно
    # итерироваться по нему и создавать строку для environment.properties
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл
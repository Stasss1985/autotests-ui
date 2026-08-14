from config import settings
import platform
import sys


def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)
    # Здесь мы формируем список из ключей и значений наших настроек.
    # Метод settings.model_dump() вернет нам настройки в формате словаря, что позволит удобно
    # итерироваться по нему и создавать строку для environment.properties

    my_platform = f'os_info={platform.system()}, {platform.release()}'

    my_system = f'python_version={sys.version}'

    # Собираем все элементы в единую строку с переносами
    all_environment = properties + '\n' + my_platform + '\n' + my_system

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(all_environment)  # Записываем переменные в файл

import allure
from playwright.sync_api import Playwright, Page

from config import settings, Browser  # Импортируем enum Browser
from tools.playwright.mocks import mock_static_resources


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,  # Передаем браузер в качестве аргумента
        storage_state: str | None = None
) -> Page:
    # Динамически получаем нужный браузер
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)  # Отключаем загрузку статических ресурсов

    yield page

    # 1. Останавливаем трейсинг и прикрепляем trace — тут всё корректно,
    #    zip финализируется при tracing.stop()
    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    allure.attach.file(
        settings.tracing_dir.joinpath(f'{test_name}.zip'),
        name='trace',
        extension='zip'
    )

    # 2. Сохраняем путь к видео ДО закрытия контекста —
    #    после close() объект page/видео уже недоступен
    video_path = page.video.path()

    # 3. Закрываем контекст — только в этот момент Playwright
    #    дописывает webm-файл до конца (финализирует его)
    context.close()

    # 4. Теперь файл готов — прикрепляем его к отчёту
    allure.attach.file(
        video_path,
        name='video',
        attachment_type=allure.attachment_type.WEBM
    )

    # 5. Закрываем браузер в самом конце
    browser.close()

# def initialize_playwright_page(
#         playwright: Playwright,
#         test_name: str,
#         browser_type: Browser,  # Передаем браузер в качестве аргумента
#         storage_state: str | None = None
# ) -> Page:
#     # Динамически получаем нужный браузер
#     browser = playwright[browser_type].launch(headless=settings.headless)
#     context = browser.new_context(
#         base_url=settings.get_base_url(),
#         storage_state=storage_state,
#         record_video_dir=settings.videos_dir
#     )
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#     mock_static_resources(page)  # Отключаем загрузку статических ресурсов
#
#     yield page
#
#     context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
#     browser.close()
#
#     allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
#     allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

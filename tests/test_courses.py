import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible("username")
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.empty_view.check_visible(
        title="There is no results",
        description="Results from the load test pipeline will be displayed here",
    )

@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # Проверка начального состояния компонентов
    create_course_page.toolbar.check_visible()
    create_course_page.create_course_form.check_visible(
        title="", estimated_time="", description="", max_score="0", min_score="0"
    )
    create_course_page.exercises_toolbar.check_visible()
    create_course_page.exercises_empty_view.check_visible(
        title="There is no exercises", description="Click on \"Create exercise\" button to create new exercise")

    # Загрузка изображения (предполагается, что метод upload_preview_image существует)
    create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # Заполнение формы курса
    create_course_page.create_course_form.fill(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
    )

    # Проверка, что кнопка создания стала активной, и нажатие
    create_course_page.toolbar.check_visible()
    create_course_page.toolbar.click_create_course_button()

    # Проверка, что курс появился в списке
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10",
    )
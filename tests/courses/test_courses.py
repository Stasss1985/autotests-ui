import pytest
import allure

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.COURSES)  # Добавили feature
@allure.story(AllureStory.COURSES)  # Добавили story
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
    @allure.title("Проверка пустого листа курса")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible('username')
        courses_list_page.sidebar.check_visible()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Тест создания курса")
    @allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
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

    @allure.title("Тест редактирования курса")
    @allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_form.check_visible(
            title="", estimated_time="", description="", max_score="0", min_score="0"
        )

        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )

        create_course_page.toolbar.check_visible()
        create_course_page.toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            estimated_time="2 weeks",
            max_score="100",
            min_score="10",
        )

        courses_list_page.course_view.menu.menu_button.click(index=0)
        courses_list_page.course_view.menu.edit_menu_item.click()

        create_course_page.create_course_form.fill(
            title="Edited Course",
            estimated_time="5 weeks",
            description="Updated description",
            max_score="90",
            min_score="10",
        )

        # Проверка, что кнопка создания стала активной, и нажатие
        create_course_page.toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title="Edited Course",
            estimated_time="5 weeks",
            max_score="90",
            min_score="10",
        )

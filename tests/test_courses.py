import time

from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
    # Проверить наличие и текст заголовка "Courses"
    courses_list_page.check_visible_courses_title()
    # Кнопка создания курса
    courses_list_page.check_visible_create_course_button()
    # Проверить наличие и текст блока "There is no results"
    # Проверить наличие и видимость иконки пустого блока
    # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(title='', estimated_time='',
                                                        description='', max_score='0', min_score='0')
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title="Playwright", estimated_time="2 weeks", description="Playwright",
        max_score="100", min_score="10")
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0, title="Playwright", estimated_time="2 weeks", max_score="100", min_score="10"
    )
    time.sleep(3)

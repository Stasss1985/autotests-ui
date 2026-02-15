from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверить наличие и текст заголовка "Courses"
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Проверить наличие и текст блока "There is no results"
    no_results_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_results_text).to_be_visible()
    expect(no_results_text).to_have_text('There is no results')

    # Проверить наличие и видимость иконки пустого блока
    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    # Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    results_from_the_load_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_from_the_load_block).to_be_visible()
    expect(results_from_the_load_block).to_have_text('Results from the load test pipeline will be displayed here')

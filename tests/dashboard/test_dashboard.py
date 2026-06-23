import allure
import pytest

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic  # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature  # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory  # Импортируем enum AllureStory
from allure_commons.types import Severity


@pytest.mark.dashboard
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.DASHBOARD)  # Добавили feature
@allure.story(AllureStory.DASHBOARD)  # Добавили story
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title("Тест отображение карточек на странице dashboard")
    @allure.tag(AllureTag.DASHBOARD, AllureTag.REGRESSION)
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
        dashboard_page_with_state.navbar.check_visible("username")
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.scores_chart.check_visible("Scores")
        dashboard_page_with_state.courses_chart.check_visible("Courses")
        dashboard_page_with_state.students_chart.check_visible("Students")
        dashboard_page_with_state.activities_chart.check_visible("Activities")

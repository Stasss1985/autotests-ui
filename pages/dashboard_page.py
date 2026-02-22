from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title_name = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_dashboard_title_name(self):
        # После перехода ищем заголовок "Dashboard" и сравниваем текст заголовка
        expect(self.dashboard_title_name).to_be_visible()
        expect(self.dashboard_title_name).to_have_text('Dashboard')

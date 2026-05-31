from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.toolbar = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible(self) -> None:
        expect(self.toolbar).to_be_visible()
        expect(self.toolbar).to_have_text('Dashboard')
        
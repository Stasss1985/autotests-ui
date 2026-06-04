from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.toolbar = Text(page, 'dashboard-toolbar-title-text', 'Dashboard title text')

    def check_visible(self) -> None:
        self.toolbar.check_visible()
        self.toolbar.check_have_text('Dashboard')

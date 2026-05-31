from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Create course')

    def click_create_course_button(self) -> None:
        self.create_course_button.click()

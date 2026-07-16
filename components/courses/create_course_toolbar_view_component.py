from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
import allure

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title = Text(page,'create-course-toolbar-title-text', 'Create course toolbar title')
        self.create_course_button = Button(page,'create-course-toolbar-create-course-button', 'Create course toolbar button')
    @allure.step('Check visible toolbar "Create course" ')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Create course')

    def click_create_course_button(self) -> None:
        self.create_course_button.click()

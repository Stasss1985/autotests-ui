from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_exercise_button = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

    def check_visible(self) -> None:
        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self) -> None:
        self.create_exercise_button.click()
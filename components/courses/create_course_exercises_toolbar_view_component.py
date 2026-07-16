from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
import allure

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.create_exercise_button = Button(page,'create-course-exercises-box-toolbar-create-exercise-button', 'Create exercise button')

    @allure.step('Check visible create exercise button')
    def check_visible(self) -> None:
        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self) -> None:
        self.create_exercise_button.click()
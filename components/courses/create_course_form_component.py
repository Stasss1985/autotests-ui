from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea
import allure


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_input = Input(page, 'create-course-form-title-input', 'Title input')
        self.estimated_time_input = Input(page,'create-course-form-estimated-time-input', 'Estimated time input')
        self.description_input = Textarea(page,'create-course-form-description-input', 'Description')
        self.max_score_input = Input(page,'create-course-form-max-score-input', 'Max score input')
        self.min_score_input = Input(page,'create-course-form-min-score-input', 'Min score input')

    @allure.step('Fill create course form with title "{title}", estimated time "{estimated_time}", description "{description}", max_score "{max_score}", min_score "{min_score}"')
    def fill(self, title: str, estimated_time: str, description: str,
             max_score: str, min_score: str) -> None:
        self.title_input.fill(title)
        self.estimated_time_input.fill(estimated_time)
        self.description_input.fill(description)
        self.max_score_input.fill(max_score)
        self.min_score_input.fill(min_score)

    @allure.step('Check visible created course form with title "{title}", estimated time "{estimated_time}", description "{description}", max_score "{max_score}", min_score "{min_score}"')
    def check_visible(self, title: str, estimated_time: str, description: str,
                      max_score: str, min_score: str) -> None:
        self.title_input.check_visible()
        self.estimated_time_input.check_visible()
        self.description_input.check_visible()
        self.max_score_input.check_visible()
        self.min_score_input.check_visible()
        self.title_input.check_have_value(title)
        self.estimated_time_input.check_have_value(estimated_time)
        self.description_input.check_have_value(description)
        self.max_score_input.check_have_value(max_score)
        self.min_score_input.check_have_value(min_score)
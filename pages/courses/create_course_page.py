from playwright.sync_api import Page
from components.navigation.navbar_component import NavbarComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent   # если есть
from pages.base_page import BasePage

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = NavbarComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.create_course_form = CreateCourseFormComponent(page)
        self.toolbar = CreateCourseToolbarViewComponent(page)
        self.exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.exercise_form = CreateCourseExerciseFormComponent(page)  # если используется
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
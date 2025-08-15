import pytest
from playwright.sync_api import expect, Page

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    empty_view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_view_icon).to_be_visible()

    empty_view_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_view_title).to_be_visible()
    expect(empty_view_title).to_have_text('There is no results')

    empty_view_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_view_description).to_be_visible()
    expect(empty_view_description).to_have_text('Results from the load test pipeline will be displayed here')


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    
    # Проверка: отображается заголовок "Create course"
    create_course_page.check_visible_create_course_title()
    
    # Проверка: кнопка создания курса недоступна
    create_course_page.check_disabled_create_course_button()
    
    # Проверка: отображается пустой блок предпросмотра изображения
    create_course_page.check_visible_image_preview_empty_view()
    
    # Проверка: блок загрузки изображения в состоянии "изображение не выбрано"
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    
    # Проверка: форма создания курса отображается с дефолтными значениями
    create_course_page.check_visible_create_course_form(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0"
    )
    
    # Проверка: отображается заголовок блока "Exercises"
    create_course_page.check_visible_exercises_title()
    
    # Проверка: отображается кнопка создания задания
    create_course_page.check_visible_create_exercise_button()
    
    # Проверка: отображается пустой список заданий
    create_course_page.check_visible_exercises_empty_view()
    
    # Проверка: блок загрузки изображения в состоянии "изображение загружено"
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    
    # Заполнение формы создания курса
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    
    create_course_page.click_create_course_button()


    # После создания курса произойдет редирект на страницу со списком курсов
    
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    
    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
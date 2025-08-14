import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    
    registration_page.fill_registration_form_email_input('user.name@gmail.com')
    registration_page.fill_registration_form_username_input('username')
    registration_page.fill_registration_form_password_input('password')
    registration_page.click_registration_form_button()
    
    dashboard_page.check_visible_dashboard_title()
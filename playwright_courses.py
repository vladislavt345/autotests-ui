from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.wait_for_timeout(2000)

    email_input = page.locator('[data-testid="registration-form-email-input"] input')
    email_input.fill("user.name@gmail.com")
    
    username_input = page.locator('[data-testid="registration-form-username-input"] input')
    username_input.fill("username")
    
    password_input = page.locator('[data-testid="registration-form-password-input"] input')
    password_input.fill("password")

    page.wait_for_timeout(2000)
    registration_button = page.locator('[data-testid="registration-page-registration-button"]')
    registration_button.click()
    page.wait_for_timeout(2000)

    context.storage_state(path="browser-state.json")

    context.close()
    browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    page.wait_for_timeout(2000)

    assert page.inner_text("h6:has-text('Courses')") == "Courses"
    assert page.inner_text("text=There is no results") == "There is no results"

    context.close()
    browser.close()
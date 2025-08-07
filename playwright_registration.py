from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    

    email_input = page.locator('[data-testid="registration-form-email-input"] input')
    email_input.fill("user.name@gmail.com")
    
    username_input = page.locator('[data-testid="registration-form-username-input"] input')
    username_input.fill("username")
    
    password_input = page.locator('[data-testid="registration-form-password-input"] input')
    password_input.fill("password")
    

    registration_button = page.locator('[data-testid="registration-page-registration-button"]')
    registration_button.click()
    

    dashboard_title = page.locator('h1, h2, h3, h4, h5, h6').filter(has_text="Dashboard")
    expect(dashboard_title).to_be_visible()
    

    if dashboard_title.is_visible():
        page.wait_for_timeout(5000)

    browser.close()
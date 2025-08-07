from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")


    registration_button = page.locator('[data-testid="registration-page-registration-button"]') 
    # "Registration"= disabled
    expect(registration_button).to_be_disabled()
    
    
    email_input = page.locator('[data-testid="registration-form-email-input"] input')
    email_input.fill("user.name@gmail.com")
    
    username_input = page.locator('[data-testid="registration-form-username-input"] input')
    username_input.fill("username")
    
    password_input = page.locator('[data-testid="registration-form-password-input"] input')
    password_input.fill("password")
    

    # "Registration"= enabled
    expect(registration_button).to_be_enabled()
    
    
    if registration_button.is_enabled():
        page.wait_for_timeout(5000)

    browser.close()
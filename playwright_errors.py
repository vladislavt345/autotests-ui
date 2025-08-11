from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа и ждём загрузки сети
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Ждём завершения сетевых запросов
    )

    # Явно ждём появления элемента по id
    title = page.locator('#authentication-ui-course-title-text')
    expect(title).to_be_visible()

    # Изменяем текст заголовка
    page.evaluate("""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
    """)

    # Чтобы увидеть результат, сделаем небольшую паузу
    page.wait_for_timeout(3000)

    browser.close()
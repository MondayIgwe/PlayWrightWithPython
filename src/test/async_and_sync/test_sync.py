from playwright.sync_api import sync_playwright

app_url = "https://www.saucedemo.com/"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.goto(app_url)

    # locate element
    docs_button = page.get_by_role('link', name="Docs")
    docs_button.click()
    print(f"Url: {page.url}")
    page.go_back()
    get_started = page.get_by_role('link', name="Get started")
    get_started.highlight()
    get_started.click()
    page.close()

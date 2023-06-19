from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright as playwright


class LifeCycle:

    def __init__(self):
        self.browser = playwright.chromium.launch(headless=False, slow_mo=5000)
        self.page = self.browser.new_page()
        self.page.goto("https://playwright.dev/python")
        self.page.screenshot(path="/src/dev/resource/test.png")

    def get_page(self):
        return self.page

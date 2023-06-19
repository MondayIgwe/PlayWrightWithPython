from playwright.sync_api import Page
from src.dev.commonConst.commons import app_url


def test_title(page: Page):
    page.goto(app_url)
    title = page.title()
    print(title.upper())
    print(title)
    assert title == "Swag Labs"
    assert page.inner_text("h4") == "Accepted usernames are:"


def test_validate_locators(page: Page):
    page.goto(app_url)
    assert page.inner_text("h4") == "Accepted usernames are:"

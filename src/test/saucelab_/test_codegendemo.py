from playwright.sync_api import Page, expect
from src.dev.commonConst.commons import app_url, inventory_page


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"password\"]").click()

    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).not_to_have_url(f"{app_url}{inventory_page}" + "negative test error")
    expect(page).to_have_url(f"{app_url}{inventory_page}", timeout=200)

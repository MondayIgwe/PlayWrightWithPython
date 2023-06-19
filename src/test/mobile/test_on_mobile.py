import pytest

from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 12"]}


def test_mobile(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("sauce")
    page.locator("[data-test=\"password\"]").press("ArrowLeft")
    page.locator("[data-test=\"password\"]").press("ArrowLeft")
    page.locator("[data-test=\"password\"]").press("ArrowLeft")
    page.locator("[data-test=\"password\"]").press("ArrowLeft")
    page.locator("[data-test=\"password\"]").press("ArrowLeft")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

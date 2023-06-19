from playwright.async_api import async_playwright, expect
import asyncio
from src.dev.commonConst.commons import app_url


async def main():
    screenshot = "C:\\Users\\migwe\\PycharmProjects\\pythonProject\\src\\dev\\resource\\screenshots\\test.png"
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False, slow_mo=5000)
        page = await browser.new_page()
        await page.goto(app_url)
        await expect(page).to_have_url()
        print(await page.title())
        await page.screenshot(path=screenshot)
        await page.close()
        await browser.close()


asyncio.run(main())

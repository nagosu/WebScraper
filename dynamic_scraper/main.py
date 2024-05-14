import time
from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

page.click("button.Aside_searchButton__Xhqq3.Aside_isNotMobileDevice__WuwWh")

page.click("input.SearchInput_SearchInput__gySrv")

page.fill("input.SearchInput_SearchInput__gySrv", "flutter")

page.press("input.SearchInput_SearchInput__gySrv", "Enter")

time.sleep(5)

page.click(
    "#search_tab_position",
)

for _ in range(3):
    page.evaluate("window.scrollBy(0, window.innerHeight)")

page_content = page.content()

print(page_content)

time.sleep(5)

browser.close()

p.stop()

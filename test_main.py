from playwright.sync_api import Page, expect

def test_Start(page: Page):
    page.goto("https://makashov-english.kwiga.com/courses/pre-intermediate-basic/test-formativ")
    page.get_by_role("button", name="Войти в учетную запись").click()
  
    page.wait_for_timeout(1000)  # 1 second pause
    page.wait_for_selector("input[name=\"email\"]")

    page.fill("input[name=\"email\"]", "XXXXXXX@gmail.com")
    page.get_by_role("button", name="Далее").click()
    page.wait_for_timeout(1000)  # 1 second pause
    page.fill("input[name=\"password\"]", "XXXXXXXXXX")
    page.wait_for_timeout(500)                 
    page.get_by_role("button", name="Далее").click()

    page.pause()  
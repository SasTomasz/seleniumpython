from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AwesomeHomePage:
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser
        self.result_headers_locator = (By.CSS_SELECTOR, "h1")
        self.wait = WebDriverWait(self.browser, 10)

    def go_to_home_page(self):
        self.browser.get("https://awesome-testing.blogspot.com/")

    def check_if_number_of_posts_are_correct(self, number_of_posts: int) -> bool:
        self.wait.until(EC.visibility_of_all_elements_located(self.result_headers_locator))
        result_headers = self.browser.find_elements(*self.result_headers_locator)
        return len(result_headers) == number_of_posts



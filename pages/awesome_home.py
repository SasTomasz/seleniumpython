from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AwesomeHomePage:
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    def go_to_home_page(self):
        self.browser.get("https://awesome-testing.blogspot.com/")



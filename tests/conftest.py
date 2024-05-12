import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_chrome_driver():
    service = Service(ChromeDriverManager().install())
    chrome_driver = Chrome(service=service)
    chrome_driver.set_window_size(1920, 1080)
    yield chrome_driver
    chrome_driver.quit()

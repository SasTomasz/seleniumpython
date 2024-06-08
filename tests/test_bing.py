import time

from assertpy import assert_that
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_bing():
    service = Service(ChromeDriverManager().install())
    chrome_driver = Chrome(service=service)

    chrome_driver.get("https://bing.com/")
    chrome_driver.set_window_size(1920, 1080)

    search_field = chrome_driver.find_element(By.CSS_SELECTOR, "#sb_form_q")

    # Searching 4testers in search engine
    search_field.send_keys("4testers", Keys.ENTER)

    # Check there is a proper header in results
    expected_header_title = "4_testers Automaty – Kurs Tester Automatyzujący & AI"
    headers_in_search_results = chrome_driver.find_elements(By.CSS_SELECTOR, "h2 a")
    time.sleep(2)

    titles = []
    for title in headers_in_search_results:
        time.sleep(2)
        titles.append(title.text)

    assert_that(titles).contains(expected_header_title)

    chrome_driver.quit()

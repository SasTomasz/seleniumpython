import time
from assertpy import assert_that

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_duckduckgo():
    service = Service(ChromeDriverManager().install())
    chrome_driver = Chrome(service=service)

    chrome_driver.get("https://duckduckgo.com/")
    chrome_driver.maximize_window()

    search_field = chrome_driver.find_element(By.ID, "searchbox_input")

    search_button = chrome_driver.find_element(By.CSS_SELECTOR, "button[aria-label=Search]")

    assert search_field.is_displayed()
    assert search_button.is_displayed()

    # Szukanie 4testers
    search_field.send_keys("4testers")
    search_button.click()

    # Sprawdzenie że pierwszy wynik ma poprawny tytuł
    expected_header_title = "4_testers Automaty - Kurs Tester Automatyzujący & AI"
    headers_in_search_results = chrome_driver.find_elements(By.CSS_SELECTOR, "[data-testid=result-title-a] span")

    titles = []
    for title in headers_in_search_results:
        time.sleep(2)
        titles.append(title.text)
    assert expected_header_title in titles

    # Zamknięcie przeglądarki
    chrome_driver.quit()


def test_searching_in_bing():
    service = Service(ChromeDriverManager().install())
    chrome_driver = Chrome(service=service)

    chrome_driver.get("https://bing.com/")
    chrome_driver.maximize_window()

    search_field = chrome_driver.find_element(By.CSS_SELECTOR, "#sb_form_q")

    search_button = chrome_driver.find_element(By.CSS_SELECTOR, "#search_icon")

    # Szukanie 4testers
    search_field.send_keys("4testers", Keys.ENTER)
    # search_button.click()

    # Sprawdzenie że pierwszy wynik ma poprawny tytuł
    expected_header_title = "4_testers Automaty – Kurs Tester Automatyzujący & AI"
    headers_in_search_results = chrome_driver.find_elements(By.CSS_SELECTOR, "h2 a")
    time.sleep(2)

    titles = []
    for title in headers_in_search_results:
        time.sleep(2)
        titles.append(title.text)

    assert_that(titles).contains(expected_header_title)

    # Zamknięcie przeglądarki
    chrome_driver.quit()


import pytest
import time

from assertpy import assert_that
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_post_count():
    service = Service(ChromeDriverManager().install())
    chrome_driver = Chrome(service=service)

    chrome_driver.get("https://awesome-testing.blogspot.com/")
    chrome_driver.set_window_size(1920, 1080)

    result_headers = chrome_driver.find_elements(By.CSS_SELECTOR, "h1")
    assert_that(len(result_headers)).is_equal_to(4)


def test_post_count_after_search():
    service = Service(ChromeDriverManager().install())
    chrome_driver = Chrome(service=service)

    chrome_driver.get("https://awesome-testing.blogspot.com/")
    chrome_driver.set_window_size(1920, 1080)

    search_button = chrome_driver.find_element(By.CSS_SELECTOR, "input.gsc-search-button")
    search_field = chrome_driver.find_element(By.CSS_SELECTOR, "input.gsc-input")

    search_field.send_keys("selenium")
    search_button.click()

    result_headers = chrome_driver.find_elements(By.CSS_SELECTOR, "h1")
    assert_that(len(result_headers)).is_equal_to(20)


def test_post_count_on_cypress_label():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = Chrome(executable_path=ChromeDriverManager().install())

    # Otwarcie strony

    # Inicjalizacja elementu z labelką

    # Kliknięcie na labelkę

    # Czekanie na stronę

    # Pobranie listy tytułów

    # Asercja że lista ma 1 element

    # Zamknięcie przeglądarki
    assert False

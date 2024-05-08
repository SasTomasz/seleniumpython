from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_searching_in_duckduckgo():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    chrome_driver = Chrome(service=service)

    # Otwarcie strony duckduckgo
    chrome_driver.get("https://duckduckgo.com/")
    chrome_driver.maximize_window()

    # Znalezienie paska wyszukiwania
    search_field = chrome_driver.find_element(By.ID, "searchbox_input")

    # Znalezienie guzika wyszukiwania (lupki)
    search_button = chrome_driver.find_element(By.CSS_SELECTOR, "button[aria-label=Search]")

    # Asercje że elementy są widoczne dla użytkownika
    assert search_field.is_displayed()
    assert search_button.is_displayed()

    # Szukanie Vistula University
    search_field.send_keys("Vistula University")
    search_button.click()

    # Sprawdzenie że pierwszy wynik ma tytuł 'Vistula University in Warsaw'
    expected_header_title = "Home - Vistula University"
    headers_in_search_results = chrome_driver.find_elements(By.CSS_SELECTOR, "[data-testid=mainline] li h2")
    first_header_in_search_result = headers_in_search_results[0]
    assert expected_header_title == first_header_in_search_result.text

    # Zamknięcie przeglądarki
    chrome_driver.quit()


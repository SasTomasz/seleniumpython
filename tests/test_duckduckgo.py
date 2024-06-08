from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_searching_in_duckduckgo(browser):
    wait = WebDriverWait(browser, 10)

    browser.get("https://duckduckgo.com/")

    search_field = browser.find_element(By.ID, "searchbox_input")

    search_button = browser.find_element(By.CSS_SELECTOR, "button[aria-label=Search]")

    assert search_field.is_displayed()
    assert search_button.is_displayed()

    # Searching 4testers in search engine
    search_field.send_keys("4testers")
    search_button.click()

    # Check there is a proper header in results
    expected_header_title = "4_testers Automaty - Kurs Tester Automatyzujący & AI"
    locator_headers_in_search_results = (By.CSS_SELECTOR, "[data-testid=result-title-a] span")
    wait.until(EC.visibility_of_all_elements_located(locator_headers_in_search_results))
    headers_in_search_results = browser.find_elements(*locator_headers_in_search_results)

    titles = []
    for title in headers_in_search_results:
        titles.append(title.text)
    assert expected_header_title in titles

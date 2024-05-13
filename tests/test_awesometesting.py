from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.awesome_home import AwesomeHomePage


def test_post_count(browser):
    awesome_home_page = AwesomeHomePage(browser)
    awesome_home_page.go_to_home_page()
    assert awesome_home_page.check_if_number_of_posts_are_correct(4)


def test_post_count_after_search(browser):
    wait = WebDriverWait(browser, 10)

    awesome_home_page = AwesomeHomePage(browser)

    awesome_home_page.go_to_home_page()

    search_button = browser.find_element(By.CSS_SELECTOR, "input.gsc-search-button")
    search_field = browser.find_element(By.CSS_SELECTOR, "input.gsc-input")

    search_field.send_keys("selenium")
    search_button.click()

    result_headers_locator = (By.CSS_SELECTOR, "h1")
    wait.until(EC.visibility_of_element_located(result_headers_locator))
    result_headers = browser.find_elements(*result_headers_locator)
    assert_that(len(result_headers)).is_equal_to(20)


def test_post_count_on_cypress_label(browser):
    # open page

    # find element with cypress label

    # click to element

    # wait for page

    # get titles

    # asser that list has at least one element
    assert False

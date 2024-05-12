from assertpy import assert_that
from selenium.webdriver.common.by import By


def test_post_count(get_chrome_driver):
    chrome_driver = get_chrome_driver

    chrome_driver.get("https://awesome-testing.blogspot.com/")

    result_headers = chrome_driver.find_elements(By.CSS_SELECTOR, "h1")
    assert_that(len(result_headers)).is_equal_to(4)


def test_post_count_after_search(get_chrome_driver):
    chrome_driver = get_chrome_driver

    chrome_driver.get("https://awesome-testing.blogspot.com/")

    search_button = chrome_driver.find_element(By.CSS_SELECTOR, "input.gsc-search-button")
    search_field = chrome_driver.find_element(By.CSS_SELECTOR, "input.gsc-input")

    search_field.send_keys("selenium")
    search_button.click()

    result_headers = chrome_driver.find_elements(By.CSS_SELECTOR, "h1")
    assert_that(len(result_headers)).is_equal_to(20)


def test_post_count_on_cypress_label(get_chrome_driver):
    browser = get_chrome_driver

    # open page

    # find element with cypress label

    # click to element

    # wait for page

    # get titles

    # asser that list has at least one element
    assert False

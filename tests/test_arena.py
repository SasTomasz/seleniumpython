from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Test - open chrome browser
def test_successful_login(browser):
    wait = WebDriverWait(browser, 10)

    administrator_email = "administrator@testarena.pl"

    browser.get('http://demo.testarena.pl/zaloguj')

    email_field = browser.find_element(By.CSS_SELECTOR, "#email")
    email_field.send_keys(administrator_email)
    password_field = browser.find_element(By.CSS_SELECTOR, "#password")
    password_field.send_keys("sumXQQ72$L")
    button_login = browser.find_element(By.CSS_SELECTOR, "#login")
    button_login.click()

    user_email_locator = (By.CSS_SELECTOR, ".user-info small")
    wait.until(EC.visibility_of_element_located(user_email_locator))
    user_email = browser.find_element(*user_email_locator)

    assert administrator_email == user_email.text

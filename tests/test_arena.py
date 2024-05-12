from selenium.webdriver.common.by import By


# Test - open chrome browser
def test_successful_login(get_chrome_driver):
    browser = get_chrome_driver

    administrator_email = "administrator@testarena.pl"

    browser.get('http://demo.testarena.pl/zaloguj')

    email_field = browser.find_element(By.CSS_SELECTOR, "#email")
    email_field.send_keys(administrator_email)
    password_field = browser.find_element(By.CSS_SELECTOR, "#password")
    password_field.send_keys("sumXQQ72$L")
    button_login = browser.find_element(By.CSS_SELECTOR, "#login")
    button_login.click()

    user_email = browser.find_element(By.CSS_SELECTOR, ".user-info small")

    assert administrator_email == user_email.text

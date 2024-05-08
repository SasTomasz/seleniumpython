from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Test - uruchomienie Chroma
def test_successful_login():
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)

    administrator_email = "administrator@testarena.pl"

    browser.get('http://demo.testarena.pl/zaloguj')
    browser.maximize_window()

    email_field = browser.find_element(By.CSS_SELECTOR, "#email")
    email_field.send_keys(administrator_email)
    password_field = browser.find_element(By.CSS_SELECTOR, "#password")
    password_field.send_keys("sumXQQ72$L")
    button_login = browser.find_element(By.CSS_SELECTOR, "#login")
    button_login.click()

    user_email = browser.find_element(By.CSS_SELECTOR, ".user-info small")

    assert administrator_email == user_email.text

    browser.quit()

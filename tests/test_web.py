from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Test - open Chrome browser
def test_my_first_chrome_selenium_test(browser):
    # Open testarena webpage - first use Selenium API
    browser.get('http://demo.testarena.pl/zaloguj')
    browser.maximize_window()

    # Verification if title opened webpage contains 'TestArena'
    assert 'TestArena' in browser.title

    # Close web browser
    browser.quit()


# Test - open Edge browser
def test_my_first_edge_selenium_test():
    # Run Edge browser. Path to EdgeChromiumDriverManager(driver for Edge)
    # set automatically by webdriver-mager library
    service = Service(EdgeChromiumDriverManager().install())
    edge_driver = Edge(service=service)

    # Open www.google.pl webpage
    edge_driver.get('http://demo.testarena.pl/zaloguj')
    edge_driver.maximize_window()

    assert "TestArena" in edge_driver.title

    edge_driver.quit()


def test_my_first_firefox_selenium_test():
    service = FirefoxService(GeckoDriverManager().install())
    firefox_driver = Firefox(service=service)

    firefox_driver.get('http://demo.testarena.pl/zaloguj')
    firefox_driver.maximize_window()

    assert "TestArena" in firefox_driver.title

    firefox_driver.quit()


def test_friday_tips(browser):
    browser.get('https://www.ftfs.it/')
    assert 'Friday Tips for Seniors' in browser.title

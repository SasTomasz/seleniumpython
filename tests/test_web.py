from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Test - open Chrome browser
def test_my_first_chrome_selenium_test(get_chrome_driver):
    chrome_driver = get_chrome_driver

    # Open testarena webpage - first use Selenium API
    chrome_driver.get('http://demo.testarena.pl/zaloguj')
    chrome_driver.maximize_window()

    # Verification if title opened webpage contains 'TestArena'
    assert 'TestArena' in chrome_driver.title

    # Close web browser
    chrome_driver.quit()


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


def test_friday_tips(get_chrome_driver):
    browser = get_chrome_driver
    browser.get('https://www.ftfs.it/')
    browser.set_window_size(1920, 1080)
    assert 'Friday Tips for Seniors' in browser.title

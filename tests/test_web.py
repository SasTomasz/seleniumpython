from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Test - uruchomienie Chroma
def test_my_first_chrome_selenium_test():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(ChromeDriverManager().install())
    chrome_driver = Chrome(service=service)

    # Otwarcie strony testareny - pierwsze użycie Selenium API
    chrome_driver.get('http://demo.testarena.pl/zaloguj')
    chrome_driver.maximize_window()

    # Weryfikacja czy tytuł otwartej strony zawiera w sobie 'TestArena'
    assert 'TestArena' in chrome_driver.title

    # Zamknięcie przeglądarki
    chrome_driver.quit()


# Test - uruchomienie Edge
def test_my_first_edge_selenium_test():
    # Uruchomienie przeglądarki Edge. Ścieżka do geckodrivera (drivera dla Firefoxa)
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    service = Service(EdgeChromiumDriverManager().install())
    edge_driver = Edge(service=service)


    # Otwarcie strony www.google.pl
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


def test_friday_tips():
    service = Service(ChromeDriverManager().install())
    browser = Chrome(service=service)
    browser.get('https://www.ftfs.it/')
    browser.set_window_size(1920, 1080)
    assert 'Friday Tips for Seniors' in browser.title
    browser.quit()

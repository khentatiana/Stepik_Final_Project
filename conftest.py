import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or farefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    #user_language = request.config.getoption("language"). This pattern I took from 4.2.step3 comments
    if browser_name  == "chrome":
        print("\nConftest.py: start chrome browser for test..")
        browser = webdriver.Chrome(executable_path="Drivers/chromedriver")
        yield browser
        print("\nConftest.py: quit browser..")
        browser.quit()


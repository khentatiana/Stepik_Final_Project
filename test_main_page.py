import pytest
import time
from .Pages.main_page import MainPage

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_can_go_to_login_page(browser, language):
    url = "http://selenium1py.pythonanywhere.com/{language}/"
    timeout = 10
    page = MainPage(browser,timeout, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    url = "http://selenium1py.pythonanywhere.com/{language}/"
    timeout = 10
    page = MainPage(browser, timeout, url)
    page.open()
    page.should_be_login_link()

#
#
# def go_to_login_page(browser):
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()
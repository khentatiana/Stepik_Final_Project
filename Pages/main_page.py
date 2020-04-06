from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):

    # this methods will be called in test_main_page.py
    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
    #     login_link.click()

    '''Обратите внимание здесь на символ *,
    он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать. '''
    '''Moved method "def go_to_login_page" to bage_page '''
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #     #return LoginPage(browser=self.browser, url=self.browser.current_url)

        '''Затем разработчики добавили alert, который вызывается при клике на нужную нам ссылку. '''
        # alert = self.browser.switch_to.alert
        # alert.accept()

    # this methods will be called in test_main_page.py. This method purposely using wrong locator.
    # If you change locator to correct one: "login_link", then test will pass
    # def should_be_login_link(self):
    #     assert self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid_locator"), \
    #         "Login link is not presented"
    #
    # def should_be_login_link(self):
    #     assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid_locator"), \
    #         "Login link IS NOT PRESENT"
    '''Обратите внимание здесь на символ *, 
        он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать. '''

'''Moved method "def go_to_login_page" to bage_page '''
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link IS NOT PRESENTED"

'''В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку:'''

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        '''Как вы уже знаете, метод __init__ вызывается при создании объекта. 
        Конструктор выше с ключевым словом super на самом деле только вызывает 
        конструктор класса предка и передает ему все те аргументы, которые мы 
        передали в конструктор MainPage. '''

'''А достаточно будет написать так '''
# class MainPage(BasePage):
# #     pass
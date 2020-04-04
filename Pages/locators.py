from selenium.webdriver.common.by import By

#создайте новый класс.Каждый класс будет соответствовать каждому классу PageObject

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

#class LoginPageLocators():

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
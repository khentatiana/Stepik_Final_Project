from selenium.webdriver.common.by import By

#создайте новый класс.Каждый класс будет соответствовать каждому классу PageObject

class MainPageLocators():
    ''' LOGIN_LINK below is for
    is for url = "http://selenium1py.pythonanywhere.com/{language}/"'''
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")         #by ID

    ''' LOGIN_LINK below is for
      url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"'''
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")           #by ID
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")     #by ID


class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")


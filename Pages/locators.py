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
    # This is tag_name(div).class_attribute(alertinner) space tag_name(strong: "div.alertinner strong"
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    # This is several class_names separated by " ." (alert-noicon    alert-info  p)
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    # This is class_name(price_color)
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    # This is tag_name(h1)
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    # This is tag_name(p).class_attribute(price_color): "p.price_color"
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1)")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "##messages .alert:nth-child(1) strong")
    SUCCESS_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

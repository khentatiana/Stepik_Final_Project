from selenium.webdriver.common.by import By

#создайте новый класс.Каждый класс будет соответствовать каждому классу PageObject

class MainPageLocators():
    ''' LOGIN_LINK below is for
    is for url = "http://selenium1py.pythonanywhere.com/{language}/"'''
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    ''' LOGIN_LINK below is for
      url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"'''
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")



# class ProductPageLocators():
#     ADD_TO_BASKET = (By.CSS_SELECTOR, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
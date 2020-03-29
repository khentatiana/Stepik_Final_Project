from selenium.webdriver.common.by import By

#создайте новый класс.Каждый класс будет соответствовать каждому классу PageObject

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


#class ProductPageLocators():
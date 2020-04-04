import pytest
from .Pages.product_page import ProductPage
from .Pages.base_page import BasePage
import time


def test_add_to_cart(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    #url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    timeout = 5
    page = ProductPage(browser, url, timeout)   # инициализируем объект Page Object
    page.open()        # открываем страницу в браузере
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    print ("\nbutton there")
    page.add_product_to_cart()            # жмем кнопку добавить в корзину
    print("\nadded to cart")
    page.solve_quiz_and_get_code()
    print("\nQUIZ is done")
    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
    print("\nSUCCESS MESSAGE IS DISPLAYED")
    time.sleep(10)

    '''In terminal run command:
    python3.8 -m pytest -v -s test_product_page.py
    or run command:
    python3.8 -m pytest -v --tb=line test_product_page.py'''

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
# #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# # def test_guest_can_add_product_to_basket(browser, link):
# #     # ваша реализация теста
# #     page = ProductPage(browser, link)
# #     page.open()
# #     page.add_product_to_cart()
# #     page.add_product_to_cart()  # жмем кнопку добавить в корзину
# #     print("\nadded to cart")
# #     page.solve_quiz_and_get_code()
# #     print("\nQUIZ is done")
# #     time.sleep(5)
# #     page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом
# #     print("\nSUCCESS MESSAGE IS DISPLAYED")
# #     time.sleep(10)
def test_guest_can_add_non_promo_product_to_basket(browser):
    # ваша реализация теста
    #url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    timeout = 5
    page = ProductPage(browser, url, timeout)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()  # жмем кнопку добавить в корзину
    print("\nadded to cart")
    page.should_be_present_in_cart()
    page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом
    print("\nSUCCESS MESSAGE IS DISPLAYED")
    time.sleep(10)

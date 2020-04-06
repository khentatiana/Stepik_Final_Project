import pytest
from .Pages.product_page import ProductPage
from .Pages.base_page import BasePage
from .Pages.login_page import LoginPage
import time

@pytest.mark.skip
def test_add_to_cart(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    #url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    timeout = 5
    page = ProductPage(browser, url, timeout)   # инициализируем объект Page Object
    page.open()        # открываем страницу в браузере
    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    print ("\n test_product_page.py::test_add_to_cart: BUTTON add_to_cart_button is there")
    #page.should_not_be_success_message()
    page.add_product_to_cart()            # жмем кнопку добавить в корзину
    print("\ntest_product_page.py::test_add_to_cart: added to cart")
    page.solve_quiz_and_get_code()
    print("\ntest_product_page.py::test_add_to_cart: QUIZ is done")
    page.should_be_success_message()
    # Down below method "should_not_be_success_message()" will fail test_add_to_cart if everything is OK.
    #page.should_not_be_success_message()
    page.should_check_total_basket_price()
    print("\ntest_product_page.py::test_add_to_cart: Basket is checked")
    #time.sleep(5)

'''In terminal run command:
    python3.8 -m pytest -v -s test_product_page.py
    or run command:
    python3.8 -m pytest -v --tb=line test_product_page.py'''

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip
@pytest.mark.xfail(promo_offer_num ="7")
@pytest.mark.parametrize('promo_offer_num', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_with_promo_to_basket(browser, promo_offer_num):
    # ваша реализация теста
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + promo_offer_num
    timeout = 5
    page = ProductPage(browser, url, timeout)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()  # жмем кнопку добавить в корзину
    print("\ntest_product_page.py::test_guest_can_add_product_with_promo_to_basket: added to cart")
    page.solve_quiz_and_get_code()
    print("\ntest_product_page.py::test_guest_can_add_product_with_promo_to_basket: QUIZ is done")
    page.should_be_present_in_cart()
   #time.sleep(5)
    page.should_check_total_basket_price()
    print("\ntest_product_page.py::test_guest_can_add_product_with_promo_to_basket: Basket is checked")
    #time.sleep(5)

@pytest.mark.skip
def test_guest_can_add_non_promo_product_to_basket(browser):
    # ваша реализация теста
    #url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    timeout = 5
    page = ProductPage(browser, url, timeout)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()  # жмем кнопку добавить в корзину
    print("\ntest_product_page.py::test_guest_can_add_non_promo_product_to_basket: added to cart")
    page.should_be_present_in_cart()
    # page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом
    # print("\ntest_product_page.py::test_guest_can_add_non_promo_product_to_basket: SUCCESS MESSAGE IS DISPLAYED")
    page.should_check_total_basket_price()
    print("\ntest_product_page.py::test_guest_can_add_non_promo_product_to_basket: Basket is checked")
    #time.sleep(5)


'''Открываем страницу товара 
Добавляем товар в корзину 
Проверяем, что нет сообщения об успехе с помощью is_not_element_present'''
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url, timeout=4)
    page.open()
    page.add_product_to_cart()
    page.should_not_be_success_message()

'''Открываем страницу товара 
Проверяем, что нет сообщения об успехе с помощью is_not_element_present'''
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url, timeout=4)
    page.open()
    page.should_not_be_success_message()

'''Открываем страницу товара
Добавляем товар в корзину
Проверяем, что нет сообщения об успехе с помощью is_disappeared'''
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url, timeout=4)
    page.open()
    page.add_product_to_cart()
    time.sleep(1)
    page.should_message_disappeared_after_adding_product_to_basket()


'''Теперь мы можем легко добавлять тесты вида "гость может
 перейти на страницу логина со страницы Х". '''
#@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()

#@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()




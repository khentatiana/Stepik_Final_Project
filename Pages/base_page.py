from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    # Add constructor method with parameters "browser" and "url"
    def __init__(self, browser, timeout, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Add method "open" which will open web page using get()
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


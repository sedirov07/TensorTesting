from pages.base_page import BasePage
from selenium.webdriver.common.by import By


strength_in_people_selector = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
strength_in_people_more_selector = (By.CSS_SELECTOR, "a[href='/about']")


class TensorPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://tensor.ru/')

    @property
    def strength_in_people(self):
        return self.find(strength_in_people_selector)

    @property
    def strength_in_people_more(self):
        return self.find(strength_in_people_more_selector)

    def is_expected_url(self, url='https://tensor.ru/about'):
        expected_url = url
        new_url = self.browser.current_url
        return expected_url == new_url

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


banner_selector = (By.CSS_SELECTOR, "a[title='tensor.ru']")
region_selector = (By.CLASS_NAME, "sbis_ru-link")
partners_list_selector = (By.ID, "contacts_list")
kamchatka_selector = (By.CSS_SELECTOR, "span[title='Камчатский край']")


class ContactsPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://sbis.ru/contacts')

    @property
    def banner(self):
        return self.find(banner_selector)

    @property
    def region(self):
        return self.find(region_selector)

    @property
    def partners(self):
        return self.finds(partners_list_selector)

    @property
    def kamchatka(self):
        return self.find(kamchatka_selector)

    def is_expected_url(self, url='https://tensor.ru/'):
        expected_url = url
        new_url = self.browser.current_url
        return expected_url == new_url

    def is_expected_region(self, region='Свердловская обл.'):
        return self.region == region

    def change_region(self):
        self.region.click()
        self.kamchatka.click()

    def successful_change_region(self, region='Камчатский край'):
        new_url = self.browser.current_url
        return self.region.text == region and '41-kamchatskij-kraj' in new_url and region in self.browser.title

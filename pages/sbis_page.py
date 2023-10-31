from pages.base_page import BasePage
from selenium.webdriver.common.by import By


contacts_selector = (By.CSS_SELECTOR, "a[href='/contacts']")
download_sbis_selector = (By.PARTIAL_LINK_TEXT, "Скачать СБИС")


class SbisPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://sbis.ru/')

    @property
    def contacts(self):
        return self.find(contacts_selector)

    @property
    def downloader_sbis(self):
        downloader = self.find(download_sbis_selector)
        self.scroll_to_element(downloader)
        return downloader

    def is_expected_url(self, sub_url='contacts'):
        expected_sub_url = sub_url
        new_url = self.browser.current_url
        return expected_sub_url in new_url

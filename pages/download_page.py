import os
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


sbis_plugin_selector = (By.CLASS_NAME, "controls-TabButton")
windows_selector = (By.XPATH, "//span[contains(text(), 'Windows')]")
sbis_plugin_downloader_selector = (By.XPATH, "//a[contains(text(), 'Скачать (Exe')]")
file_name = "sbisplugin-setup-web.exe"


class DownloadPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://sbis.ru/download')

    @property
    def sbis_plugin(self):
        return self.finds(sbis_plugin_selector)[1]

    @property
    def windows(self):
        return self.find(windows_selector)

    @property
    def sbis_plugin_downloader(self):
        return self.find(sbis_plugin_downloader_selector)

    @property
    def sbis_plugin_location(self):
        return self.project_dir + '\\' + file_name

    def is_expected_url(self, url='https://tensor.ru/about'):
        expected_url = url
        new_url = self.browser.current_url
        return expected_url == new_url

    def windows_click(self):
        windows = self.windows
        is_selected = "selected" in windows.get_attribute("class")
        if not is_selected:
            windows.click()

    def download_sbis_plugin(self):
        self.sbis_plugin_downloader.click()
        time.sleep(5)

    def sbis_plugin_is_downloaded(self):
        return os.path.isfile(self.sbis_plugin_location)

    def sbis_plugins_have_same_sizes(self):
        file_size = os.path.getsize(self.sbis_plugin_location) / 1024**2
        return str(round(file_size, 2)) in self.sbis_plugin_downloader.text

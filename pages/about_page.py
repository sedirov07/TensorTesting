from pages.base_page import BasePage
from selenium.webdriver.common.by import By


working_selector = (By.XPATH, "//h2[contains(text(),'Работаем')]")
images_selector = (By.XPATH, "//div[contains(@class, 'tensor_ru-About__block3-image-wrapper')]//img")


class AboutPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://tensor.ru/about')

    @property
    def working(self):
        return self.find(working_selector)

    @property
    def working_images(self):
        return self.finds(images_selector)

    @property
    def working_images_heights_and_widths(self):
        images_sizes = []
        for image in self.working_images:
            images_sizes.append((image.get_attribute("height"), image.get_attribute("width")))
        return images_sizes

    def working_images_have_same_sizes(self):
        images_sizes = set(self.working_images_heights_and_widths)
        return len(images_sizes) <= 2

    def is_expected_url(self, url='https://tensor.ru/about'):
        expected_url = url
        new_url = self.browser.current_url
        return expected_url == new_url

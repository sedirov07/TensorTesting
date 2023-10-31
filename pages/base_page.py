import os


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def finds(self, args):
        return self.browser.find_elements(*args)

    def scroll_to_element(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def change_window(self):
        all_windows = self.browser.window_handles
        new_window = all_windows[-1]
        self.browser.switch_to.window(new_window)

    @property
    def project_dir(self):
        return '\\'.join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-1])

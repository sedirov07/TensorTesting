import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    chrome_options = Options()
    download_directory = os.path.dirname(os.path.abspath(__file__))
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_directory,
        'safebrowsing.enabled': 'false'
    })
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()

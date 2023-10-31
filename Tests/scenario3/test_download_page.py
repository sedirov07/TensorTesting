import allure
import pytest
from utils.logger import logger
from pages.download_page import DownloadPage


@pytest.mark.order(9)
@allure.feature("Скачивание СБИС")
@allure.story("Скачивание СБИС")
def test_download_sbis(browser):
    download_page = DownloadPage(browser)
    download_page.open()
    download_page.sbis_plugin.click()
    download_page.windows_click()
    download_page.download_sbis_plugin()
    try:
        assert download_page.sbis_plugin_is_downloaded()
        logger.info("Тест 'test_download_sbis' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_download_sbis' завершился с ошибкой: {e}")


@pytest.mark.order(10)
@allure.feature("Проверка размера плагина СБИС")
@allure.story("Проверка размера плагина СБИС")
def test_sbis_plugin_size(browser):
    download_page = DownloadPage(browser)
    download_page.open()
    download_page.sbis_plugin.click()
    download_page.windows.click()
    try:
        assert download_page.sbis_plugins_have_same_sizes()
        logger.info("Тест 'test_sbis_plugin_size' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_sbis_plugin_size' завершился с ошибкой: {e}")

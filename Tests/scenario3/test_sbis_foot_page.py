import allure
import pytest
from utils.logger import logger
from pages.sbis_page import SbisPage


@pytest.mark.order(8)
@allure.feature("СБИС")
@allure.story("Ссылка на скачивание 'СБИС'")
def test_download_link_sbis(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open()
    sbis_page.downloader_sbis.click()
    try:
        assert sbis_page.is_expected_url('download')
        logger.info("Тест 'test_download_link_sbis' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_download_link_sbis' завершился с ошибкой: {e}")

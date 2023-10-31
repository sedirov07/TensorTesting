import allure
import pytest
from utils.logger import logger
from pages.sbis_page import SbisPage


@pytest.mark.order(0)
@allure.feature("СБИС")
@allure.story("Переход со страницы 'СБИС' на 'СБИС Контакты'")
def test_contacts_url_is_expected(browser):
    contacts_page = SbisPage(browser)
    contacts_page.open()
    contacts_page.contacts.click()
    try:
        assert contacts_page.is_expected_url()
        logger.info("Тест 'test_contacts_url_is_expected' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_contacts_url_is_expected' завершился с ошибкой: {e}")

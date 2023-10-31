import allure
import pytest
from utils.logger import logger
from pages.contacts_page import ContactsPage


@pytest.mark.order(1)
@allure.feature("Контакты")
@allure.story("Поиск баннера 'Тензор'")
def test_banner_tensor_exists(browser):
    contacts_page = ContactsPage(browser)
    contacts_page.open()
    try:
        assert contacts_page.banner
        logger.info("Тест 'test_banner_tensor_exists' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_banner_tensor_exists' завершился с ошибкой: {e}")


@pytest.mark.order(2)
@allure.feature("Контакты")
@allure.story("Переход со страницы 'Контакты' на 'Тензор' при нажатии на баннер 'Тензор'")
def test_banner_tensor_url_is_expected(browser):
    contacts_page = ContactsPage(browser)
    contacts_page.open()
    contacts_page.banner.click()
    contacts_page.change_window()
    try:
        assert contacts_page.is_expected_url()
        logger.info("Тест 'test_banner_tensor_url_is_expected' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_banner_tensor_url_is_expected' завершился с ошибкой: {e}")

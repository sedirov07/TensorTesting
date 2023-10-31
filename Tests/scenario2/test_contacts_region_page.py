import allure
import pytest
from utils.logger import logger
from pages.contacts_page import ContactsPage


@pytest.mark.order(6)
@allure.feature("Контакты")
@allure.story("Проверка автоопределения региона и наличия списка партнеров")
def test_contacts_region_is_expected(browser):
    contacts_region_page = ContactsPage(browser)
    contacts_region_page.open()
    try:
        assert contacts_region_page.is_expected_region()
        logger.info("Автоматически определен верный регион.")
        assert contacts_region_page.partners
        logger.info("Найден список партнеров.")
        logger.info("Тест 'test_contacts_region_is_expected' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_contacts_region_is_expected' завершился с ошибкой: {e}")


@pytest.mark.order(7)
@allure.feature("Контакты")
@allure.story("Изменение региона на 'Камчатский край'")
def test_contacts_change_region(browser):
    contacts_region_page = ContactsPage(browser)
    contacts_region_page.open()
    auto_region_partners = contacts_region_page.partners
    contacts_region_page.change_region()
    changed_region_partners = contacts_region_page.partners
    try:
        assert contacts_region_page.successful_change_region()
        logger.info("Регион успешно изменен.")
        assert auto_region_partners != changed_region_partners
        logger.info("Список партнеров успешно изменен.")
        logger.info("Тест 'test_contacts_change_region' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_contacts_change_region' завершился с ошибкой: {e}")

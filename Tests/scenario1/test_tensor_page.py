import allure
import pytest
from utils.logger import logger
from pages.tensor_page import TensorPage


@pytest.mark.order(3)
@allure.feature("Тензор")
@allure.story("Поиск блока 'Сила в людях' на странице")
def test_block_strength_in_people_exists(browser):
    tensor_page = TensorPage(browser)
    tensor_page.open()
    try:
        assert tensor_page.strength_in_people
        logger.info("Тест 'test_block_strength_in_people_exists' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_block_strength_in_people_exists' завершился с ошибкой: {e}")


@pytest.mark.order(4)
@allure.feature("Тензор")
@allure.story("Переход со страницы 'Тензор' на 'О компании' при нажатии на 'Подробнее'")
def test_block_strength_in_people_exists_more_url_is_expected(browser):
    tensor_page = TensorPage(browser)
    tensor_page.open()
    block_more = tensor_page.strength_in_people_more
    tensor_page.scroll_to_element(block_more)
    block_more.click()
    try:
        assert tensor_page.is_expected_url()
        logger.info("Тест 'test_block_strength_in_people_exists_more_url_is_expected' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_block_strength_in_people_exists_more_url_is_expected' завершился с ошибкой: {e}")

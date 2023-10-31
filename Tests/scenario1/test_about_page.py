import allure
import pytest
from utils.logger import logger
from pages.about_page import AboutPage


@pytest.mark.order(5)
@allure.feature("Подробнее")
@allure.story("Проверка, что все изображения блока 'Работаем' имеют одинаковые размеры")
def test_working_images_have_same_heights_and_widths(browser):
    about_page = AboutPage(browser)
    about_page.open()
    try:
        assert about_page.working_images_have_same_sizes()
        logger.info("Тест 'test_working_images_have_same_heights_and_widths' успешно выполнен.")
    except AssertionError as e:
        logger.error(f"Тест 'test_working_images_have_same_heights_and_widths' завершился с ошибкой: {e}")

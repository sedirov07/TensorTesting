# Автотесты с использованием Python, Selenium и Pytest

## Описание

Этот проект включает в себя автотесты, написанные на Python 3 с использованием библиотеки Selenium Webdriver, тестового фреймворка Pytest, а также паттерна PageObject. Для логирования используется библиотека `logging`, а для создания отчетов - `allure-pytest`.

## Сценарий 1: Проверка Tensor

1. Перейти на [https://sbis.ru/](https://sbis.ru/) и перейти в раздел "Контакты".
2. Найти баннер "Тензор" и кликнуть по нему.
3. Перейти на [https://tensor.ru/](https://tensor.ru/).
4. Проверить, что есть блок "Сила в людях".
5. В этом блоке перейти в "Подробнее" и убедиться, что открывается [https://tensor.ru/about](https://tensor.ru/about).
6. Найти раздел "Работаем" и проверить, что у всех фотографий хронологии одинаковые высота (height) и ширина (width).

## Сценарий 2: Проверка регионов и партнеров

1. Перейти на [https://sbis.ru/](https://sbis.ru/) и перейти в раздел "Контакты".
2. Проверить, что определен регион и есть список партнеров.
3. Изменить регион на "Камчатский край".
4. Проверить, что подставился выбранный регион, список партнеров изменился, URL и заголовок (title) содержат информацию выбранного региона.

## Сценарий 3: Скачивание СБИС Плагина

1. Перейти на [https://sbis.ru/](https://sbis.ru/).
2. Найти и перейти в Footer по "Скачать СБИС".
3. Скачать СБИС Плагин для Windows в папку с данным тестом.
4. Убедиться, что плагин был успешно скачан.
5. Сравнить размер скачанного файла в мегабайтах с размером, указанным на сайте.

## Требования

- Python 3
- Библиотеки: Selenium, pytest, logging, allure-pytest
- WebDriver для браузера, например, Chrome WebDriver

## Установка и Запуск
### Установка
1. Установите необходимые библиотеки:
   ```bash
   pip install -r requirements.txt
2. Убедитесь, что chrome webdriver установлен и добавлен в переменную PATH.
3. Для создания отчетов при помощи allure убедитесь, что установлен и добавлен в переменную PATH и JAVA_HOME Node.js, после чего пропишите:
   ```bash
   npm install -g allure-commandline
   
### Запуск
1. Запуск всех тестов с созданием allure-отчета
   ```bash
   pytest --allure-dir=allure-results
2. Открытие allure-отчета с использованием веб-интерфейса (Node.js)
   ```bash
   allure serve allure-results
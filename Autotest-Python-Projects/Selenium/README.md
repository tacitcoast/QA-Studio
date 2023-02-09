# 🦸‍♀️ Автотесты Python + Selenium + Allure
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com)

> Тестирование фронта

## Сайт для отправки открыток
Сайт: https://postcard.qa.studio/

Проект: [папка проекта](https://github.com/tacitcoast/QA-Studio/tree/main/Autotest-Python-Projects/Selenium/Postcard-Website), [файл с тестами](https://github.com/tacitcoast/QA-Studio/blob/main/Autotest-Python-Projects/Selenium/Postcard-Website/tests/test_main.py)
- Smoke test: проверяем наличие кнопки на сайте:
    - Ищем кнопку "Отправить"
    - Ждем пока загрузится элемент
    - Проверяем текст на кнопке
- Positive test: отправляем открытку:
    - Вводим email
    - Выбираем открытку
    - Вводим сообщение
    - Отправляем открытку
    - Проверяем модальное окно
- Negative test: отправляем открытку с незаполненным полем email:
    - Находим атрибут нужного класса, без сообщения об ошибки
    - Нажимаем кнопку отправить, не заполняя email
    - Проверяем, что трибут класса сообщает об ошибке

## Сайт для покупки мебели
Сайт: https://test.qa.studio

Проект: [папка проекта](https://github.com/tacitcoast/QA-Studio/tree/main/Autotest-Python-Projects/Selenium/Furniture-Website), [файл с тестами](https://github.com/tacitcoast/QA-Studio/blob/main/Autotest-Python-Projects/Selenium/Postcard-Website/tests/test_main.py), [отчёт allure](https://github.com/tacitcoast/QA-Studio/tree/main/Autotest-Python-Projects/Selenium/Furniture-Website/my_allure_results)
- Тест-кейс WERT-1: Открытие деталей товара. Проверка артикула

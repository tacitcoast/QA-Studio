# 🦸‍♀️ Автотесты Python + Selenium + Allure
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com)

> Тестирование фронта

## 1. Сайт для отправки открыток
Сайт: https://postcard.qa.studio/

Проект: [папка проекта](https://github.com/tacitcoast/QA-Studio/tree/main/Autotest-Python-Projects/Selenium/Postcard-Website), [файл с тестами](https://github.com/tacitcoast/QA-Studio/blob/main/Autotest-Python-Projects/Selenium/Postcard-Website/tests/test_main.py)
- Smoke test: проверяем наличие кнопки на сайте:
    - Переходим на сайт
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
- Allure: 

<img src="https://user-images.githubusercontent.com/44261093/217888108-8fbffa48-1b24-45aa-83af-672bfe2db37b.jpg" width="300"> <img src="https://user-images.githubusercontent.com/44261093/217886487-470e3d9c-3ac2-4019-ae0c-6d698b91800f.jpg" width="450">


## 2. Сайт для покупки мебели
Сайт: https://test.qa.studio

Проект: [папка проекта](https://github.com/tacitcoast/QA-Studio/tree/main/Autotest-Python-Projects/Selenium/Furniture-Website), [файл с тестами](https://github.com/tacitcoast/QA-Studio/blob/main/Autotest-Python-Projects/Selenium/Furniture-Website/tests/test_main.py), [отчёт allure](https://github.com/tacitcoast/QA-Studio/tree/main/Autotest-Python-Projects/Selenium/Furniture-Website/my_allure_results)
- Test case: Открытие деталей товара. Проверка артикула:
    - Переходим на сайт
    - Ищем по селектору элемент меню "Горячие товары" и кликаем по нему
    - Ищем по XPATH "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    - Ищем по имени класса артикул для "Журнального столика"
    - Проверяем соответствие

## 3. Сайт для покупки мебели
Сайт: https://test.qa.studio

Проект: [папка проекта](https://github.com/tacitcoast/QA-Studio/tree/main/Autotest-Python-Projects/Selenium/QAStudio-Website), [test case #1](https://github.com/tacitcoast/QA-Studio/blob/main/Autotest-Python-Projects/Selenium/QAStudio-Website/tests/test_first.py), [test case #2](https://github.com/tacitcoast/QA-Studio/blob/main/Autotest-Python-Projects/Selenium/QAStudio-Website/tests/test_shop.py) [отчёт allure](https://github.com/tacitcoast/QA-Studio/tree/main/Autotest-Python-Projects/Selenium/QAStudio-Website/my_allure_results)
- Test case #1: Smoke test
    - Переходим на сайт
    - Нажимаем "Горячие товары"
    - Выбираем Журнальный столик
    - Проверяем актикул товара
- Test case #2: Проверка покупки
    - Сверяем элементы меню
    - Скролим страницу до последнего товара
    - Добавляем товар в корзину
    - Оформляем заказ: заполняем все поля
    - Проверяем, что покупка прошла успешно
- Allure: 

<img src="https://user-images.githubusercontent.com/44261093/217889087-5a0a7fe4-666e-4391-87b3-e5c7b08936cd.jpg" width="300"> <img src="https://user-images.githubusercontent.com/44261093/217889100-6208f671-289e-412d-900b-c4c73f2280bf.jpg" width="380">

____
<p align="center">
  <img src="https://komarev.com/ghpvc/?username=tacitcoast" alt="tacitcoast" />
    <a href="https://github.com/tacitcoast/"><img src="https://img.shields.io/github/followers/tacitcoast?style=flat-square?color=%234CC61E&label=GitHub%20Followers%20"/></a>
  <a href="https://github.com/tacitcoast/"><img src="https://img.shields.io/github/last-commit/tacitcoast/tacitcoast?style=flat-square?color=red&label=Last%20Updated%20"/></a>
</p>


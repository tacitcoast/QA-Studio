# 🐯 Автотесты JS Cypress

Здесь собраны мои автотесты

## Автотесты для формы логина и пароля на https://login.qa.studio/

> Важно: у поля логин есть логика. Если не указать @ то после отправки логина и пароля получим ошибку валидации. Поле для ввода имейла на клиенте должны приводить к строчным буквам

1. [Проверка на позитивный кейс авторизации](https://github.com/tacitcoast/QA-Studio/blob/main/Cypress.JS/cypress/integration/4_QA_Studio/login.js):

    -  Ввод правильного логина
    -  Ввод правильного пароля
    -  Нажать войти
    -  Проверка нужного текса
    -  Нажать крестик
    -  Проверка нужного текста


2. [Проверка логики восстановления пароля](https://github.com/tacitcoast/QA-Studio/blob/main/Cypress.JS/cypress/integration/4_QA_Studio/login.js):

    - Нажать «Забыли пароль»
    - Ввести любой имейл
    - Проверка, что получили нужный текст и есть кнопка крестика

3. [Проверка на негативный кейс авторизации](https://github.com/tacitcoast/QA-Studio/blob/main/Cypress.JS/cypress/integration/4_QA_Studio/login.js):

    - Ввод правильного логина
    - Ввод НЕправильного пароля
    - Нажать войти
    - Проверка нужного текста и наличие кнопки крестик

4. [Проверка на негативный кейс авторизации](https://github.com/tacitcoast/QA-Studio/blob/main/Cypress.JS/cypress/integration/4_QA_Studio/login.js):

    - Ввод НЕправильного логина
    - Ввод правильного пароля
    - Нажать войти
    - Проверка нужного текста и наличие кнопки крестик

5. [Проверка на негативный кейс валидации](https://github.com/tacitcoast/QA-Studio/blob/main/Cypress.JS/cypress/integration/4_QA_Studio/login.js):

    - Ввод логин без @
    - Ввод правильного пароля
    - Нажать войти
    - Проверка, что получаем текст с ошибкой

6. [Проверка на привидение к строчным буквам в логине](https://github.com/tacitcoast/QA-Studio/blob/main/Cypress.JS/cypress/integration/4_QA_Studio/login.js):

    - Ввод логина с заглавными буквами
    - Ввод правильного пароля
    - Нажать войти
    - Проверить, что авторизация успешна (нужный текст и наличие кнопки крестик)

____

## Автотест для https://testqastudio.me/

1. [Проверка покупки товаров на сайте](https://github.com/tacitcoast/QA-Studio/blob/main/Cypress.JS/cypress/integration/4_QA_Studio/purchase.js):

    - Открытие карточки товара
    - Изменение количества
    - Отправка в корзину
    - Вовзращение на главную страницу
    - Открытие новой карточки и добавление в корзину
    - Завершение покупки
    - Проверка, что покупка успешно совершенна

____

[![made-with-javascript](https://img.shields.io/badge/Made%20with-JavaScript-1f425f.svg)](https://www.javascript.com)
![Profile views](https://gpvc.arturio.dev/tacitcoast)
[![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com)


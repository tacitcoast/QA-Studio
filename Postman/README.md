# 👾 Автотесты JS + Postman

Здесь собраны мои автотесты

## Автотесты для сайта, посвящённый звёздным войнам
> Адрес АПИ: https://swapi.dev/

1. [Автотесты к запросам по персонажу, за планетой и за космическим кораблём](https://github.com/tacitcoast/QA-Studio/blob/main/Postman/Starwars.postman_collection.json):

    - Проверка статуса ответа 200
    - Время отклика составляет менее 200 мс
    - Status code name has string
    - Content-Type is present
    - Body matches string
    - Сравнение поля url
    - Успешный запрос POST

![tg_image_659238402](https://user-images.githubusercontent.com/44261093/220179371-b4a568f5-3955-413e-a7c6-36aa1e9b3704.jpeg)

## Автотесты для сайта HeadHunter
> Gубличной АПИ https://dev.hh.ru

> Документация к ней: https://github.com/hhru/api

1. [Автотесты к запросу по поиску работодателя](https://github.com/tacitcoast/QA-Studio/blob/main/Postman/HeadHunter.postman_collection.json):

    - Status code is 200
    - Body matches string
    - Сравнение поля id
    - Тест на скорость


## 🗿 Свой CI/CD

CI/CD — Continuous Integration (CI) и Continuous Delivery (CD). Это философия непрерывной интеграции и доставки.

Для практики я создала свой CI/CD в github actions.

План реализации: запускать проверку линтера css (это проверка на соблюдение стандарта синтаксиса css) и отправлять отчёт в telegram.

> Для запуска CI/CD в репозитории проекта создан файл в формате .yml, в котором описана необходимая последовательность.

[В этом .yml файле содержится вся настройка](https://github.com/tacitcoast/tacitcoast.github.io/blob/main/.github/workflows/cicd.yml)

## Что получилось
Теперь при любом из событий:
- Любой пуш и коммит в main ветку
- Любой открытый pull request

Будет запускаться сборка ci/cd (github actions).

___
<p align="center">
  <img src="https://komarev.com/ghpvc/?username=tacitcoast" alt="tacitcoast" />
    <a href="https://github.com/tacitcoast/"><img src="https://img.shields.io/github/followers/tacitcoast?style=flat-square?color=%234CC61E&label=GitHub%20Followers%20"/></a>
  <a href="https://github.com/tacitcoast/"><img src="https://img.shields.io/github/last-commit/tacitcoast/tacitcoast?style=flat-square?color=red&label=Last%20Updated%20"/></a>
</p>

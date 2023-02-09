# Импортируем модули и отдельные классы
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем переменную с тестируемым сайтом
URL = 'https://postcard.qa.studio/'


# Smoke test: запускаем тест с текстурой browser
def test_smoke(browser):
    # Переходим на адрес тестируемой страницы
    browser.get(URL)
    # Ищем кнопку "Отправить"
    button = browser.find_element(By.ID, value="send")
    # Ждем пока загрузится элемент
    WebDriverWait(browser, timeout=5, poll_frequency=1).until(EC.visibility_of_element_located(
        (By.ID, "send")))
    # Проверяем текст на кнопке
    assert button.text == 'Отправить', 'Unexpected text on button'


# Список, чтобы прооверить, что все две картинки отправляются
CASE = [
    0, 1
]

# Positive test: отправляем открытку
@pytest.mark.parametrize('case', CASE)
def test_send_postcard(browser, case):
    browser.get(URL)

    # Вводим email
    email = browser.find_element(By.ID, value="email")
    email.click()
    email.send_keys("hello@qa.studio")

    # Выбираем открытку
    cards = browser.find_elements(By.CSS_SELECTOR, value='[class*="photo-parent"]')
    cards[case].click()

    # Вводим сообщение
    message = browser.find_element(By.ID, value="textarea")
    message.click()
    message.send_keys("Hello world!")

    # Отправляем открытку
    button = browser.find_element(By.ID, value="send")
    button.click()

    # Выбираем модальное окно
    modal = browser.find_element(By.ID, value="modal")

    # Проверяем, что в модальном окне появилась нужная надпись
    assert modal.text == "Открытка успешно отправлена!", ""


# Негативный тест: отправляем открытку не заполняя поле email
def test_empty_input_send(browser):
    browser.get(URL)

    # Находим атрибут нужного класса, без сообщения об ошибки
    email_label = browser.find_element(By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == "requered", "Unexpected attribute class"

    # Нажимаем кнопку отправить, не заполняя email
    button = browser.find_element(By.ID, value="send").click()

    # Проверяем, что трибут класса сообщает об ошибке
    email_label = browser.find_element(By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == "requered error", "Unexpected attribute class"
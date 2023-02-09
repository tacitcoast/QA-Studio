# Импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Тест-кейс WERT-1: Открытие деталей товара. Проверка артикула:
def test_product_view_sku():
	    # Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
	
	    # Устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
        # Запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
	    # Определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
	    # Ищем по селектору элемент меню "Горячие товары" и кликаем по нему
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()
		# Ищем по XPATH "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = driver.find_element(By.XPATH, value=x_path_table)
    element.click()
		# Ищем по имени класса артикул для "Журнального столика"
    sku = driver.find_element(By.CLASS_NAME, value="sku")
		# Проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"
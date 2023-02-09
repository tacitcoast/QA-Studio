# Fixture
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='session')
def browser():
    # Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox") # отключаем песочницу
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
    service = Service(ChromeDriverManager().install()) # устанавливаем webdriver в соответствии с версией браузера
    driver = webdriver.Chrome(service=service, options=chrome_options) # запускаем браузер с указанными выше настройками
    
    # Если что-то пойдет не так, мы закроем браузер
    yield driver
    driver.quit()

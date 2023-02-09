"""
UI test for test.qa.studio
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.helper.common import CommonHelper


URL = "https://test.qa.studio"


def test_top_menu(browser):
    """
    Test case TC-2
    """
    expected_menu = ['Каталог', 'Часто задавамые вопросы', 'Блог', 'О компании', 'Контакты']

    browser.get(URL)
    elements = browser.find_elements(by=By.CSS_SELECTOR, value="[id='menu-top'] li a")
    result = [el.get_attribute('text') for el in elements]

    assert expected_menu == result, 'Top menu does not matching to expected'


@pytest.mark.xfail(reason="Wait for fix bug")
def test_products_group(browser):
    """
    Test case TC-2
    """
    expected_menu = [
        ("Все", "", "[class='tab-all active']"),
        ("Бестселлеры", "/?products_group=best_sellers", "[class='tab-best_sellers ']"),
        ("Горячие товары", "/?products_group=featured", "[class='tab-featured ']"),
        ("Новые товары", "/?products_group=new", "[class='tab-new ']"),
        ("Распродажа товаров", "/?products_group=sale", "[class='tab-sale ']")
    ]

    browser.get(URL)
    menu_element = "[class='catalog-toolbar-tabs__content'] a"
    elements = browser.find_elements(by=By.CSS_SELECTOR, value=menu_element)
    assert len(elements) == len(expected_menu), "Unexpected number of products group"

    for item in expected_menu:
        element = browser.find_element(by=By.CSS_SELECTOR, value=item[2])
        element.click()

    result = [el.get_attribute('text') for el in elements]

    assert expected_menu == result, 'Top menu does not matching to expected'

def test_count_of_all_products(browser):
    """
    Test case TC-3
    """
    browser.get(URL)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "current-post"), "17"))

    elements = browser.find_elements(by=By.CSS_SELECTOR, value="[id='rz-shop-content'] ul li")

    assert len(elements) == 17, "Unexpected count of products"

def test_right_way(browser):
    """
    Test case TC-4
    """
    browser.get(URL)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "current-post"), "17"))

    product = browser.find_element(by=By.CSS_SELECTOR, value="[data-product_sku='4XAVRC35']")
    product.click()

    WebDriverWait(browser, timeout=10, poll_frequency=2).until(
        EC.visibility_of_element_located((By.ID, "cart-modal")))

    cart_is_visible = browser.find_element(
        By.XPATH, value="//div[@id='cart-modal']").value_of_css_property("display")
    assert cart_is_visible == "block", "Unexpected state of cart"

    browser.find_element(by=By.CSS_SELECTOR, value="a.button.checkout").click()
    WebDriverWait(browser, timeout=10, poll_frequency=1).until(
        EC.url_to_be("https://test.qa.studio/checkout/"))

    common_helper = CommonHelper(browser)
    common_helper.enter_input(input_id="billing_first_name", data="Andrey")
    common_helper.enter_input(input_id="billing_last_name", data="Ivanov")
    common_helper.enter_input(input_id="billing_address_1", data="2-26, Sadovaya street")
    common_helper.enter_input(input_id="billing_city", data="Moscow")
    common_helper.enter_input(input_id="billing_state", data="Moscow")
    common_helper.enter_input(input_id="billing_postcode", data="122457")
    common_helper.enter_input(input_id="billing_phone", data="+79995784256")
    common_helper.enter_input(input_id="billing_email", data="andrey.i@mail.ru")

    payments_el = '//*[@id="payment"] [contains(@style, "position: static; zoom: 1;")]'
    WebDriverWait(browser, timeout=10, poll_frequency=1).until(
        EC.presence_of_element_located((By.XPATH, payments_el)))
    browser.find_element(by=By.ID, value="place_order").click()

    WebDriverWait(browser, timeout=5, poll_frequency=1).until(
        EC.url_changes("https://test.qa.studio/?page_id=10"))

    result = WebDriverWait(browser, timeout=10, poll_frequency=2).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), \
                "Ваш заказ принят. Благодарим вас."))

    assert result, 'Unexpected notificztion text'

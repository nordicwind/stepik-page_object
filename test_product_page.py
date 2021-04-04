import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
parameters = [
    '?promo=offer0',
    '?promo=offer1',
    '?promo=offer2',
    '?promo=offer3',
    '?promo=offer4',
    '?promo=offer5',
    '?promo=offer6',
    pytest.param('?promo=offer7', marks=pytest.mark.xfail),
    '?promo=offer8',
    '?promo=offer9',
]


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@mailinator.com"
        password = str(time.time()) + "@mailinator.com"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        page.should_be_authorized_user()

    # Removed parameter as required
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    # @pytest.mark.skip
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.success_message_should_appear()
        page.product_title_should_match_product_in_basket()
        page.product_price_and_basket_should_match()


@pytest.mark.parametrize('parameter', parameters)
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, parameter):
    page = ProductPage(browser, f"{link}{parameter}")
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_appear()
    page.product_title_should_match_product_in_basket()
    page.product_price_and_basket_should_match()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_be_empty_basket_text()

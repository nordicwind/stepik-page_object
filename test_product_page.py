from pages.product_page import ProductPage
import time


link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_appear()
    page.product_title_should_match_product_in_basket()
    page.product_price_and_basket_should_match()

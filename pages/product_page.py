from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def success_message_should_appear(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE_ALERT), "Success message doesn't appear"

    def product_title_should_match_product_in_basket(self):
        success_alert_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_TEXT).text
        product_title_text = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert product_title_text in success_alert_text, "Test product doesn't match product added to basket"

    def product_price_and_basket_should_match(self):
        basket_text = self.browser.find_element(*ProductPageLocators.BASKET_TEXT).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MAIN).text
        assert product_price in basket_text, "Product price doesn't match basket amount"

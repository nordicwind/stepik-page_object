from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE_ALERT = (By.CSS_SELECTOR, "div.alert-success")
    PRODUCT_TITLE = "The shellcoder's handbook"
    SUCCESS_MESSAGE_TEXT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRODUCT_PRICE_MAIN = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    BASKET_TEXT = (By.CSS_SELECTOR, 'div.basket-mini')

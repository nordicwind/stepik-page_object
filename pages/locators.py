from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    BASKET_LINK_INVALID = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default-invalid")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ADDED_ITEM_LIST = (By.CSS_SELECTOR, "div#content_inner > form#basket_formset")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REGISTRATION_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


class MainPageLocators:
    pass


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE_ALERT = (By.CSS_SELECTOR, "div.alert-success")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main > h1")
    SUCCESS_MESSAGE_TEXT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE_MAIN = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    BASKET_TEXT = (By.CSS_SELECTOR, 'div.basket-mini')

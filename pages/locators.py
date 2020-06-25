from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_INPUT_FOR_REGISTER_FORM = (By.CSS_SELECTOR, "[id='id_registration-email']")
    PASSWORD_INPUT_FOR_REGISTER_FORM = (By.NAME, "registration-password1")
    CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "form button.btn.btn-lg")
    MESSAGE_ABOUT_SUCCESS_ADDED_INTO_BASKET = (By.XPATH, "//div[@id='messages']/child::div[1]")
    PRODUCT_NAME_SHOULD_BE = (By.CSS_SELECTOR, "div h1")
    PRODUCT_NAME_ADDED_INTO_BASKET = (By.CSS_SELECTOR, "#messages div:first-child div.alertinner strong")
    PRODUCT_PRICE_SHOULD_BE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_PRICE_ADDED_INTO_BASKET = (By.XPATH, "//div[@id='messages']/child::div[3]/div/child::p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/child::div[1]")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a")
    USER_ICON = (By.CSS_SELECTOR, "div.alertinner.wicon")


class ViewBasketLocators:
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "div[id='content_inner'] p")
    EMPTY_BASKET = (By.XPATH, "div.basket-title.hidden-xs")

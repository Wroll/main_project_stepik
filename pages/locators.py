from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "form button.btn.btn-lg")
    MESSAGE_ABOUT_SUCCESS_ADDED_INTO_BASKET = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]")
    PRODUCT_NAME_SHOULD_BE = (By.CSS_SELECTOR, "div h1")
    PRODUCT_NAME_ADDED_INTO_BASKET = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    PRODUCT_PRICE_SHOULD_BE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    PRODUCT_PRICE_ADDED_INTO_BASKET = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]")

from selenium.webdriver.common.by import By


class SignInPageLocators:
    class Buttons:
        SIGN_IN = (By.CSS_SELECTOR, ".full")

    class Links:
        SIGN_UP = (By.CSS_SELECTOR, "[href='/sign_up']")

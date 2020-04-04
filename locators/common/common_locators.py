from selenium.webdriver.common.by import By


class CommonLocators:
    class Links:
        SIGN_IN = (By.CSS_SELECTOR, "[href='/signin']")
        FORGOT_PASSWORD = (By.CSS_SELECTOR, "[href='/forgot']")

    class Inputs:
        EMAIL = (By.CSS_SELECTOR, "input[name='email']")
        PASSWORD = (By.CSS_SELECTOR, "input[name='password']")

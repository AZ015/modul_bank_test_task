from selenium.webdriver.common.by import By


class SignUpPageLocators:
    class Inputs:
        COMPANY_NAME = (By.CSS_SELECTOR, "input[name='company']")
        FIRST_NAME = (By.CSS_SELECTOR, "input[name='name']")
        LAST_NAME = (By.CSS_SELECTOR, "input[name='surname']")
        MOBILE_PHONE = (By.CSS_SELECTOR, "input[name='phone']")
        EMAIL = (By.CSS_SELECTOR, "input[name='email']")
        PASSWORD = (By.CSS_SELECTOR, "input[name='password']")

    class Buttons:
        SIGN_UP = (By.CSS_SELECTOR, ".button")

    class Checkboxes:
        AGREEMENT = (By.CSS_SELECTOR, ".label_check")

    class Links:
        SIGN_IN = (By.CSS_SELECTOR, "[href='/signin']")

    class Alerts:
        SUCCESSFULLY_REGISTRATION = (By.CSS_SELECTOR, "div.info > p")

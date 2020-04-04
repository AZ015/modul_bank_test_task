from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    class Header:
        pass

    class Buttons:
        CLEARLY = (By.CSS_SELECTOR, ".middle[type='button']")

    class Alerts:
        TIPS = (By.CSS_SELECTOR, ".joyride-tooltip > .joyride-tooltip__header")
        TITLE = (By.CSS_SELECTOR, ".center-info > .title")


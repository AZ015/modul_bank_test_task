from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def close_tips(self) -> None:
        self._click(PersonalAccountLocators.Alerts.TIPS)

    def click_on_clearly(self) -> None:
        self._click(PersonalAccountLocators.Buttons.CLEARLY)

    @property
    def title(self):
        return self._get_element_text(PersonalAccountLocators.Alerts.TITLE)

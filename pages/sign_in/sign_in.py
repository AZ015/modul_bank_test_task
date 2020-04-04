from locators.common.common_locators import CommonLocators
from locators.sign_in_locators import SignInPageLocators
from pages.base_page import BasePage


class SignInPage(BasePage):

    def sign_in(self, email: str, password: str) -> None:
        self._set_email(email)
        self._set_password(password)
        self._click_on_sign_in_button()

    def _set_email(self, email: str) -> None:
        self._input(CommonLocators.Inputs.EMAIL, email)

    def _set_password(self, password: str) -> None:
        self._input(CommonLocators.Inputs.PASSWORD, password)

    def _click_on_sign_in_button(self) -> None:
        self._click(SignInPageLocators.Buttons.SIGN_IN)

from locators.common.common_locators import CommonLocators
from locators.sign_up_locators import SignUpPageLocators
from pages.base_page import BasePage


class SignUpPage(BasePage):

    def sign_up(self, company_name: str, first_name: str, last_name: str, phone_number: str, email: str,
                password) -> None:
        self._set_company_name(company_name)
        self._set_first_name(first_name)
        self._set_last_name(last_name)
        self._set_phone_number(phone_number)
        self._set_email(email)
        self._set_password(password)
        self._set_agreement()
        self._click_on_sign_up_button()

    def go_to_sign_in_page(self) -> None:
        self._click(SignUpPageLocators.Links.SIGN_IN)

    def go_to_forgot_password_page(self) -> None:
        self._click(CommonLocators.Links.FORGOT_PASSWORD)

    @property
    def successfully_message(self) -> str:
        return self._get_element_text(SignUpPageLocators.Alerts.SUCCESSFULLY_REGISTRATION)

    def _set_company_name(self, company_name: str) -> None:
        self._input(SignUpPageLocators.Inputs.COMPANY_NAME, company_name)

    def _set_first_name(self, first_name: str) -> None:
        self._input(SignUpPageLocators.Inputs.FIRST_NAME, first_name)

    def _set_last_name(self, last_name: str) -> None:
        self._input(SignUpPageLocators.Inputs.LAST_NAME, last_name)

    def _set_phone_number(self, phone_number: str) -> None:
        self._input(SignUpPageLocators.Inputs.MOBILE_PHONE, phone_number)

    def _set_email(self, email: str) -> None:
        self._input(SignUpPageLocators.Inputs.EMAIL, email)

    def _set_password(self, password: str) -> None:
        self._input(SignUpPageLocators.Inputs.PASSWORD, password)

    def _set_agreement(self) -> None:
        self._click(SignUpPageLocators.Checkboxes.AGREEMENT)

    def _click_on_sign_up_button(self) -> None:
        self._click(SignUpPageLocators.Buttons.SIGN_UP)

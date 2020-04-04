from const.messages import PersonAccountMessages
from const.messages import SignUpMessages


class TestRegistration:
    def test_successfully_sign_up(self, sign_up_page, sign_in_page, personal_account_page, sign_up_info):
        company_name, first_name, last_name, phone, email, password = sign_up_info
        sign_up_page.sign_up(company_name=company_name, first_name=first_name, last_name=last_name, phone_number=phone,
                             email=email, password=password)
        assert sign_up_page.successfully_message == SignUpMessages.SUCCESSFUL_REGISTER_MESSAGE
        sign_up_page.go_to_sign_in_page()
        sign_in_page.sign_in(email=email, password=password)
        personal_account_page.click_on_clearly()
        assert personal_account_page.title == PersonAccountMessages.TITLE

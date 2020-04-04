from urllib.parse import urljoin

import pytest

from const import Endpoints
from data_providers.sign_up.sign_up import generate_sign_up_info
from pages.personal_account.personal_account import PersonalAccountPage
from pages.sign_in import SignInPage
from pages.sign_up import SignUpPage


@pytest.fixture(scope='session')
def sign_up_page(browser, url) -> SignUpPage:
    browser.get(urljoin(url, Endpoints.SIGN_UP))
    return SignUpPage(browser)


@pytest.fixture(scope='session')
def sign_in_page(browser) -> SignInPage:
    return SignInPage(browser)


@pytest.fixture(scope='session')
def personal_account_page(browser) -> PersonalAccountPage:
    return PersonalAccountPage(browser)


@pytest.fixture()
def sign_up_info():
    return generate_sign_up_info()

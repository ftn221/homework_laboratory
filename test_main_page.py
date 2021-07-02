from .pages.main_page import MainPage
from .pages.locators import MainPageLocators

link = MainPageLocators.MAIN_PAGE_LINK


class TestMainPage():
    def test_send_email_with_login(self, browser):
        # Arrange
        page = MainPage(browser, link)
        page.open()
        page.check_have_login_form()
        page.check_have_email_input()
        page.clear_email_input()
        page.send_keys_to_email_input()
        page.choose_domen_name()
        page.check_password_button()
        page.click_password_button()
        page.check_password_input()
        page.clear_password_input()
        page.send_keys_to_password_input()
        page.check_enter_button()
        page.click_enter_button()
        page.check_new_email_button()
        page.click_new_email_button()
        # Act
        page.check_recipient_input()
        page.send_keys_to_recipient_input()
        page.check_letter_body()
        page.send_keys_to_letter_body()
        page.check_submit_button()
        page.click_submit_button()
        # Assert
        page.check_layer_sent_page()

from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):

    def check_have_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), 'Login form is not present'

    def check_have_email_input(self):
        assert self.is_element_present(*MainPageLocators.EMAIL_INPUT), 'Email input is not present'

    def clear_email_input(self):
        email_input = self.browser.find_element(*MainPageLocators.EMAIL_INPUT)
        email_input.clear()

    def send_keys_to_email_input(self):
        email_input = self.browser.find_element(*MainPageLocators.EMAIL_INPUT)
        email_input.send_keys(MainPageLocators.LOGIN)

    def choose_domen_name(self):
        select = Select(self.browser.find_element(*MainPageLocators.DOMAIN_SELECT))
        select.select_by_value(MainPageLocators.DOMAIN_NAME)

    def check_password_button(self):
        assert self.is_element_present(*MainPageLocators.PASSWORD_BUTTON), 'Password button is not present'

    def click_password_button(self):
        password_button = self.browser.find_element(*MainPageLocators.PASSWORD_BUTTON)
        password_button.click()

    def check_password_input(self):
        assert self.is_element_present(*MainPageLocators.PASSWORD_INPUT), 'Password input is not present'

    def clear_password_input(self):
        password_input = self.browser.find_element(*MainPageLocators.PASSWORD_INPUT)
        password_input.clear()

    def send_keys_to_password_input(self):
        password_input = self.browser.find_element(*MainPageLocators.PASSWORD_INPUT)
        password_input.send_keys(MainPageLocators.PASSWORD)

    def check_enter_button(self):
        assert self.is_element_present(*MainPageLocators.ENTER_BUTTON), 'Enter button is not present'

    def click_enter_button(self):
        enter_button = self.browser.find_element(*MainPageLocators.ENTER_BUTTON)
        enter_button.click()

    def check_new_email_button(self):
        assert self.is_element_present(*MainPageLocators.NEW_EMAIL_BUTTON)

    def click_new_email_button(self):
        new_email_button = self.browser.find_element(*MainPageLocators.NEW_EMAIL_BUTTON)
        new_email_button.click()

    def check_recipient_input(self):
        assert self.is_element_present(*MainPageLocators.RECIPIENT_INPUT), 'recipient input is not present'

    def send_keys_to_recipient_input(self):
        recipient_input = self.browser.find_element(*MainPageLocators.RECIPIENT_INPUT)
        recipient_input.send_keys(MainPageLocators.RECIPIENT_EMAIL)

    def check_letter_body(self):
        assert self.is_element_present(*MainPageLocators.LETTER_BODY)

    def send_keys_to_letter_body(self):
        letter_body = self.browser.find_element(*MainPageLocators.LETTER_BODY)
        letter_body.send_keys(MainPageLocators.SOME_TEXT_TO_LETTER_BODY)

    def check_submit_button(self):
        assert self.is_element_present(*MainPageLocators.SUBMIT_BUTTON), 'Submit button is not present'

    def click_submit_button(self):
        submit_button = self.browser.find_element(*MainPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    # Проверка наличия страницы с сообщением об успешной отправке
    # в идеале можно было бы проверить на наличие текста "Сообщение отправлено", но здесь надо решать проблему многоязычности
    def check_layer_sent_page(self):
        assert self.is_element_present(*MainPageLocators.LAYER_SENT_PAGE), 'Layer sent page is not present'

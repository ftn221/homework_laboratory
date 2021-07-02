from selenium.webdriver.common.by import By

class MainPageLocators():
    MAIN_PAGE_LINK = 'https://mail.ru/'
    LOGIN_FORM = (By.ID, 'mailbox')
    EMAIL_INPUT = (By.CLASS_NAME, 'email-input')
    DOMAIN_SELECT = (By.CLASS_NAME, 'domain-select')
    LOGIN = 'test26262727272'
    DOMAIN_NAME = '@mail.ru'
    PASSWORD_BUTTON = (By.CSS_SELECTOR, '#mailbox .body button')
    PASSWORD_INPUT = (By.CLASS_NAME, 'password-input')
    PASSWORD = 'awergsergsegserg567'
    ENTER_BUTTON = (By.CLASS_NAME, 'second-button')
    NEW_EMAIL_BUTTON = (By.CSS_SELECTOR, '.sidebar__header a')
    RECIPIENT_INPUT = (By.CSS_SELECTOR, '.head_container--3W05z input')
    RECIPIENT_EMAIL = 'testingtesting@mail.com'
    LETTER_BODY = (By.CSS_SELECTOR, '.cke_editable div')
    SOME_TEXT_TO_LETTER_BODY = 'sometextsometextsometextsometextsometextsometextsometextsometextsometextsometextsometextsometext'
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.compose-app__buttons .button2_primary')
    LAYER_SENT_PAGE = (By.CLASS_NAME, 'layer-sent-page')

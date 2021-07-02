import pytest
from selenium import webdriver


# фикстура открытия/закрытия браузера, а также проверка на этапе формирования ссылки, что подставляется верный параметр language
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()

    yield browser
    browser.quit()

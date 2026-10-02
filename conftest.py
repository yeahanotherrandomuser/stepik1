import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    # Добавляем параметр --language в командную строку pytest
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, es, fr, etc...")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение параметра --language
    user_language = request.config.getoption("language")
    
    if user_language is None:
        raise pytest.UsageError("--language option is required! Example: pytest --language=es test_items.py")
    
    print(f"\nstart chrome browser for test with locale: {user_language}..")
    
    # Настраиваем язык интерфейса для Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    driver = webdriver.Chrome(options=options)
    yield driver
    
    print("\nquit browser..")
    driver.quit()

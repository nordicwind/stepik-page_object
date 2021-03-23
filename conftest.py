import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    languages_list = ['es', 'fr', 'en', 'ru']
    if user_language in languages_list:
        print("\n...Start browser...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError(f"--language should be set and should be in {languages_list}")
    yield browser
    print("\n...Closing browser...")
    browser.quit()

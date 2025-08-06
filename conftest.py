from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from pages.auth_page import AuthPage
from data.data import Data
from data.urls import Urls
from pathlib import Path
import allure
import pytest
import config

@pytest.fixture
@allure.title("подключаем удаленный/локальный драйвер в зависимости от настройки конфига")
def driver():
    if config.driver:
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "128.0")
        options.set_capability("selenoid:options", {"enableVNC": True})
        options.set_capability("selenoid:options", {"enableVideo": False})

        driver = webdriver.Remote(command_executor='http://selenoid:4444/wd/hub', options=options)
    else:
        driver = webdriver.Chrome()

    yield driver
    driver.quit()
    
@pytest.fixture
@allure.title("Создание и авторизация пользователя")
def login_user(driver):
    driver.get(Urls.BASE_URL)
    page = AuthPage(driver)
    page.auth_with_valid_data()
    yield driver

    

@pytest.fixture
@allure.title("Получить картинку")
def recipe_path():
    path = Path(Data.RECIPE_PATH)
    if path.exists():
        return str(path.absolute())
    else:
        pytest.skip(f"Test image {path} not found")
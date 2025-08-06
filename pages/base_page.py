from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from data.urls import Urls
import allure

class BasePage:

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.URL_BASE = Urls.BASE_URL
        
    @allure.step("Открытие страницы")
    def open(self, suff=""):
        self.driver.get(self.URL_BASE + suff)
        
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.title("Дождаться кликабельности элемента {locator}")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться исчезновения элемента {locator}")
    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        self.wait_for_clickable(locator).click()
        
    @allure.step("Заполнить поле")
    def send_keys_to_element(self, locator, keys):
        self.wait_for_clickable(locator).send_keys(keys)
        
    @allure.step("Загрузить картинку")
    def upload_image(self, locator, recipe_path):
        element = self.find_element(locator)
        element.send_keys(recipe_path)
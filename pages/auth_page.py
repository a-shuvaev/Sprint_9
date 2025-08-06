from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from data.data import Data
import allure


class AuthPage(BasePage):

    @allure.step("Нажатие на кнопку логина")
    def click_login_button(self):
        self.click_element(LoginLocators.BUTTON_LOGIN)

    @allure.step("Ввод email")
    def enter_email(self):
        self.send_keys_to_element(LoginLocators.INPUT_EMAIL, Data.EMAIL_STATIC)

    @allure.step("Ввод пароля")
    def enter_password(self):
        self.send_keys_to_element(LoginLocators.INPUT_PASSWORD, Data.PASSWORD_STATIC)

    @allure.step("Нажатие на кнопку 'Войти'")
    def click_enter_button(self):
        self.click_element(LoginLocators.BUTTON_ENTER)

    @allure.step("Авторизация")
    def auth_with_valid_data(self):
        self.click_login_button()
        self.enter_email()
        self.enter_password()
        self.click_enter_button()

    @allure.step("Кнопка выхода видна")
    def exit_button_is_visible(self):
        return self.wait_for_visible(LoginLocators.BUTTON_EXIT)

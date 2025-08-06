from pages.base_page import BasePage
from locators.create_account_locators import CreateAccountLocators
from data.data import Data
import allure

class CreateAccountPage(BasePage):
    
    @allure.step("Нажатие на кнопку создания аккаунта в заголовке")
    def click_create_account_button_header(self):
        self.click_element(CreateAccountLocators.BUTTON_CREATE_ACCOUNT_HEADER)
        
    @allure.step("Заполнить поле имени")
    def enter_first_name(self):
        self.send_keys_to_element(CreateAccountLocators.INPUT_FIRST_NAME, Data.EMAIL)
        
    @allure.step("Заполнить поле фамилии")
    def enter_last_name(self):
        self.send_keys_to_element(CreateAccountLocators.INPUT_SECOND_NAME, Data.LAST_NAME)

    @allure.step("Заполнить поле имени пользователя")
    def enter_username(self):
        self.send_keys_to_element(CreateAccountLocators.INPUT_USERNAME, Data.USERNAME)
        
    @allure.step("Заполнить поле электронной почты")
    def enter_email(self):
        self.send_keys_to_element(CreateAccountLocators.INPUT_EMAIL, Data.EMAIL)
        
    @allure.step("Заполнить поле пароля")
    def enter_password(self):
        self.send_keys_to_element(CreateAccountLocators.INPUT_PASSWORD, Data.PASSWORD)
        
    @allure.step("Нажатие на кнопку создания аккаунта в форме")
    def click_create_account_button_form(self):
        self.click_element(CreateAccountLocators.BUTTON_CREATE_ACCOUNT_FORM)
        
    @allure.step("Регистрация пользователя")
    def register_user(self):
        self.click_create_account_button_header()
        self.enter_first_name()
        self.enter_last_name()
        self.enter_username()
        email = self.enter_email()
        password = self.enter_password()
        self.click_create_account_button_form()
        
        return email, password
        
    @allure.step("Форма авторизации видна")
    def auth_form_is_visible(self):
        return self.wait_for_visible(CreateAccountLocators.BUTTON_ENTER)
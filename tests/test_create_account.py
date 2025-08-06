from pages.create_account_page import CreateAccountPage
import allure

class TestCreateAccount:
    
    @allure.title("Проверка успешной регистрации")
    def test_create_account_with_valid_data(self, driver):
        page = CreateAccountPage(driver)
        page.open()
        page.click_create_account_button_header()
        page.enter_first_name()
        page.enter_last_name()
        page.enter_username()
        page.enter_email()
        page.enter_password()
        page.click_create_account_button_form()
        
        assert page.auth_form_is_visible()
        
from pages.auth_page import AuthPage
import allure

class TestAuth:
    
    @allure.title("Проверка успешной авторизации")
    def test_login_with_valid_data(self, driver):
        page = AuthPage(driver)
        page.open()
        page.auth_with_valid_data()
        
        assert page.exit_button_is_visible()
        
        
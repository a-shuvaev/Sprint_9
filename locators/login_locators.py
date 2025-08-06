from selenium.webdriver.common.by import By

class LoginLocators:
    
    BUTTON_LOGIN = (By.XPATH, "//*[@href='/signin']")
    BUTTON_ENTER = (By.XPATH, "//button[contains(@class, 'style_button_style_dark-blue__1cpq7') and text()='Войти']")
    BUTTON_EXIT = (By.XPATH, "//a[contains(@class, 'styles_menuLink__3a59I') and text()='Выход']")
    
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    
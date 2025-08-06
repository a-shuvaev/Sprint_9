from selenium.webdriver.common.by import By

class CreateAccountLocators:
    
    BUTTON_CREATE_ACCOUNT_HEADER = (By.XPATH, "//*[@href='/signup']")
    BUTTON_CREATE_ACCOUNT_FORM = (By.CSS_SELECTOR, "button.style_button__1FFWl.styles_button__146Sy.style_button_style_dark-blue__1cpq7")
    BUTTON_ENTER = (By.XPATH, "//button[contains(@class, 'style_button_style_dark-blue__1cpq7') and text()='Войти']")
    
    INPUT_FIRST_NAME = (By.NAME, "first_name")
    INPUT_SECOND_NAME = (By.NAME, "last_name")
    INPUT_USERNAME = (By.NAME, "username")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    
    FORM_AUTHORIZATION = (By.XPATH, "//button[contains(@class, 'styles_form__2nwxz styles_form__2_42b')]")
from selenium.webdriver.common.by import By

class CreateRecipeLocators:
    
    BUTTON_CREATE_RECIPE_HEADER = (By.XPATH, "//a[contains(@class, 'style_nav__link__2rAY6') and text()='Создать рецепт']")
    BUTTON_CREATE_RECIPE_FORM = (By.XPATH, "//button[contains(@class, 'style_button__1FFWl') and text()='Создать рецепт']")
    BUTTON_ADD_INGREDIENT = (By.XPATH, ".//div[text()='Добавить ингредиент']")
    BUTTON_ADD_TO_CART = (By.XPATH, ".//*[text()=' Добавить в покупки']")
    
    INPUT_RECIPE_NAME = (By.XPATH, "//div[contains(@class, 'styles_inputLabelText__WsyhD') and text()='Название рецепта']/following-sibling::input")
    INPUT_INGREDIENT_NAME = (By.XPATH, "//input[contains(@class, 'styles_inputField__3eqTj') and contains(@class, 'styles_ingredientsInput__1zzql')]")
    INPUT_INGREDIENT_WEIGHT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    INPUT_RECIPE_TIME = (By.XPATH, "//div[contains(@class, 'cookingTimeLabel') and contains(text(), 'Время приготовления')]/following-sibling::input")
    INPUT_RECIPE_DESCRIPTION = (By.XPATH, ".//div[text()='Описание рецепта']/../textarea")
    
    UPLOAD_IMAGE = (By.CSS_SELECTOR, "input[type='file'].styles_fileInput__3HjP3")
    
    TITLE_RECIPE = (By.TAG_NAME, 'h1')
    
    DROPDOWN_INGREDIENT = (By.CSS_SELECTOR, "div.styles_container__3ukwm")
    OPTION_INGREDIENT = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div[contains(., 'огуречный рассол')]")
    
    
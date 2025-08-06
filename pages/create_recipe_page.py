from pages.base_page import BasePage
from locators.create_recipe import CreateRecipeLocators
from data.data import Data
import allure

class CreateRecipe(BasePage):
    
    @allure.step("Нажатие на кнопку создания рецепта в заголовке")
    def click_create_recipe_button_header(self):
        self.click_element(CreateRecipeLocators.BUTTON_CREATE_RECIPE_HEADER)
    
    @allure.step("Ввести название рецепта")
    def enter_recipe_title(self):
        self.send_keys_to_element(CreateRecipeLocators.INPUT_RECIPE_NAME, Data.RECIPE_TITLE)
        
    @allure.step("Выбор ингредиента")
    def choose_ingredient(self):
        self.send_keys_to_element(CreateRecipeLocators.INPUT_INGREDIENT_NAME, Data.INGREDIENT_NAME)
        self.click_element(CreateRecipeLocators.OPTION_INGREDIENT)
    
    @allure.step("Нажать на кнопку добавление ингредиента")
    def click_add_ingredient(self):
        self.click_element(CreateRecipeLocators.BUTTON_ADD_INGREDIENT)
        
    @allure.step("Ввести массу ингредиента")
    def enter_ingredient_weight(self):
        self.send_keys_to_element(CreateRecipeLocators.INPUT_INGREDIENT_WEIGHT, Data.INGREDIENT_WEIGHT)
        
    allure.step("Ввести время приготовления")
    def enter_recipe_time(self):
        self.send_keys_to_element(CreateRecipeLocators.INPUT_RECIPE_TIME, Data.COOKING_TIME)
        
    @allure.step("Добавить описание")
    def enter_description(self):
        self.send_keys_to_element(CreateRecipeLocators.INPUT_RECIPE_DESCRIPTION, Data.RECIPE_DESCRIPTION)
        
    @allure.step("Зазгрузить картинку")
    def upload_recipe_image(self, recipe_path):
        self.upload_image(CreateRecipeLocators.UPLOAD_IMAGE, recipe_path)
        
    @allure.step("Нажать на кнопку создания рецепта в форме")
    def click_create_recipe_button_form(self):
        self.click_element(CreateRecipeLocators.BUTTON_CREATE_RECIPE_FORM)
        
    @allure.step("Создание рецепта")
    def create_recipe(self, recipe_path):
        self.click_create_recipe_button_header()
        self.enter_recipe_title()
        self.choose_ingredient()
        self.enter_ingredient_weight()
        self.click_add_ingredient()
        self.enter_recipe_time()
        self.enter_description()
        self.upload_recipe_image(recipe_path)
        self.click_create_recipe_button_form()
        
    @allure.step("Получение название рецепта")
    def get_recipe_title(self):
        return self.find_element(CreateRecipeLocators.TITLE_RECIPE).text
    
    @allure.step("Проверка отображение кнопки добавления в корзину")
    def add_to_cart_button_is_visible(self):
        return self.wait_for_visible(CreateRecipeLocators.BUTTON_ADD_TO_CART)
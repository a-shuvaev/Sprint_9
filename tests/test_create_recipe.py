from pages.create_recipe_page import CreateRecipe
import allure

class TestCreateRecipe:
    
    @allure.title("Проверка создание рецепта")
    def test_create_recipe_with_valid_data(self, login_user, recipe_path):
        page = CreateRecipe(login_user)
        page.create_recipe(recipe_path)
        
        assert page.add_to_cart_button_is_visible()
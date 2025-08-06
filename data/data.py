from helpers.generator import Generator

class Data:
    
    EMAIL = Generator().generate_email()
    PASSWORD = Generator().generate_password()
    FIRST_NAME = Generator().generate_first_name()
    LAST_NAME = Generator().generate_last_name()
    USERNAME = Generator().generate_username()
    
    EMAIL_STATIC = "alexshuva@alexshuva.com"
    PASSWORD_STATIC = "1234qwer!@#$QWER"
    
    RECIPE_TITLE = f"Recipe_{Generator().generate_randomint()}"
    INGREDIENT_NAME = "огуречный рассол"
    INGREDIENT_WEIGHT = "750"
    COOKING_TIME = "5"
    RECIPE_DESCRIPTION = "Хорошо пить утром и вечером во время ..."
    
    RECIPE_PATH = "assets/image1.png"
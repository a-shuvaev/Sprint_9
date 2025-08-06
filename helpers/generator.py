from faker import Faker

class Generator:
    
    def __init__(self):
        self.fake = Faker()
    
    def generate_email(self):
        return self.fake.email(domain='alexshuva.com')
    
    def generate_password(self):
        return str(self.fake.password(length=8))
    
    def generate_first_name(self):
        return self.fake.first_name()
    
    def generate_last_name(self):
        return self.fake.last_name()
    
    def generate_username(self):
        return self.fake.user_name()
    
    def generate_randomint(self):
        return self.fake.random_number()
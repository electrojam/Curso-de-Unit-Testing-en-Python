import unittest, os

from faker import Faker
from src.user import User
from src.bank_account import BankAccount

class UserTests(unittest.TestCase):
    
    def setUp(self) -> None:    # cinfugración inicial de unittest
        self.faker = Faker(locale="es") #instanciamos Faker, e idioma de datos en español
        self.user = User(name=self.faker.name(), email=self.faker.email())

    def test_user_cration(self):    #prueba de creación de usuario con name y email
        name_faker = self.faker.name()  #generamos nombre fake
        email_faker = self.faker.email()    #generamos correo fake
        user = User(name=name_faker, email=email_faker) #creamos usuario
        self.assertEqual(user.name, name_faker) #probamos nombre usuario generado
        self.assertEqual(user.email, email_faker)   #probamos email usuario generado
    
    def test_user_with_multiple_accounts(self): #probamos creación de cuentas

        for _ in range(3):
            bank_account = BankAccount( #creamos buenta aleatoria
                balance = self.faker.random_int(min=100, max=2000, step=50),  #creamos balance aleatorio
                log_file = self.faker.file_name(extension=".txt")   #creamos log_file aleatorio
            )
            self.user.add_account(account=bank_account)  # agregamos cuenta al mismo user

        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value, expected_value)

    def tearDown(self) -> None: #cuadno acaben todas las pruebas, irá a cada cuenta creada y borrará cada log_file
        for account in self.user.accounts:
            os.remove(account.log_file)

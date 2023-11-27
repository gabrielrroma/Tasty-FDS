import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.SITE_LINK = "http://tastyflavorfusion.azurewebsites.net"  
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        self.driver.get(self.SITE_LINK)
        time.sleep(2)

        # Localize os campos de entrada de usuário e senha e preencha-os
        username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Usuário']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Senha']")
        login_button = self.driver.find_element(By.ID, 'faz-login')

        username_input.send_keys("seu_nome_de_usuário")  # Substitua pelo seu nome de usuário
        password_input.send_keys("sua_senha")  # Substitua pela sua senha
        login_button.click()

        time.sleep(5)  # Aguarde algum tempo para ver a página após o login

        # Verifique se você foi redirecionado para a página correta após o login
        self.assertEqual(self.driver.current_url, "https://tastyflavorfusion.azurewebsites.net/filter-recipe/")  # Substitua pela URL correta
    def tearDown(self):
        self.driver.quit()

    


class CadastroTest(unittest.TestCase):

    def setUp(self):
        self.SITE_LINK = "https://tastyflavorfusion.azurewebsites.net/cadastrar_usuario/"  # Substitua pela URL correta
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_cadastro(self):
        self.driver.get(self.SITE_LINK)
        time.sleep(2)

        # Localize os campos de entrada de nome, sobrenome, nome de usuário, senha e botões
        nome_input = self.driver.find_element(By.ID, "nome")
        sobrenome_input = self.driver.find_element(By.ID, "sobrenome")
        username_input = self.driver.find_element(By.ID, "username")
        senha_input = self.driver.find_element(By.ID, "senha")
        criar_conta_button = self.driver.find_element(By.ID, "criar-conta-button")
        cancelar_button = self.driver.find_element(By.ID, "cancelar-button")

        # Preencha os campos com informações de teste
        nome_input.send_keys("SeuNome")
        sobrenome_input.send_keys("SeuSobrenome")
        username_input.send_keys("NomeDeUsuario")
        senha_input.send_keys("SenhaDeTeste")

        # Clique no botão "Criar Conta"
        criar_conta_button.click()

        time.sleep(5)  # Aguarde algum tempo para ver a página após o clique

        # Verifique se você foi redirecionado para a página correta após o cadastro
        self.assertEqual(self.driver.current_url, "https://tastyflavorfusion.azurewebsites.net/filter-recipe/")  # Substitua pela URL correta

        # Você pode adicionar mais verificações conforme necessário, por exemplo, para verificar se os campos de culinária foram selecionados.

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

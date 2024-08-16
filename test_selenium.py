import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()  # Fecha o navegador após cada teste

    def test_user_login(self):
        # Acessa a página de login
        self.driver.get("https://biblioteca-on-line.onrender.com/login")
        # Aguarda um momento para garantir que a página carregou
        time.sleep(10)
        
        # Verifica se o texto "Login" está presente na página
        self.assertIn("Login", self.driver.page_source)
    # Verifica se "Lista de Livros" está na página

    def test_user_login(self):
        self.driver.get("https://biblioteca-on-line.onrender.com/login")  # Acessa a página de login
        time.sleep(1)

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("admin")  # Digita o nome de usuário
        time.sleep(3)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("senha123")
        time.sleep(3)

        # Digita a senha
        password_input.send_keys(
            Keys.RETURN
        )  # Simula o Enter para submeter o formulário
        time.sleep(5)

        self.driver.get("https://biblioteca-on-line.onrender.com/novo")
        titulo = self.driver.find_element(By.NAME,"titulo")
        titulo.send_keys("Código limpo")
        time.sleep(2)

        autor = self.driver.find_element(By.NAME, "autor")
        autor.send_keys("Iton Carlos")
        time.sleep(2)

        categoria = self.driver.find_element(By.NAME, "categoria")
        categoria.send_keys("Desenvolvimento de Software")
        time.sleep(2)

        ano = self.driver.find_element(By.NAME, "ano")
        ano.send_keys("2024")
        time.sleep(2)

        editora = self.driver.find_element(By.NAME, "editora")
        editora.send_keys("Editora Exemplo")
        time.sleep(2)

        # 5. Clica no botão "Salvar"
        save_button = self.driver.find_element(By.XPATH, "//button[text()='Salvar']")
        save_button.click()

       


if __name__ == "__main__":
    unittest.main()
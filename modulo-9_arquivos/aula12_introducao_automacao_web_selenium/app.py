import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.chdir('modulo-9_arquivos')
os.chdir('aula12_introducao_automacao_web_selenium')

# Cria o navegador webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')
# Navega até o site
driver.get('https://automatize.netlify.app')
# Econtrar elementos
input_email = driver.find_element(By.ID, 'email')
input_senha = driver.find_element(By.XPATH, "//input[@name='campoSenha']")
button_enviar = driver.find_element(By.XPATH, "//button[text()='Enviar']")
# Interagir com eles digitando ou clicando
input_email.send_keys('andrei.ric@hotmail.com')
input_senha.send_keys('123456')
button_enviar.click()

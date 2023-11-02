from selenium import webdriver

#Webdriver vai verificar a versão do navegado
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Webdriver vai verificar a versão do navegado
servico = Service(ChromeDriverManager().install())
#usar o chrome
navegador = webdriver.Chrome(service=servico)

#Entrar no navegado
navegador.get("https://sso.acesso.gov.br/login?client_id=5b1db4fd-87e7-4689-9c37-faa2a5663c6c&authorization_id=18b910c0020")

#Encontrar o Elemento pegar xpath onde vai colocar os dados
navegador.find_element('xpath','//*[@id="accountId"]').send_keys("12345678978")

#Vai clicar no botão para entrar
navegador.find_element('xpath','//*[@id="login-button-panel"]/button').click()
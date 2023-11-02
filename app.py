from selenium import webdriver

#Webdriver vai verificar a versão do navegado
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Webdriver vai verificar a versão do navegado
servico = Service(ChromeDriverManager().install())
#usar o chrome
navegador = webdriver.Chrome(service=servico)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

search_text = input('Digite Sua pesquisa: ')

#nav = webdriver.Chrome()

#---------------- esconder o navegador
options = webdriver.ChromeOptions()
options.add_argument("--headless")
nav = webdriver.Chrome(options=options)
#-------------------------------------

nav.get('https://www.google.com/')
nav.find_element(By.NAME, 'q').send_keys(search_text)
time.sleep(1) 
nav.find_element(By.NAME, 'btnK').click()

degrees = nav.find_element(By.ID, 'wob_tm').text
rain = nav.find_element(By.ID, 'wob_pp').text
moisture = nav.find_element(By.ID, 'wob_hm').text
wind = nav.find_element(By.ID, 'wob_ws').text
place = nav.find_element(By.ID, 'wob_loc').text
day = nav.find_element(By.ID, 'wob_dts').text
weather = nav.find_element(By.ID, 'wob_dcp').text
nav.quit()

print('Temperatura: {}\nChuva: {}%\nUmidade: {}%\nVento: {}%\n\nLocal: {}\nDia: {}\nTempo: {}'.format(degrees, rain,moisture,wind,place,day,weather))
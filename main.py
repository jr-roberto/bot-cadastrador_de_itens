from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from cadastrar_itens import ler_arquivo_csv, registro
import time

bot = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
bot.get('http://192.168.1.9:5000')

# Mapeando itens da tela
xpath_sel_grupo = '//*[@id="item_grupo"]'
xpath_tex_cod_item = '//*[@id="item_cod"]'
xpath_tex_desc = '//*[@id="item_desc"]'
xpath_tex_item_estoque = '//*[@id="item_estoque"]'
xpath_tex_fabricante = '//*[@id="item_fabric"]'
xpath_select_laudo = '//*[@id="item_laudo"]'
xpath_btn_cadastrar = '/html/body/main/form/input[5]'

lista_itens = ler_arquivo_csv()

for i in lista_itens:
    
    # 1 - Selecionar GRUPO
    select = bot.find_element(By.XPATH,xpath_sel_grupo)
    options = select.find_elements(By.TAG_NAME,'option')

    for opt in options:
        value = opt.text
        if value == i.grupo:
            opt.click()
            break

    # 2 - Digitar cod item
    input_text = bot.find_element(By.XPATH,xpath_tex_cod_item)
    input_text.send_keys(i.cod_item)

    # 3 - Digitando a descricao
    input_text = bot.find_element(By.XPATH,xpath_tex_desc)
    input_text.send_keys(i.descricao)

    # 4 - Digitando a local estoque
    input_text = bot.find_element(By.XPATH,xpath_tex_item_estoque)
    input_text.send_keys(i.local_estoque)

    # 5 - Digitando a Fabricante
    input_text = bot.find_element(By.XPATH,xpath_tex_fabricante)
    input_text.send_keys(i.fabricante)

    # 6 - Selecionar LAUDO (Sim ou Nao)
    select = bot.find_element(By.XPATH,xpath_select_laudo)
    options = select.find_elements(By.TAG_NAME,'option')

    for opt in options:
        value = opt.text
        if value == i.laudo:
            opt.click()
            break

    # Clicando em cadastrar
    input_btn = bot.find_element(By.XPATH,xpath_btn_cadastrar)
    input_btn.click()

    descricao = i.descricao

    # Finalizando o cadastro
    while True:
        i = bot.find_elements(By.XPATH,'//*[@id="popup"]/div/div/button') 

        if i.__len__() > 0:
            cod_item_gerado = bot.find_element(By.XPATH,'//*[@id="cod_item_gerado"]').text
            
            i[0].click()

            registro(descricao,cod_item=cod_item_gerado)
            
            break

print('Finalizado')

time.sleep(3)
bot.quit()
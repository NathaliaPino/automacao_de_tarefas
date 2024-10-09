# 1 passo: abrir o google
# 2 passo: digitar o site na aba e clicar em enter
# 3 passo: fazer o login e clicar em logar
# 4 passo: importar a base de dados
# 5 passo: cadastrar um produto em looping e clicar em enviar
# 6 passo: repetir o processo até acabar todos os produtos


# 1 passo:abrir o google

# pip install pyautogui

import pyautogui as pg
import time

    # pyautogui.write -> escrever um texto
    # pyautogui.press -> apertar 1 tecla do teclado
    # pyautogui.click -> clicar em algum lugar da tela
    # pyautogui.hotkey -> combinação de teclas
    # pyautogui.position -> pega a posição na tela


pg.PAUSE = 0.5

pg.press("win")
pg.write("chrome")
pg.press("enter")

time.sleep(1)
pg.click(x=303, y=645)



# 2 passo: digitar o site na aba e clicar em enter

pg.click(x=630, y=68)
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")
time.sleep(2)



# 3 passo: fazer o login e clicar em logar

email = "emailteste@gmai.com"
senha = "senhaqualquer"

pg.click(x=550, y=373)
pg.write(email)
pg.press("tab")
pg.write(senha)
pg.press("tab")
pg.press("enter")


# 4 passo: importar a base de dados

import pandas as pd

tabela = pd.read_csv("produtos.csv")



# 5 passo: cadastrar um produto em looping e clicar em enviar


for linha in tabela.index:
    
    # Código do Produto
    pg.click(x=552, y=257)  # Clique no campo do código do produto
    pg.hotkey("ctrl", "a")  # Seleciona todo o texto no campo
    pg.press("backspace")   # Apaga o texto selecionado
    codigo = tabela.loc[linha, "codigo"]  # Pega o valor do código na tabela
    pg.write(str(codigo))   # Escreve o novo código
    pg.press("tab")         # Avança para o próximo campo
    
    # Marca do Produto
    pg.hotkey("ctrl", "a")  # Seleciona todo o texto no campo
    pg.press("backspace")   # Apaga o texto selecionado
    marca = tabela.loc[linha, "marca"]  # Pega o valor da marca na tabela
    pg.write(str(marca))    # Escreve a nova marca
    pg.press("tab")         # Avança para o próximo campo

    # Tipo do Produto
    pg.hotkey("ctrl", "a")  # Seleciona todo o texto no campo
    pg.press("backspace")   # Apaga o texto selecionado
    tipo = tabela.loc[linha, "tipo"]  # Pega o valor do tipo na tabela
    pg.write(str(tipo))     # Escreve o novo tipo
    pg.press("tab")         # Avança para o próximo campo

    # Categoria do Produto
    pg.hotkey("ctrl", "a")  # Seleciona todo o texto no campo
    pg.press("backspace")   # Apaga o texto selecionado
    categoria = tabela.loc[linha, "categoria"]  # Pega o valor da categoria
    pg.write(str(categoria))  # Escreve a nova categoria
    pg.press("tab")         # Avança para o próximo campo

    # Preço Unitário do Produto
    pg.hotkey("ctrl", "a")  # Seleciona todo o texto no campo
    pg.press("backspace")   # Apaga o texto selecionado
    preco = tabela.loc[linha, "preco_unitario"]  # Pega o preço unitário
    pg.write(str(preco))    # Escreve o novo preço
    pg.press("tab")         # Avança para o próximo campo

    # Custo do Produto
    pg.hotkey("ctrl", "a")  # Seleciona todo o texto no campo
    pg.press("backspace")   # Apaga o texto selecionado
    custo = tabela.loc[linha, "custo"]  # Pega o custo do produto
    pg.write(str(custo))    # Escreve o novo custo
    pg.press("tab")         # Avança para o próximo campo

    # OBS (apenas se houver algo para escrever)
    pg.hotkey("ctrl", "a")  # Seleciona todo o texto no campo
    pg.press("backspace")   # Apaga o texto selecionado
    obs = tabela.loc[linha, "obs"]  # Pega a observação, se houver
    if pd.notna(obs):
        pg.write(str(obs))  # Escreve a observação, se existir
    
    pg.press("tab")
    pg.press("enter")  # Envia o formulário

    # Scroll para o topo (se necessário)
    pg.scroll(5000)




        

















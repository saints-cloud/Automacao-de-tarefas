"""link do sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
passo 1: abrir o sistema da empresa
passo 2: fazer o login
passo 3: importar a base de dados dos produtos
passo 4: cadastrar um produto
passo 5: repetir o passo quatro até acabar todos os produtos"""

import pyautogui, time, pandas, openpyxl

pyautogui.PAUSE = 0.5


# Pressionar a tecla Windows
pyautogui.press("win")
time.sleep(0.7)  # Espera para o menu iniciar aparecer

# Digitar "edge"
pyautogui.write("edge", interval=0.1)
time.sleep(0.7)  # Espera para garantir que o texto foi escrito

# Pressionar Enter
pyautogui.press("enter")
time.sleep(0.7)

# Digitar o link do site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login", interval=0.1)
time.sleep(0.7)

# Pressionar Enter
pyautogui.press("enter")
time.sleep(0.7)

######## FAZENDO O LOGIN
pyautogui.click(x=649, y=455)
pyautogui.write("pinheiro.lays01@gmail.com")
time.sleep(0.5)

pyautogui.press("tab")
pyautogui.write("euamooflashinho", interval=0.05)

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(0.5)

#### IMPORTAR BASE DE DADOS
tabela = pandas.read_csv("produtos.csv")
print(tabela)
time.sleep(2)

#### CADASTRAR UM PRODUTO
for linha in tabela.index:
    pyautogui.click(x=607, y=302)
    
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")

    
    pyautogui.scroll(10000)
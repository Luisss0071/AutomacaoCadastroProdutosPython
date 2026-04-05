import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.5 # Cria um intervalo 0.5 segundos entre cada interação do pyautogui 

# Passo 1: Entrar no sistema da empresa 

link_site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "login123@gmail.com"
senha = "senha_dificil098"
navegador = "google chrome"

# Entrar no navegador
pyautogui.press("win")
pyautogui.write(navegador)
pyautogui.press("enter")
time.sleep(5) # Pause o Código por 5 segundos

# Entrar no sistema


pyautogui.write(link_site)
pyautogui.press("enter")
time.sleep(5)

# Passo 2: Logar no sistema da empresa

pyautogui.click(x=964, y=360) # Clicar no campo de email
pyautogui.write(email)
pyautogui.press("tab") # Passar para o próximo campo (SENHA)
pyautogui.write(senha)
pyautogui.press("tab") # Passa para o campo de LOGAR
pyautogui.press("enter")
time.sleep(5)

# Passo 3: Importar a base de dados

produtos_df = pd.read_csv("produtos.csv")

# Passo 4: Cadastrar Produtos

pyautogui.PAUSE = 0.1

pyautogui.click(x=955, y=245)

for linha in produtos_df.index:
    
    pyautogui.click(x=955, y=245)

    codigo = produtos_df.loc[linha, "codigo"] # Localiza a linha de código
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = produtos_df.loc[linha, "marca"] # Localiza a linha da marca
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = produtos_df.loc[linha, "tipo"] # Localiza a linha do tipo 
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = produtos_df.loc[linha, "categoria"] # Localiza a linha da categoria
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = produtos_df.loc[linha, "preco_unitario"] # Localiza a linha da preço unitário
    pyautogui.write(str(preco_unitario)) # "str" converte número para string(texto)
    pyautogui.press("tab")

    custo = produtos_df.loc[linha, "custo"] # Localiza a linha do custo
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = produtos_df.loc[linha, "obs"] # Localiza a linha de Observação
    if not pd.isna(obs):
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    
    pyautogui.scroll(5000)
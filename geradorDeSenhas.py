# Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
import random

def gerarSenha():
    # Definindo caracteres que podem estar na senha
    numeros = "1234567890"
    letrasMinusculas = "abcdefghijklmnopqrstuvwxyz"
    letrasMaiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caracteresEspeciais = "@#$%&!"

    count = 0

    # Se o tamanho da senha não for informado, o programa exibe uma mensagem de erro
    if (numero.get() == ""):
        messagebox.showinfo ("Erro", "Digite o tamanho da senha desejada.")
        return

    tamanho = int(numero.get())

    senha = ""

    # Garante que haverá pelo menos um caractere do tipo selecionado na senha gerada
    senhaObrigatoria = []

    if (checkVar1.get() == 1):
        senha = numeros
        senhaObrigatoria.append(random.choice(numeros))
    # Faz a contagem de quantas checkboxes não foram marcadas
    else:
        count += 1

    if (checkVar2.get() == 1):
        senha += letrasMinusculas
        senhaObrigatoria.append(random.choice(letrasMinusculas))
    else:
        count += 1

    if (checkVar3.get() == 1):
        senha += letrasMaiusculas
        senhaObrigatoria.append(random.choice(letrasMaiusculas))
    else:
        count += 1

    if (checkVar4.get() == 1):
        senha += caracteresEspeciais
        senhaObrigatoria.append(random.choice(caracteresEspeciais))
    else:
        count += 1

    # Se count = 4 (todas as checkboxes não foram marcadas), exibe uma mensagem de erro
    if (count == 4):
        messagebox.showinfo ("Erro", "Selecione pelo menos um tipo de caractere.")
        return 

    # Se o tamanho de senha desejado for menor que o número de caracteres que ela deve ter,
    # o programa exibe uma mensagem de erro
    if (tamanho < len(senhaObrigatoria)):
        messagebox.showinfo ("Erro", "Tamanho insuficiente para incluir todos os tipos de caracteres.")
        return

    # Inclui os caracteres obrigatórios + a quantidade que falta para completar a senha
    senhaOficial = senhaObrigatoria + [random.choice(senha) for _ in range (tamanho - len(senhaObrigatoria))]
    # Embaralha para que os elementos obrigatórios não fiquem em ordem no começo da senha
    random.shuffle(senhaOficial)

    global senhaFinal

    senhaFinal = "".join(senhaOficial)
    exibeSenha["text"] = senhaFinal


def copiaSenha ():
    janela.clipboard_clear()
    janela.clipboard_append(senhaFinal)

    messagebox.showinfo ("", "Senha copiada com sucesso!")


# Interface gráfica do programa
janela = Tk()
janela.title("Gerador de senhas")
janela.geometry("315x383")
janela.configure(background = "#DFE9F5")

janela.columnconfigure (0, weight = 1)
janela.rowconfigure (0, weight = 1)

primeiroContainer = Frame (janela, bg = "#DFE9F5")
primeiroContainer.grid (row = 0, column = 0, sticky = "nsew", padx = 10, pady = 5)

segundoContainer = Frame (janela, bg = "#DFE9F5")
segundoContainer.grid (row = 1, column = 0, sticky = "nsew", padx = 10)

numeroLabel = Label(primeiroContainer, text = "Quantos caracteres a sua senha deve ter?", font = ("Arial", 12), 
                    wraplength = 300, justify = LEFT, background = "#DFE9F5")
numeroLabel.grid (row = 0, column = 0, sticky = "w", pady = 5)

numero = Entry (primeiroContainer, font = ("Arial", 11))
numero.grid (row = 1, column = 0, sticky = "ew", pady = 5)

checkboxLabel = Label(segundoContainer, text = "Selecione quais tipos de caracteres a sua senha deve ter", 
                      font = ("Arial", 12), wraplength = 300, anchor = "w", justify = LEFT, background = "#DFE9F5")
checkboxLabel.grid (row = 0, column = 0, sticky = "w", pady = 2)

checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()
checkVar4 = IntVar()

checkboxNumero = Checkbutton(segundoContainer, text = "Números (123)", font = ("Arial", 11), 
                             variable = checkVar1, background = "#DFE9F5")
checkboxNumero.grid (row = 1, column = 0, sticky = "w", pady = 1)

checkboxLetrasMinusculas = Checkbutton(segundoContainer, text = "Letras minúsculas (abc)", 
                                       font = ("Arial", 11), variable = checkVar2, background = "#DFE9F5")
checkboxLetrasMinusculas.grid (row = 2, column = 0, sticky = "w", pady = 1)

checkboxLetrasMaiusculas = Checkbutton(segundoContainer, text = "Letras maiúsculas (ABC)", 
                                       font = ("Arial", 11), variable = checkVar3, background = "#DFE9F5")
checkboxLetrasMaiusculas.grid (row = 3, column = 0, sticky = "w", pady = 1)

checkboxCaracteresEspeciais = Checkbutton(segundoContainer, text = "Caracteres especiais (!@#)", 
                                          font = ("Arial", 11), variable = checkVar4, background = "#DFE9F5")
checkboxCaracteresEspeciais.grid (row = 4, column = 0, sticky = "w", pady = 1)

gerarSenha = Button (janela, text = "GERAR SENHA", width = 12, height = 2, font = ("Arial", 12, "bold"), 
                     command = gerarSenha, bg = "#2C5D84", fg = "white")
gerarSenha.grid (row = 5, column = 0, sticky = "nsew", pady = 1)

exibeSenha = Label (janela, text = "", width = 12, height = 2, font = ("Arial", 12))
exibeSenha.grid (row = 6, column = 0, sticky = "nsew", pady = 1)

gerarSenha = Button (janela, text = "COPIAR SENHA", width = 12, height = 2, font = ("Arial", 10, "bold"), 
                     command = copiaSenha, bg = "#4682B4", fg = "white")
gerarSenha.grid (row = 7, column = 0, sticky = "nsew", pady = 1)

janela.mainloop()
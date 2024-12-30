#importando a biblioteca tkinter
from tkinter import *
from tkinter import messagebox
import random

def gerarSenha():
    numeros = "1234567890"
    letrasMinusculas = "abcdefghijklmnopqrstuvwxyz"
    letrasMaiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caracteresEspeciais = "@#$%&!"

    tamanho = int(numero.get())

    senha = ""

    senhaObrigatoria = []

    if (check_var1.get() == 1):
        senha = numeros
        senhaObrigatoria.append(random.choice(numeros))

    if (check_var2.get() == 1):
        senha += letrasMinusculas
        senhaObrigatoria.append(random.choice(letrasMinusculas))

    if (check_var3.get() == 1):
        senha += letrasMaiusculas
        senhaObrigatoria.append(random.choice(letrasMaiusculas))

    if (check_var4.get() == 1):
        senha += caracteresEspeciais
        senhaObrigatoria.append(random.choice(caracteresEspeciais))

    if (tamanho < len(senhaObrigatoria)):
        messagebox.showinfo ("Erro", "Tamanho insuficiente para incluir todos os tipos de caracteres.")
        return

    senhaOficial = senhaObrigatoria + [random.choice(senha) for _ in range (tamanho - len(senhaObrigatoria))]
    
    global senhaFinal

    senhaFinal = "".join(senhaOficial)
    exibeSenha["text"] = senhaFinal


def copiaSenha ():
    janela.clipboard_clear()
    janela.clipboard_append(senhaFinal)

    messagebox.showinfo ("", "Senha copiada com sucesso!")


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

check_var1 = IntVar()
check_var2 = IntVar()
check_var3 = IntVar()
check_var4 = IntVar()

checkboxNumero = Checkbutton(segundoContainer, text = "Números (123)", font = ("Arial", 11), 
                             variable = check_var1, background = "#DFE9F5")
checkboxNumero.grid (row = 1, column = 0, sticky = "w", pady = 1)

checkboxLetrasMinusculas = Checkbutton(segundoContainer, text = "Letras minúsculas (abc)", 
                                       font = ("Arial", 11), variable = check_var2, background = "#DFE9F5")
checkboxLetrasMinusculas.grid (row = 2, column = 0, sticky = "w", pady = 1)

checkboxLetrasMaiusculas = Checkbutton(segundoContainer, text = "Letras maiúsculas (ABC)", 
                                       font = ("Arial", 11), variable = check_var3, background = "#DFE9F5")
checkboxLetrasMaiusculas.grid (row = 3, column = 0, sticky = "w", pady = 1)

checkboxCaracteresEspeciais = Checkbutton(segundoContainer, text = "Caracteres especiais (!@#)", 
                                          font = ("Arial", 11), variable = check_var4, background = "#DFE9F5")
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
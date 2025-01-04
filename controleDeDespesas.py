from tkinter import *

def adiciona ():
    adicionarJanela = Toplevel()
    adicionarJanela.title ("Adicionar despesa")
    adicionarJanela.geometry ("300x200")

    adicionarJanela.columnconfigure (0, weight = 1)
    adicionarJanela.rowconfigure (0, weight = 1)

    descricaoLabel = Label (adicionarJanela, text = "Digite uma breve descrição da despesa", font = ("Arial", 12))
    descricaoLabel.grid (row = 0, column = 0, sticky = "nsew", pady = 5)

    descricaoDespesa = Entry (adicionarJanela, font = ("Arial", 11))
    descricaoDespesa.grid (row = 1, column = 0, sticky = "nsew", pady = 5)

    valorLabel = Label (adicionarJanela, text = "Digite o valor da despesa", font = ("Arial", 12))
    valorLabel.grid (row = 2, column = 0, sticky = "nsew", pady = 5)

    valorDespesa = Entry (adicionarJanela, font = ("Arial", 11))
    valorDespesa.grid (row = 3, column = 0, sticky = "nsew", pady = 5)


    #chamar método para adicionar
    submeterDespesa = Button (adicionarJanela, text = "Adicionar", font = ("Arial", 12))
    submeterDespesa.grid (row = 4, column = 0, sticky = "nsew", pady = 0)

    fecharDespesa = Button (adicionarJanela, text = "Fechar", font = ("Arial", 12), command = adicionarJanela.destroy)
    fecharDespesa.grid (row = 5, column = 0, sticky = "nsew", pady = 0)



janela = Tk()
janela.title ("Controle de despesas")
janela.geometry ("300x200")

janela.columnconfigure (0, weight = 1)
janela.rowconfigure (0, weight = 1)

primeiroContainer = Frame (janela)
primeiroContainer.grid (row = 0, column = 0, sticky = "nsew", padx = 10, pady = 10)

primeiroContainer.columnconfigure (0, weight = 1)
primeiroContainer.rowconfigure (0, weight = 1)

segundoContainer = Frame (janela)
segundoContainer.grid (row = 1, column = 0, sticky = "nsew", padx = 10)

segundoContainer.columnconfigure (0, weight = 1)
segundoContainer.rowconfigure (0, weight = 1)


welcomeLabel = Label (primeiroContainer, text = "SEJA BEM-VINDO(A)",  font = ("Arial", 12, "bold"))
welcomeLabel.grid (row = 0, column = 0, sticky = "nsew", pady = 5)

acaoLabel = Label (segundoContainer, text = "O que você deseja fazer?", font = ("Arial", 12))
acaoLabel.grid (row = 0, column = 0, sticky = "nsew", pady = 10)

adicionarDespesa = Button (janela, text = "Adicionar despesa", font = ("Arial", 12), command = adiciona)
adicionarDespesa.grid (row = 5, column = 0, sticky = "nsew", pady = 1)

exibirDespesas = Button (janela, text = "Exibir despesas", font = ("Arial", 12))
exibirDespesas.grid (row = 10, column = 0, sticky = "nsew", pady = 1)

exibirTotal = Button (janela, text = "Exibir total gasto", font = ("Arial", 12))
exibirTotal.grid (row = 15, column = 0, sticky = "nsew", pady = 1)

janela.mainloop()
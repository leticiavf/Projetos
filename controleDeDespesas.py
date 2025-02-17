# Importando as bibliotecas
from tkinter import *
from tkinter import messagebox

# Criando a lista de despesas como uma variável global
despesas = []

# Função que adiciona uma despesa à lista de acordo com as entradas fornecidas
def adiciona ():
    descricao = descricaoDespesa.get()
    valor = valorDespesa.get()

    if not descricao or not valor:
        messagebox.showinfo ("Erro", "Preencha os dois campos!")
        return
    
    valor = float(valor)

    despesas.append ({"descricaoDespesa": descricao, "valorDespesa": valor})

    messagebox.showinfo ("", "Despesa armazenada com sucesso!")


# Cria nova janela para a adição de despesas, armazenando as entradas e criando botões
def janelaAdiciona ():
    adicionarJanela = Toplevel()
    adicionarJanela.title ("Adicionar despesas")
    adicionarJanela.geometry ("300x200")

    adicionarJanela.columnconfigure (0, weight = 1)
    adicionarJanela.rowconfigure (0, weight = 1)

    global descricaoDespesa, valorDespesa

    descricaoLabel = Label (adicionarJanela, text = "Digite uma breve descrição da despesa", font = ("Arial", 12))
    descricaoLabel.grid (row = 0, column = 0, sticky = "w", pady = 5)

    descricaoDespesa = Entry (adicionarJanela, font = ("Arial", 11))
    descricaoDespesa.grid (row = 1, column = 0, sticky = "nsew", pady = 5)

    valorLabel = Label (adicionarJanela, text = "Digite o valor da despesa", font = ("Arial", 12))
    valorLabel.grid (row = 2, column = 0, sticky = "w", pady = 5)

    valorDespesa = Entry (adicionarJanela, font = ("Arial", 11))
    valorDespesa.grid (row = 3, column = 0, sticky = "nsew", pady = 5)

    submeterDespesa = Button (adicionarJanela, text = "Adicionar", font = ("Arial", 12), command = adiciona, bg = "#a7cd2c")
    submeterDespesa.grid (row = 4, column = 0, sticky = "nsew", pady = 0)

    fecharDespesa = Button (adicionarJanela, text = "Fechar", font = ("Arial", 12), command = adicionarJanela.destroy, bg = "#f65456")
    fecharDespesa.grid (row = 5, column = 0, sticky = "nsew", pady = 0)


# Cria nova janela para exibir as despesas
def janelaExibe ():
    exibirJanela = Toplevel()
    exibirJanela.title ("Exibir despesas")
    exibirJanela.geometry ("300x200")

    exibirJanela.columnconfigure (0, weight = 1)
    exibirJanela.rowconfigure (0, weight = 1)

    terceiroContainer = Frame (exibirJanela)
    terceiroContainer.grid (row = 0, column = 0, sticky = "nsew")

    terceiroContainer.columnconfigure (0, weight = 1)
    terceiroContainer.rowconfigure (0, weight = 1)

    quartoContainer = Frame (exibirJanela, bg = "#ffffff")
    quartoContainer.grid (row = 1, column = 0, sticky = "nsew", padx = 20, pady = 20)

    quartoContainer.columnconfigure (0, weight = 1)
    quartoContainer.rowconfigure (0, weight = 1)

    descricaoLabel = Label (terceiroContainer, text = "Aqui estão todas as suas despesas:", font = ("Arial", 12, "bold"), bg = "#cee891")
    descricaoLabel.grid (row = 0, column = 0, sticky = "nsew")

    if not despesas:
        messagebox.showinfo ("Erro", "Você ainda não armazenou nenhuma despesa.")
        return
    
    for i, despesa in enumerate (despesas, start = 1):
        texto = f"{i}. {despesa['descricaoDespesa']} - R$ {despesa['valorDespesa']:.2f}"
        exibeDespesas = Label(quartoContainer, text = texto, font = ("Arial", 12), bg = "#ffffff")
        exibeDespesas.grid (row = i, column = 0, sticky = "w")

# Soma todas as despesas e exibe o total gasto
def total():
    if not despesas:
        messagebox.showinfo ("Erro", "Você ainda não armazenou nenhuma despesa.")
        return

    totalDespesas = sum (despesa['valorDespesa'] for despesa in despesas)
    messagebox.showinfo ("Total gasto", f"O total gasto é de R${totalDespesas:.2f}")


# Parte considerável da interface gráfica do programa
janela = Tk()
janela.title ("Controle de despesas")
janela.geometry ("300x200")
janela.configure (background = "#ffffff")

janela.columnconfigure (0, weight = 1)
janela.rowconfigure (0, weight = 1)

primeiroContainer = Frame (janela, bg = "#ffffff")
primeiroContainer.grid (row = 0, column = 0, sticky = "nsew", padx = 20, pady = 20)

primeiroContainer.columnconfigure (0, weight = 1)
primeiroContainer.rowconfigure (0, weight = 1)

segundoContainer = Frame (janela)
segundoContainer.grid (row = 1, column = 0, sticky = "nsew")

segundoContainer.columnconfigure (0, weight = 1)
segundoContainer.rowconfigure (0, weight = 1)

welcomeLabel = Label (primeiroContainer, text = "SEJA BEM-VINDO(A)",  font = ("Arial", 12, "bold"), bg = "#ffffff")
welcomeLabel.grid (row = 0, column = 0, sticky = "nsew", pady = 5)

acaoLabel = Label (segundoContainer, text = "O que você deseja fazer?", font = ("Arial", 12))
acaoLabel.grid (row = 0, column = 0, sticky = "nsew", pady = 5)

adicionarDespesa = Button (janela, text = "Adicionar despesas", font = ("Arial", 12), command = janelaAdiciona, bg = "#bada5f")
adicionarDespesa.grid (row = 5, column = 0, sticky = "nsew", pady = 1)

exibirDespesas = Button (janela, text = "Exibir despesas", font = ("Arial", 12), command = janelaExibe, bg = "#bada5f")
exibirDespesas.grid (row = 10, column = 0, sticky = "nsew", pady = 1)

exibirTotal = Button (janela, text = "Exibir total gasto", font = ("Arial", 12), command = total, bg = "#bada5f")
exibirTotal.grid (row = 15, column = 0, sticky = "nsew", pady = 1)

janela.mainloop()
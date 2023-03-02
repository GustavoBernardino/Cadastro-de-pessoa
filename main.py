from tkinter import *


janela = Tk()
janela.title("Cadastro de Pessoa ")
janela.geometry('500x500')


# funçao obter
def obter():

    nome = str(enntry_nome.get())
    dn = enntry_dn.get()
    mae = enntry_nome_mae.get()
    cpf = enntry_cpf.get()
    rg = enntry_rg.get()

    flag = True
    flog = True
    tam_cpf = 14
    tam_date = 10
    tam_rg = 8


    #Verificando Tamanho do RG
    if (len(rg) != tam_rg):
        print("RG Inválido")
    else:
        print("RG Válido")

      
    #Verificando Tamanho da Data de Nascimento com barras
    if (len(dn) != tam_date):
        flog = False
    elif ((dn[2] != "/") or (dn[5] != "/")):
        flog = False
    else:
        for i in range(tam_date):
            if (i != 2) and (i != 5):
                d = dn[i]
                if (not d.isdigit()):
                    flog = False
    if (flog):
        print("Data Válida")
    else:
        print("A data informada não tem um formato válido.")

      
    #Verificando Tamanho do CPF com pontos e barras
    if (len(cpf) != tam_cpf):
        flag = False
    elif ((cpf[3] != ".") or (cpf[7] != ".") or (cpf[-3] != "-")):
        flag = False
    else:
        for i in range(tam_cpf):
            if (i != 3) and (i != 7) and (i != 11):
                c = cpf[i]
                if (not c.isdigit()):
                    flag = False

    if (flag):
        print("Formato de CPF Válido.")
        print("-" * 40)
    else:
        print("O CPF informado não tem um formato válido.")

    print("Revise seus dados antes de continuar ")
    print("-" * 40)
    print(f"Nome: {nome} \nData de nascimento: {dn} \nNumero de  CPF: {cpf} \nNumero de RG: {rg} \nNome da mãe: {mae}.")
    print("-" * 40)

    print("Cadastro Concluido")


# nome do usuario
Label_nome = Label(janela, width=10, height=2, text="Nome: ", font=('Arial 10'))
Label_nome.grid(row=0, column=0, padx=10, pady=5)
enntry_nome = Entry(janela, font=('Arial 10'))
enntry_nome.grid(row=0, column=1, padx=10, pady=5)

# Data de nascimento
Label_dn = Label(janela, width=20, height=2, text="Data de Nascimento: ", font=('Arial 10'))
Label_dn.grid(row=1, column=0, padx=10, pady=5)
enntry_dn = Entry(janela, font=('Arial 10'))
enntry_dn.grid(row=1, column=1, padx=10, pady=5)

# Nome da Mãe
Label_nome_mae = Label(janela, width=10, height=2, text="Nome da Mãe: ", font=('Arial 10'))
Label_nome_mae.grid(row=2, column=0, padx=10, pady=5)
enntry_nome_mae = Entry(janela, font=('Arial 10'))
enntry_nome_mae.grid(row=2, column=1, padx=10, pady=5)

# CPF
Label_cpf = Label(janela, width=10, height=2, text="CPF: ", font=('Arial 10'))
Label_cpf.grid(row=3, column=0, padx=10, pady=5)
enntry_cpf = Entry(janela, font=('Arial 10'))
enntry_cpf.grid(row=3, column=1, padx=10, pady=5)

# RG
Label_rg = Label(janela, width=10, height=2, text="RG: ", font=('Arial 10'))
Label_rg.grid(row=4, column=0, padx=10, pady=5)
enntry_rg = Entry(janela, font=('Arial 10'))
enntry_rg.grid(row=4, column=1, padx=10, pady=5)

botao = Button(janela, command=obter, width=8, height=1, text="Ver dados",relief="raised",fg="#fcb603",bg='white')
botao.grid(row=13,column=0,padx=5,pady=20)



janela.mainloop()
import tkinter as tk  # Importa o Tkinter


janela = tk.Tk()  # Cria a janela principal
janela.title("TechBairro — Cadastro de Cliente")  # Define o título
janela.geometry("480x500")  # Define o tamanho da janela
janela.resizable(False, False)  # Impede alterar o tamanho da janela


clientes = []  # Lista que vai armazenar os clientes


# ==================== CABEÇALHO ====================

cabecalho = tk.Frame(janela, bg="#2c3e50")  # Cria um Frame para o cabeçalho
cabecalho.pack(side="top", fill="x")  # Posiciona o Frame no topo


tk.Label(
    cabecalho,
    text="Cadastro de Cliente",
    fg="white",
    bg="#2c3e50",
    font=("Arial", 14, "bold"),
    pady=12
).pack()


# ==================== FORMULÁRIO ====================

form = tk.Frame(janela)  # Cria um Frame para o formulário
form.pack(pady=20)


campos = ["Nome", "Telefone", "E-mail", "Endereço"]
# Lista com os nomes dos campos


entradas = {}
# Dicionário que vai guardar os Entry


for i, campo in enumerate(campos):

    # Cria o Label do campo
    tk.Label(
        form,
        text=f"{campo}:"
    ).grid(
        row=i,
        column=0,
        sticky="e",
        padx=5,
        pady=6
    )

    # Cria o campo para digitar
    entrada = tk.Entry(form, width=30)

    # Posiciona o campo
    entrada.grid(
        row=i,
        column=1,
        padx=5,
        pady=6
    )

    # Guarda o Entry no dicionário
    entradas[campo] = entrada


# ==================== STATUS ====================

status = tk.Label(
    janela,
    text="Nenhum cliente cadastrado ainda",
    fg="gray",
    wraplength=440,
    justify="left"
)

status.pack(pady=(0, 5))


contador = tk.Label(
    janela,
    text="Clientes cadastrados: 0"
)

contador.pack()


# ==================== LIMPAR CAMPOS ====================

def limpar_campos():

    # Percorre todos os campos
    for entrada in entradas.values():

        # Apaga o conteúdo
        entrada.delete(0, tk.END)


# ==================== VALIDAÇÃO DO E-MAIL ====================

def email_parece_valido(email):

    # Verifica se existe o símbolo @
    if "@" not in email:
        return False

    # Divide o e-mail em usuário e domínio
    usuario, _, dominio = email.partition("@")

    # Verifica se o usuário está vazio
    # ou se o domínio não possui ponto
    if usuario == "" or "." not in dominio:
        return False

    # Se passou pelas validações
    return True


# ==================== SALVAR CLIENTE ====================

def salvar():

    # Pega os valores digitados nos campos
    valores = {
        campo: entradas[campo].get().strip()
        for campo in campos
    }

    # Verifica se existe algum campo vazio
    vazios = [
        campo
        for campo in campos
        if valores[campo] == ""
    ]

    # Se houver campos vazios
    if vazios:

        status.config(
            text=f"Preencha o(s) campo(s): {', '.join(vazios)}",
            fg="red"
        )

        return


    # Verifica se o telefone possui somente números
    if not valores["Telefone"].isdigit():

        status.config(
            text="Telefone inválido: use somente números.",
            fg="red"
        )

        return


    # Verifica se o e-mail parece válido
    if not email_parece_valido(valores["E-mail"]):

        status.config(
            text="E-mail inválido: use o formato nome@dominio.com",
            fg="red"
        )

        return


    # Adiciona o cliente à lista
    clientes.append(valores)


    # Mostra mensagem de sucesso
    status.config(
        text=f"Cliente '{valores['Nome']}' salvo com sucesso!",
        fg="green"
    )


    # Atualiza o contador
    contador.config(
        text=f"Clientes cadastrados: {len(clientes)}"
    )


    # Limpa os campos
    limpar_campos()


# ==================== CANCELAR ====================

def cancelar():

    # Limpa os campos
    limpar_campos()

    # Atualiza o status
    status.config(
        text="Formulário limpo",
        fg="gray"
    )


# ==================== CONSULTAR CLIENTES ====================

def abrir_consulta():

    # Cria uma nova janela ligada à principal
    consulta = tk.Toplevel(janela)

    # Define o título da nova janela
    consulta.title("Consulta de Clientes")

    # Define o tamanho da nova janela
    consulta.geometry("420x300")


    # Cria uma Listbox para mostrar os clientes
    lista = tk.Listbox(
        consulta,
        width=55
    )


    # Posiciona a Listbox
    lista.pack(
        side="left",
        padx=(10, 0),
        pady=10,
        fill="both",
        expand=True
    )


    # Cria a barra de rolagem
    scrollbar = tk.Scrollbar(consulta)


    # Posiciona a barra de rolagem
    scrollbar.pack(
        side="right",
        fill="y",
        pady=10
    )


    # Liga a Listbox à barra de rolagem
    lista.config(
        yscrollcommand=scrollbar.set
    )


    # Faz a barra controlar a Listbox
    scrollbar.config(
        command=lista.yview
    )


    # Verifica se não existem clientes
    if not clientes:

        lista.insert(
            tk.END,
            "Nenhum cliente cadastrado"
        )

    else:

        # Percorre todos os clientes cadastrados
        for cliente in clientes:

            # Monta o texto que será exibido
            texto = (
                f"{cliente['Nome']} | "
                f"{cliente['Telefone']} | "
                f"{cliente['E-mail']} | "
                f"{cliente['Endereço']}"
            )

            # Adiciona o cliente na Listbox
            lista.insert(
                tk.END,
                texto
            )


# ==================== BOTÕES ====================

botoes = tk.Frame(janela)
# Cria um Frame para os botões


botoes.pack(pady=10)
# Posiciona o Frame


tk.Button(
    botoes,
    text="Salvar",
    width=12,
    command=salvar
).grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    botoes,
    text="Cancelar",
    width=12,
    command=cancelar
).grid(
    row=0,
    column=1,
    padx=5
)


# Botão para abrir a consulta
tk.Button(
    janela,
    text="Consultar Clientes",
    command=abrir_consulta
).pack(pady=5)


# ==================== VERSÃO ====================

tk.Label(
    janela,
    text="v1.0",
    fg="gray"
).place(
    relx=0.97,
    rely=0.97,
    anchor="se"
)


# Mantém a janela aberta
janela.mainloop()

def mostrar_opcoes():
    menu = """
    +-------------------------------------+
    |           MENU DE OPÇÕES            |
    +-------------------------------------+
    | 1. Salvar                           |
    | 2. Editar                           |
    | 3. Deletar                          |
    | 4. Marcar um contato como favorito  |
    | 0. Sair                             |
    +-------------------------------------+
    """
    print(menu)
    return

def Salvar(lista_de_contatos, nome, telefone, email):
    contato = {"nome_contato": nome,
                "numero_telefone": telefone,
                "endereço_email": email,
                "favoritado": False
                }
    lista_de_contatos.append(contato)
    return

def visualizar_lista(lista_de_contatos):
    for indice, contato in enumerate(lista_de_contatos, start=1):
        favoritado = "✓" if contato ["favoritado"] else " "
        print(f"{indice}. [{favoritado}] {contato['nome_contato']} ({contato['numero_telefone']})")
    return

def editar(lista_de_contatos, indice_alteraçao, opcao_de_troca):
    indice_ajustado = indice_alteraçao - 1

    if indice_ajustado >= 0 and indice_ajustado <= len(lista_de_contatos):
        if opcao_de_troca == 1:
            novo_nome = input("Qual será o novo nome?: ")
            lista_de_contatos[indice_ajustado]['nome_contato'] = novo_nome
        elif opcao_de_troca == 2:
            novo_numero = input("Qual será o novo número?: ")
            lista_de_contatos[indice_ajustado]['numero_telefone'] = novo_numero
        elif opcao_de_troca == 3:
            novo_email = input("Qual será o novo e-mail?: ")
            lista_de_contatos[indice_ajustado]['endereço_email'] = novo_email
    return


lista_de_contatos = []
while True:
    mostrar_opcoes()
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        print("\nNovo contato\n")
        nome = input("Informe o nome do contato: ")
        telefone = int(input("Informe o número do contato: "))
        email = input("informe o e-mail do seu contato: ")
        Salvar(lista_de_contatos, nome, telefone, email)
        visualizar_lista(lista_de_contatos)
    elif escolha == 2:
        visualizar_lista(lista_de_contatos)
        indice_alteraçao = int(input("\nEssa é a sua lista de contatos, qual deseja alterar?: "))
        print("""
        +-------------------------------------+
        |           MENU DE OPÇÕES            |
        +-------------------------------------+
        | 1. Nome                             |
        | 2. Telefone                         |
        | 3. E-mail                           |
        +-------------------------------------+
        """)
        opcao_de_troca = int(input("Qual informação deseja alterar?: "))
        editar(lista_de_contatos, indice_alteraçao, opcao_de_troca)
        visualizar_lista(lista_de_contatos)
    elif escolha == 3:
        print("Você está deletando")
        visualizar_lista(lista_de_contatos)
    elif escolha == 4:
        print("Você está favoritando")
        visualizar_lista(lista_de_contatos)
    elif escolha == 0:
        break

visualizar_lista(lista_de_contatos)
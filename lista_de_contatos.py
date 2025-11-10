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
    print("""
    +----------------------------------------------------------+
    |                     LISTA DE CONTATOS                    |
    +----------------------------------------------------------+
    """)
    for indice, contato in enumerate(lista_de_contatos, start=1):
        favoritado = "✓" if contato ["favoritado"] else " "
        largura_nome = 25
        largura_telefone = 14
        print(f"    | {indice:>2}. [{favoritado}] {contato['nome_contato']:<{largura_nome}} Número: {contato['numero_telefone']:<{largura_telefone}} |")
    print("    +----------------------------------------------------------+")
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
        else:
            print("Digite um valor válido")
    return

def favoritar(lista_de_contatos, indice_alteracao):
    indice_ajustado = indice_alteracao - 1

    if indice_ajustado >= 0 and indice_ajustado <= len(lista_de_contatos):
        if lista_de_contatos[indice_ajustado]['favoritado'] == False:
            lista_de_contatos[indice_ajustado]["favoritado"] = True
        else:
            lista_de_contatos[indice_ajustado]["favoritado"] = False
    return

def ver_contatos_favoritos(lista_de_contatos):
    print("""
    +----------------------------------------------------------+
    |                LISTA DE CONTATOS FAVORITOS               |
    +----------------------------------------------------------+
    """)
    for indice, contato_favorito in enumerate(lista_de_contatos,start=1):
        if contato_favorito ['favoritado'] == True:
            favoritado = "✓" if contato_favorito ["favoritado"] == True else " "
            largura_nome = 25
            largura_telefone = 14
            print(f"    | {indice:>2}. [{favoritado}] {contato_favorito['nome_contato']:<{largura_nome}} Número: {contato_favorito['numero_telefone']:<{largura_telefone}} |")
        else:
            continue
    print("    +----------------------------------------------------------+")
    return

def deletar_contato(lista_de_contatos, indice_alteracao):
    indice_ajustado = indice_alteracao - 1
    if indice_ajustado >= 0 and indice_ajustado <= len(lista_de_contatos):
        contato_removido = lista_de_contatos.pop(indice_ajustado)
        print(f"O contato {contato_removido}, foi removido da sua lista!")
    return


lista_de_contatos = []
while True:
    mostrar_opcoes()
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        print("""
        +-------------------------------------+
        |            NOVO CONTATO             |
        +-------------------------------------+
        """)
        nome = input(">>> Digite o nome do contato: ")
        telefone = int(input("\n>>> Digite o telefone (Ex: 11987654321): "))
        email = input("\n>>> Digite o e-mail (Ex: nome@email.com): ")
        Salvar(lista_de_contatos, nome, telefone, email)
        visualizar_lista(lista_de_contatos)
    elif escolha == 2:
        visualizar_lista(lista_de_contatos)
        indice_alteraçao = int(input("\n>>> Qual contato deseja alterar? (Digite o número do indice): "))
        print("""
        +-------------------------------------+
        |           MENU DE OPÇÕES            |
        +-------------------------------------+
        | 1. Nome                             |
        | 2. Telefone                         |
        | 3. E-mail                           |
        +-------------------------------------+
        """)
        opcao_de_troca = int(input(">>> Qual informação deseja alterar?: "))
        editar(lista_de_contatos, indice_alteraçao, opcao_de_troca)
        visualizar_lista(lista_de_contatos)
    elif escolha == 3:
        visualizar_lista(lista_de_contatos)
        indice_alteracao = int(input(">>> Qual contato deseja remover? (Digite o número): "))
        deletar_contato(lista_de_contatos, indice_alteracao)
        visualizar_lista(lista_de_contatos)
    elif escolha == 4:
        visualizar_lista(lista_de_contatos)
        indice_alteracao = int(input("\n>>> Qual contato (favoritar/desfavoritar)? (Digite o número): "))
        favoritar(lista_de_contatos, indice_alteracao)
        ver_contatos_favoritos(lista_de_contatos)
        #visualizar_lista(lista_de_contatos)
    elif escolha == 0:
        break
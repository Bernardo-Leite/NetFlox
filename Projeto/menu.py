import funcoes
import getpass
import os

#from passlib.hash import sha256_crypt

from datetime import datetime

#-------------------------------------------------------------------------------------> MENU PRINCIPAL

def menu_inicial():
    os.system('cls') or None
    print(
        '\033[37;40m\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\033')
    print('  \u2551\u2551    Welcome to NETFLOX    \u2551')
    print('\u2551                          \u2551')
    print('\u2551 1\u2192Login                  \u2551')
    print('\u2551 2\u2192Novo utilizador        \u2551')
    print('\u2551 3\u2192Sair                   \u2551')
    print(
        '\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d')

    while True:
        opcao = input("Insira a opção: ")
        if opcao not in ['1', '2', '3']:
            print("Insira uma opção valida!")
        else:
            break
    print()
    if opcao == '1':  #### Login
        print("Login: ")
        while True:
            email_input = input("E-mail: ")
            if email_input == '' or ' ' in email_input:
                print("Não insira um campo vazio...")
            else:
                break
        while True:
            passwd_input = getpass.getpass('Password:')
            if passwd_input == '':
                print("Não insira um campo vazio...")
            else:
                break
        if funcoes.check_login(email_input, passwd_input) == 'cliente':
            print()
            print("Login bem sucedido!", email_input)
            print()
            menu_cliente(email_input)

        elif funcoes.check_login(email_input, passwd_input) == 'admin':
            print()
            print("Admin", email_input, "bem vindo!")
            print()
            menu_admin(email_input)

        elif funcoes.check_login(email_input, passwd_input) == 0:
            print("Login invalido!")
            while True:
                move_on = input("Enter para continuar")
                if move_on == '':
                    break
            os.system('cls') or None
            menu_inicial()

    elif opcao == '2':  #### Novo utilizador
        print("Registo: ")
        while True:
            utilizador_email = input("Insira o email: ")
            if (utilizador_email == '' or ' ' in utilizador_email):
                print("Não insira um campo vazio!")
            else:
                break
        while True:
            utilizador_password = getpass.getpass('Password:')
            if utilizador_password == '':
                print("Não insira um campo vazio!")
            else:
                break
        while True:
            utilizador_nome = input("Insira o seu nome: ")
            if utilizador_nome == '':
                print("Não insira um campo vazio!")
            else:
                break
        funcoes.insere_novo_utilizador(utilizador_email, utilizador_password, utilizador_nome)
        menu_inicial()

    if opcao == '3':  #### Sair
        exit()


#------------------------------------------------------------------------------------------> MENU CLIENTE


def menu_cliente(user):
    os.system('cls') or None
    print(
        '\033[31;40m\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\033')
    print('\u2551\u2551       Menu Cliente          \u2551')
    print('\u2551                             \u2551')
    print('\u2551 Utilizador: ' +user+ '      \u2551')
    print('\u2551 1\u2192Lista de artigos          \u2551')
    print('\u2551 2\u2192Detalhes de artigo        \u2551')
    print('\u2551 3\u2192Minha galeria             \u2551')
    print('\u2551 4\u2192Aluguer                   \u2551')
    print('\u2551 5\u2192Historico de alugueres    \u2551')
    print('\u2551 6\u2192Mensagens                 \u2551')
    print('\u2551 7\u2192Pesquisa                  \u2551')
    print('\u2551 8\u2192Sair                      \u2551')
    print(
        '\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d')

    while True:
        opcao = input("Escolha uma das opcoes:")
        if opcao not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Opcao invalida")
        else:
            break
    if opcao == '1':
        print()
        funcoes.listar_artigos(user)
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_cliente(user)
    elif opcao == '2':
        print()
        funcoes.detalhes_artigos(user)
    elif opcao == '3':
        print()
        funcoes.minha_galeria(user)
    elif opcao == '4':
        print()
        menu_aluguer(user)
    elif opcao == '5':
        print()
        funcoes.historico_aluguer(user)
    elif opcao == '6':
        print()
        funcoes.mensagem_cliente(user)
    elif opcao == '7':
        pesq = sist_hist()
        menu_pesquisa(user, pesq)
    elif opcao == '8':
        os.system('cls') or None
        menu_inicial()

def menu_aluguer(user):
    os.system('cls') or None
    print(
        '\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557')
    print('\u2551           Menu Aluguer           \u2551')
    print('\u2551                                  \u2551')
    print('\u2551 1\u2192Alugar artigo                  \u2551')
    print('\u2551 2\u2192Finalizar Pagamento            \u2551')
    print('\u2551 3\u2192Valor de alugueres passados    \u2551')
    print('\u2551 4\u2192Voltar ao menu                 \u2551')
    print(
        '\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d')
    while True:
        opcao = input("Escolha uma opcao: ")
        if opcao not in ['1', '2', '3', '4']:
            print("Opcao invalida!")
        else:
            break

    if opcao == '1':
        funcoes.alugar_artigo(user)
    elif opcao == '2':
        funcoes.finalizar_pagamento(user)
    elif opcao == '3':
        funcoes.total_preco_tipo(user)
    elif opcao == '4':
        os.system('cls') or None
        menu_cliente(user)

#---------------------------------------------------------------------------------> MENU ADMIN


def menu_admin(utilizador):
    os.system('cls') or None
    print(
        '\033[36;40m\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557\033')
    print('\u2551\u2551                Menu Admin                  \u2551')
    print('\u2551                                            \u2551')
    print('\u2551 Admin: ' + utilizador + '                         \u2551')
    print('\u2551 1\u2192Adicionar novo artigo                    \u2551')
    print('\u2551 2\u2192Ver stock de artigo                      \u2551')
    print('\u2551 3\u2192Corrigir preco de um artigo              \u2551')
    print('\u2551 4\u2192Remover artigo                           \u2551')
    print('\u2551 5\u2192Enviar mensagem a todos os clientes      \u2551')
    print('\u2551 6\u2192Enviar mensagem a um cliente especifico  \u2551')
    print('\u2551 7\u2192Aumentar saldo de cliente                \u2551')
    print('\u2551 8\u2192Estatisticas                             \u2551')
    print('\u2551 9\u2192Sair                                     \u2551')
    print(
        '\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d')
    while True:
        opcao = input("Insira uma opção: ")
        if opcao not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Insira uma opção valida!")
        else:
            break
    if opcao == '1':  #### Adicionar novo artigo

        while True:
            artigo_titulo = input("Titulo: ")
            if artigo_titulo == '':
                print("Não insira um campo vazio!")
            else:
                break
        while True:
            try:
                artigo_preco = float(input("Preco: "))
                if artigo_preco == 0:
                    print("Erro, preço não pode ser zero!")
                else:
                    break
            except ValueError:
                print("Tem de inserir um numero")
        while True:
                artigo_tipo = input("Tipo de artigo (serie/filme/documentario): ")
                if artigo_tipo == '':
                    print("Não insira um campo vazio!")
                else:
                    break
        while True:
            artigo_produtora = input("Nome da Produtora: ")
            if artigo_produtora == '':
                print("Não insira um campo vazio")
            else:
                break

        id_produtora = funcoes.get_id_produtora(artigo_produtora)  # Vai buscar o id da produtora e guarda

        if id_produtora == None:  # Se a funcao retornar "none" quer dizer que não existe nenhuma editora com aquele nome
            funcoes.cria_produtora(artigo_produtora)  # Entao criamos a produtora inserida

        id_produtora = funcoes.get_id_produtora(artigo_produtora)  # Vai buscar o id da editora e guarda

        id_atores = []  # Lista com os id's dos atores
        while True:
            try:
                n = int(input("Quantos atores tem o artigo: "))
                if n == 0:
                    print("O artigo não pode ter 0 atores!")
                else:
                    break
            except ValueError:
                print("Tem de inserir um numero!")

        for i in range(0, n):  # Para os varios atores que o artigo tenha
            while True:
                nome_ator = input("Nome do Ator: ")
                if nome_ator == '':
                    print("Não insira um campo vazio")
                else:
                    if funcoes.get_id_ator(nome_ator) == None:  # Se ainda nao existir este ator
                        funcoes.cria_ator(nome_ator)  # Criamos um novo ator
                        id_atores.append(funcoes.get_id_ator(nome_ator))
                    else:
                        id_atores.append(funcoes.get_id_ator(nome_ator))
                    break

        id_realizadores = []  # Lista com os id's dos realizadores
        while True:
            try:
                n = int(input("Quantos realizadores tem o artigo: "))
                if n == 0:
                    print("O artigo não pode ter 0 realizadores!")
                else:
                    break
            except ValueError:
                print("Tem de inserir um numero!")

        for i in range(0, n):  # Para os varios realizadores que o artigo tenha
            while True:
                nome_realizador = input("Nome do Realizador: ")
                if nome_realizador == '':
                    print("Não insira um campo vazio")
                else:
                    if funcoes.get_id_realizador(nome_realizador) == None:  # Se ainda nao existir este realizador
                        funcoes.cria_realizador(nome_realizador)  # Criamos um novo realizador
                        id_realizadores.append(funcoes.get_id_realizador(nome_realizador))
                    else:
                        id_realizadores.append(funcoes.get_id_realizador(nome_realizador))
                    break

        funcoes.adicionar_artigo(artigo_titulo, artigo_preco, artigo_tipo, id_produtora)
        id_artigo = funcoes.get_id_artigo(artigo_titulo)

        for i in id_atores:
            funcoes.insere_atores_artigo(id_artigo, i)

        for i in id_realizadores:
            funcoes.insere_realizadores_artigo(id_artigo, i)

        funcoes.insere_historico_preco(utilizador, id_artigo, artigo_preco)

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_admin(utilizador)
    elif opcao == '2':  #### Ver stock de artigo
        funcoes.ver_stock_artigos(utilizador)
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_admin(utilizador)
    elif opcao == '3':  #### Corrigir preco de artigo
        funcoes.corrigir_preco_artigo(utilizador)
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_admin(utilizador)
    elif opcao == '4':  #### Remover artigo
        funcoes.remover_artigo()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_admin(utilizador)
    elif opcao == '5':  #### Enviar uma mensagem a todos os clientes
        funcoes.enviar_mensagem_todos_clientes()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_admin(utilizador)
    elif opcao == '6':  #### Enviar uma mensagem a um cliente especifico
        funcoes.enviar_mensagem_cliente_especifico()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_admin(utilizador)
    elif opcao == '7':  #### Aumentar saldo de cliente
        funcoes.aumentar_saldo(utilizador)
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_admin(utilizador)
    elif opcao == '8':  #### Estatisticas
        menu_estatisticas(utilizador)
    elif opcao == '9':  #### Sair
        os.system('cls') or None
        menu_inicial()


#-------------------------------------------------------------------------------------> MENU ESTATISTICA


def menu_estatisticas(utilizador):
    os.system('cls') or None
    print(
        '\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557')
    print('\u2551              Estatisticas                 \u2551')
    print('\u2551                                           \u2551')
    print('\u2551 1\u2192Total de clientes                       \u2551')
    print('\u2551 2\u2192Total de artigos                        \u2551')
    print('\u2551 3\u2192Valor total de artigos alugados         \u2551')
    print('\u2551 4\u2192Valor total dos alugueres               \u2551')
    print('\u2551 5\u2192Total de artigos por tipo               \u2551')
    print('\u2551 6\u2192Artigos mais alugados                   \u2551')
    print('\u2551 7\u2192Artigos de momento indisponiveis        \u2551')
    print('\u2551 8\u2192Sair                                    \u2551')
    print(
        '\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d')

    while True:
        opcao = input("Insira a opção: ")
        if opcao not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Insira uma opção válida!")
        else:
            break
    if opcao == '1':  #### Total de clientes
        funcoes.total_clientes()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_estatisticas(utilizador)
    elif opcao == '2':  #### Total de artigos
        funcoes.total_artigos()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_estatisticas(utilizador)
    elif opcao == '3':  #### Valor total de artigos alugados neste momento
        funcoes.valor_artigos_alugados_nestemomento()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_estatisticas(utilizador)
    elif opcao == '4':  #### Valor total dos alugueres
        funcoes.valor_alugueres()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_estatisticas(utilizador)
    elif opcao == '5':  #### Total de artigos por tipo
        funcoes.total_artigos_tipo()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_estatisticas(utilizador)
    elif opcao == '6':  #### Artigos mais alugados
        funcoes.artigos_mais_alugados()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_estatisticas(utilizador)
    elif opcao == '7':  #### Artigos indisponiveis
        funcoes.artigos_falta_stock()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu_estatisticas(utilizador)
    elif opcao == '8':  #### Sair (Voltar ao menu admin)
        os.system('cls') or None
        menu_admin(utilizador)


# --------------------------------------------------------------------------------------------------------> PESQUISAS

def menu_pesquisa(user, pesq):
    os.system('cls') or None
    print("\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557")
    print("\u2551              Pesquisa            \u2551")
    print("\u2551                                  \u2551")
    print("\u2551 Escolha o critério de pesquisa   \u2551")
    print("\u2551 1.\tAtor                       \u2551")
    print("\u2551 2.\tRealizador                 \u2551")
    print("\u2551 3.\tProdutora                  \u2551")
    print("\u2551 4.\tTitulo                     \u2551")
    print("\u2551 5.\tTipo                       \u2551")
    print("\u2551 6.\tVoltar ao menu cliente     \u2551")
    print("\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d")
    while True:
        opcao = input("Insira a opção: ")
        if opcao not in ['1', '2', '3', '4', '5', '6']:
            print("Insira uma opção válida!")
        else:
            break

    if opcao == '1':
        crit = pesquisa_ordenar(user, pesq)
        ord = asc_desc()
        if pesq == 1:
            funcoes.pesquisa_atores(user, crit, ord)
        else:
            funcoes.pesquisa_atores_aluguer(user, crit, ord)

    elif opcao == '2':
        crit = pesquisa_ordenar(user, pesq)
        ord = asc_desc()
        if pesq == 1:
            funcoes.pesquisa_realizadores(user, crit, ord)
        else:
            funcoes.pesquisa_realizadores_aluguer(user, crit, ord)

    elif opcao == '3':
        crit = pesquisa_ordenar(user, pesq)
        ord = asc_desc()
        if pesq == 1:
            funcoes.pesquisa_produtora(user, crit, ord)
        else:
            funcoes.pesquisa_produtora_aluguer(user, crit, ord)

    elif opcao == '4':
        crit = pesquisa_ordenar(user, pesq)
        ord = asc_desc()
        if pesq == 1:
            funcoes.pesquisa_titulo(user, crit, ord)
        else:
            funcoes.pesquisa_titulo_aluguer(user, crit, ord)

    elif opcao == '5':
        crit = pesquisa_ordenar(user, pesq)
        ord = asc_desc()
        if pesq == 1:
            funcoes.pesquisa_tipo(user, crit, ord)
        else:
            funcoes.pesquisa_tipo_aluguer(user, crit, ord)

    elif opcao == '6':
        menu_cliente(user)


def sist_hist():
    os.system('cls') or None
    print("Onde pretende pesquisar?")
    print("1.\tSistema")
    print("2.\tHistorico de alugueres")
    while True:
        opcao = input("Insira a opção: ")
        if opcao not in ['1', '2']:
            print("Insira uma opção válida!")
        else:
            break
    if opcao == '1':
        return 1
    if opcao == '2':
        return 2

def pesquisa_ordenar(user, pesq):
    os.system('cls') or None
    print("Escolha o critério de ordenação:")
    print("1.\tID do artigo")
    print("2.\tTitulo do artigo")
    print("3.\tPreço do aluguer")
    print("4.\tVoltar atrás")
    while True:
        opcao = input("Insira a opção: ")
        if opcao not in ['1', '2', '3', '4']:
            print("Insira uma opção válida!")
        else:
            break
    if opcao == '1':
        return 'id'
    if opcao == '2':
        return 'titulo'
    if opcao == '3':
        return 'preco'
    if opcao == '4':
        menu_pesquisa(user, pesq)

def asc_desc():
    os.system('cls') or None
    print("Escolha uma ordem:")
    print("1.\tAscendente \u2191")
    print("2.\tDescendente \u2193")
    while True:
        opcao = input("Insira a opção: ")
        if opcao not in ['1', '2']:
            print("Insira uma opção válida!")
        else:
            break
    if opcao == '1':
        return 'ASC'
    if opcao == '2':
        return 'DESC'

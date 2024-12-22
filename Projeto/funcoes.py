# Todas as funcoes que vão servir para pesquisar na base de dados devem ser implementadas aqui
import psycopg2
import psycopg2.extras

import os

# Coneção à base de dados basica
import menu

#-------------------------------------------------------------------------------------------------------------------
#FUNÇÕES LOGIN
#-------------------------------------------------------------------------------------------------------------------

def insere_novo_utilizador(utilizador_email, utilizador_passwd, utilizador_nome):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()

        postgres_insert_query = """ INSERT INTO utilizador (email, password, nome) VALUES (%s,%s,%s)"""
        record_to_insert = (utilizador_email, utilizador_passwd, utilizador_nome)

        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()

    except (Exception, psycopg2.Error):
        if (connection):
            print("Esse email já tem conta criada! Insira outro email.")

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-------------------------------------------------------------------------------------------------------------------


def check_login(input_email, input_password):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT utilizador.email, utilizador.password, cliente.utilizador_email FROM utilizador, cliente WHERE utilizador.email =%s AND utilizador.password = %s AND cliente.utilizador_email = %s;",(input_email, input_password, input_email))

        if cursor.rowcount == 1:
            return 'cliente'  # codigo para cliente_login
        else:
            cursor.execute("SELECT utilizador.email, utilizador.password, admin.utilizador_email FROM utilizador, admin WHERE utilizador.email =%s AND utilizador.password = %s AND admin.utilizador_email = %s;",(input_email, input_password, input_email))
            if cursor.rowcount == 1:
                return 'admin'  # codigo para admin_login
            else:
                return 0

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------------------------------
#FUNÇÕES DE CLIENTE
#------------------------------------------------------------------------------------------------------------------------

def listar_artigos(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT id, titulo FROM artigos ORDER BY id;")

        for linha in cursor.fetchall():
            x1 = linha[0]
            x2 = linha[1]
            print("ID:\t", x1, "\tTitulo: ", x2)

        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        #closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def minha_galeria(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")
        cursor = connection.cursor()
        cursor.execute("SELECT artigos_id FROM aluguer WHERE confirmacao = true AND cliente_utilizador_email = %s;",(user,))
        for linha in cursor.fetchall():
            artigos_id = linha[0]
            cursor.execute("SELECT titulo, tipo FROM artigos WHERE id = %s;", (artigos_id,))
            for linha in cursor.fetchall():
                x1 = linha[0]
                x2 = linha[1]
                print("Titulo:\t", x1, "\tTipo: ", x2)

        print()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu.menu_cliente(user)

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def historico_aluguer(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")
        cursor = connection.cursor()
        cursor.execute("SELECT id, preco, data, artigos_id FROM aluguer WHERE confirmacao = true AND cliente_utilizador_email = %s", (user,))

        for linha in cursor.fetchall():
            id = linha[0]
            preco = linha[1]
            data = linha[2]
            artigos_id = linha[3]
            cursor.execute("SELECT titulo, tipo FROM artigos WHERE id = %s;", (artigos_id,))
            for linha in cursor.fetchall():
                titulo = linha[0]
                tipo = linha[1]
            print("ID do artigo:\t", artigos_id)
            print("ID do aluguer:\t", id)
            print("Tipo:\t", tipo)
            print("Preco:\t", preco)
            print("Titulo:\t", titulo)
            print("Data do aluguer:\t", data.strftime("%A, %d %B %Y %I:%M%p"))
            print()

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu.menu_cliente(user)

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def mensagem_cliente(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        os.system('cls') or None
        cursor = connection.cursor()
        id_mensagens = []
        print(
            '\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557')
        print('\u2551       Caixa de Entrada       \u2551')
        print(
            '\u255a\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255d')
        cursor.execute("SELECT mensagem.id,mensagem.assunto,mensagem.data FROM mensagem,leitura WHERE leitura.lida = false AND leitura.mensagem_id = mensagem.id AND leitura.cliente_utilizador_email = %s;",(user,))
        count = cursor.rowcount
        if count == 0:
             print("    Caixa de entrada vazia!")
             print()
        for linha in cursor.fetchall():
            id = linha[0]
            id_mensagens.append(linha[0])
            assunto = linha[1]
            data = linha[2]
            print("ID: ", id, "Assunto: ", assunto, "Data: ", data.strftime("%A, %d %B %Y %I:%M%p"))
            print("----------------------------------------")
        print("1\u2192Ler mensagem")
        print("2\u2192Lidas")
        print("3\u2192Menu inicial")
        while True:
            opcao = input("Insira a opção: ")
            if opcao not in ['1', '2', '3']:
                print("Insira uma opção valida!")
            else:
                break
        if opcao == '1':
            if count == 0:
                print("Não tem mensagens por ler.")
                while True:
                    move_on = input("Enter para continuar")
                    if move_on == '':
                        break
                os.system('cls') or None
                mensagem_cliente(user)
            else:
                ler_mensagem(user, id_mensagens)
                mensagem_cliente(user)
        if opcao == '2':
            mensagens_n_lidas(user)
            mensagem_cliente(user)
        if opcao == '3':
            os.system('cls') or None
            menu.menu_cliente(user)

        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def mensagens_n_lidas(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT mensagem.id,mensagem.assunto,mensagem.data FROM mensagem,leitura WHERE leitura.lida = true AND leitura.mensagem_id = mensagem.id AND leitura.cliente_utilizador_email = %s;",(user,))
        if cursor.rowcount == 0:
            print("Não tem mensagens lidas")

        id_mensagens = []

        for linha in cursor.fetchall():
            id = linha[0]
            id_mensagens.append(linha[0])
            assunto = linha[1]
            data = linha[2]
            print("ID: ", id, "Assunto: ", assunto, "Data: ", data.strftime("%A, %d %B %Y %I:%M%p"))
            print("----------------------------------------")

        while True:
            id = int(input("Insira o id da mensagem que quer ler: "))
            if id not in id_mensagens:
                print("Não é possivel ler essa mensagem")
            else:
                break

        cursor.execute("SELECT assunto,texto FROM mensagem WHERE id = %s;", (id,))

        for linha in cursor.fetchall():
            print("Assunto: ", linha[0])
            print()
            print(linha[1])
            print("---------------FIM------------------------")

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def ler_mensagem(user, id_mensagens):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        while True:
            id = int(input("Insira o id da mensagem que quer ler: "))
            if id not in id_mensagens:
                print("Não é possivel ler essa mensagem")
            else:
                break
        cursor.execute("SELECT assunto,texto FROM mensagem WHERE id = %s;", (id,))
        for linha in cursor.fetchall():
            print("Assunto: ", linha[0])
            print()
            print(linha[1])



        cursor.execute("UPDATE leitura SET lida = true WHERE mensagem_id = %s AND cliente_utilizador_email = %s;",(id, user))
        connection.commit()
        count = cursor.rowcount
        # DEBUG
        print(count, " record updated succesfully.")

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def total_preco_tipo(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        print()
        cursor.execute("SELECT sum(preco) FROM aluguer WHERE confirmacao = true AND cliente_utilizador_email = %s;",(user,))
        for linha in cursor.fetchall():
            print("Dinheiro total gasto em artigos alugados:", linha[0], "€")

        cursor.execute("SELECT sum(aluguer.preco) FROM artigos,aluguer WHERE artigos.tipo = 'serie' AND aluguer.confirmacao = true AND aluguer.cliente_utilizador_email = %s AND artigos.id=aluguer.artigos_id;",(user,))
        for linha in cursor.fetchall():
            print("Dinheiro gasto em aluguer de series:", linha[0], "€")

        cursor.execute("SELECT sum(aluguer.preco) FROM artigos,aluguer WHERE artigos.tipo = 'documentario' AND aluguer.confirmacao = true AND aluguer.cliente_utilizador_email = %s AND artigos.id=aluguer.artigos_id;",(user,))
        for linha in cursor.fetchall():
            print("Dinheiro gasto em aluguer de documentarios:", linha[0], "€")

        cursor.execute("SELECT sum(aluguer.preco) FROM artigos,aluguer WHERE artigos.tipo = 'filme' AND aluguer.confirmacao = true AND aluguer.cliente_utilizador_email = %s AND artigos.id=aluguer.artigos_id;",(user,))
        for linha in cursor.fetchall():
            print("Dinheiro gasto em aluguer de filmes:", linha[0], "€")

        print()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu.menu_aluguer(user)

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def detalhes_artigos(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT id, titulo FROM artigos;")
        artigos_id = []
        for linha in cursor.fetchall():
            artigos_id.append(str(linha[0]))

        listar_artigos(user)

        while True:
            op1 = input("Insira o ID do artigo: ")
            if op1 not in artigos_id:
                print("Insira uma opção válida!")
            else:
                break

        cursor.execute("SELECT DISTINCT produtora_id "
                       "FROM artigos "
                       "WHERE artigos.id = %s;", (op1,))

        produtora_id = 0
        for linha in cursor.fetchall():
            produtora_id = linha[0]

        cursor.execute("SELECT DISTINCT artigos.id, artigos.titulo, preco, tipo, produtora.nome "
                       "FROM artigos, produtora "
                       "WHERE artigos.id = %s AND produtora.id = %s;", (op1, produtora_id))

        realizadores = []
        atores = []
        for linha in cursor.fetchall():
            id_artigos = linha[0]
            nome_artigos = linha[1]
            preco = linha[2]
            tipo = linha[3]
            produtora = linha[4]

            cursor.execute("SELECT DISTINCT nome FROM atores WHERE id IN (SELECT DISTINCT atores_id FROM atores_artigos WHERE artigos_id = %s);",(op1,))
            for linha in cursor.fetchall():
                atores.append(linha[0])
            cursor.execute("SELECT DISTINCT nome FROM realizadores WHERE id IN (SELECT DISTINCT realizadores_id FROM realizadores_artigos WHERE artigos_id = %s);",(op1,))
            for linha in cursor.fetchall():
                realizadores.append(linha[0])
        print("ID: ", id_artigos)
        print("Titulo:", nome_artigos)
        for i, atores in enumerate(atores, start=1):
            print("Ator", i, ":", atores)
        for i, realizadores in enumerate(realizadores, start=1):
            print("Realizadores", i, ":", realizadores)

        print("Tipo:", tipo)
        print("Produtora:", produtora)
        print("Preço:", preco, "€")

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        os.system('cls') or None
        menu.menu_cliente(user)

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def alugar_artigo(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()

        cursor.execute("SELECT id FROM artigos;")
        artigo_id = []
        for linha in cursor.fetchall():
            artigo_id.append(str(linha[0]))

        print()
        listar_artigos(user)
        print()

        while True:
            opcao_ID = input("Insira o ID do artigo que pretende alugar:")
            if opcao_ID not in artigo_id:
                print("ID invalido!")
            else:
                break

        cursor.execute("SELECT confirmacao FROM aluguer WHERE artigos_id = %s AND cliente_utilizador_email = %s ;", (opcao_ID,user,))
        conf=False
        for linha in cursor.fetchall():
            confirmacao = linha[0]
            conf=confirmacao
        if conf is True:
            print("O artigo ja se encontra alugado por este cliente!")
            while True:
                move_on = input("Enter para continuar")
                if move_on == '':
                    break
            menu.menu_aluguer(user)

        cursor.execute("SELECT em_stock FROM artigos WHERE id = %s;", (opcao_ID,))
        for linha in cursor.fetchall():
            stock = linha[0]
        if stock is False:
            print("De momento o artigo nao esta disponivel!")
            while True:
                move_on = input("Enter para continuar")
                if move_on == '':
                    break
            menu.menu_aluguer(user)

        cursor.execute("SELECT preco FROM artigos WHERE id = %s;", (opcao_ID,))
        for linha in cursor.fetchall():
            preco = linha[0]


        cursor.execute("SELECT tipo FROM artigos WHERE id = %s;", (opcao_ID,))
        for linha in cursor.fetchall():
            tipo = linha[0]

        if tipo == 'filme':
            tempo_aluguer = "1"
        elif tipo == 'serie':
            tempo_aluguer = "6"
        else:
            tempo_aluguer = "3"

        cursor.execute("INSERT INTO aluguer (id, data, preco, confirmacao, tempo_aluguer, cliente_utilizador_email, artigos_id) VALUES(nextval('aluguer_id_sequence'), now(), %s, False, %s, %s, %s);",(preco, tempo_aluguer, user, opcao_ID))
        connection.commit()
        print("Artigo pre-alugado. Proceda a finalizaçao do pagamento.")
        print()
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        menu.menu_aluguer(user)

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)
    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def finalizar_pagamento(user):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()

        cursor.execute("SELECT cliente.saldo, aluguer.preco FROM cliente, aluguer WHERE utilizador_email = %s AND cliente_utilizador_email = %s and confirmacao = false;",(user, user,))

        for linha in cursor.fetchall():
            saldo1 = linha[0]
            preco1 = linha[1]

        if preco1 > saldo1:
            print("Saldo insuficiente!")
            print()
            while True:
                move_on = input("Enter para continuar")
                if move_on == '':
                    break
            os.system('cls') or None
            menu.menu_aluguer(user)

        else:
            sal = saldo1 - preco1
            cursor.execute("UPDATE cliente SET saldo =%s WHERE utilizador_email = %s;", (sal, user))
            connection.commit()
            cursor.execute("UPDATE aluguer SET confirmacao = true WHERE cliente_utilizador_email = %s;", (user,))
            connection.commit()
            cursor.execute("SELECT artigos_id FROM aluguer WHERE confirmacao = true;")
            for linha in cursor.fetchall():
                id_artigo = linha[0]
                cursor.execute("UPDATE artigos SET alugado = true WHERE id = %s;", (id_artigo,))
                connection.commit()

            print("Confirmado. Artigo alugado!")
            print()
            while True:
                move_on = input("Enter para continuar")
                if move_on == '':
                    break
            os.system('cls') or None
            menu.menu_aluguer(user)

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)
    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

#-------------------------------------------------------------------------------------------------------------------------
#FUNÇÕES DE ADMIN
#-------------------------------------------------------------------------------------------------------------------------


def adicionar_artigo(artigo_titulo, artigo_preco, artigo_tipo, id_produtora):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO artigos VALUES (%s,nextval('artigos_id_sequence'),%s,false,%s,true,%s);",(artigo_titulo, artigo_preco, artigo_tipo, id_produtora))
        connection.commit()
        print("O artigo foi adicionado com sucesso!")
        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
    # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

#-------------------------------------------------------------------------------------------------------------------------


def ver_stock_artigos(utilizador):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT id, titulo, preco FROM artigos WHERE em_stock = TRUE ORDER BY id;")
        for linha in cursor.fetchall():
            id = linha[0]
            titulo = linha[1]
            preco = linha[2]
            cursor.execute("SELECT tipo FROM artigos WHERE id = %s;", (id,))
            for linha in cursor.fetchall():
                tipo = linha[0]

            if tipo == 'filme':
                tempo_aluguer = "1"
            elif tipo == 'serie':
                tempo_aluguer = "6"
            else:
                tempo_aluguer = "3"
            print("ID:\t", id, "\tTitulo: ", titulo, "\tPreco: \t", preco, "€" ,"\tDuracao do aluguer: \t", tempo_aluguer, "Meses")

        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#---------------------------------------------------------------------------------------------------------------------


def corrigir_preco_artigo(utilizador):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        id_artigo = []

        cursor.execute("SELECT id FROM artigos WHERE em_stock = true")  # Seleciona id de artigos que estao em stock
        for linha in cursor.fetchall():
            id_artigo.append(linha[0])  # Guarda esses id's na lista "id_artigo"

        print()
        ver_stock_artigos(utilizador)

        while True:
            id = int(input("Insira o id do artigo que pretende corrigir o preco: "))
            if id not in id_artigo:  # Verifica se o id inserido pertence a um artigo em stock
                print("Não é possivel selecionar esse artigo")
            else:
                break
        cursor.execute("SELECT preco FROM artigos WHERE id = %s;", (id,))
        for linha in cursor.fetchall():
            print("O preço atual é: ", linha[0],"€")

        while True:
            novo_preco = float(input("Insira o novo preco para o artigo selecionado: "))
            if novo_preco == 0:
                print("Valor invalido!")
            else:
                break
        cursor.execute("UPDATE artigos SET preco = %s WHERE id =%s;", (novo_preco, id))
        connection.commit()

        insere_historico_preco(utilizador, id, novo_preco)

        cursor.execute("UPDATE aluguer SET preco=%s WHERE artigos_id = %s;", (novo_preco, id))
        connection.commit()

        print("O preco do artigo foi alterado com sucesso!")
        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#--------------------------------------------------------------------------------------------------------------------


def insere_historico_preco(utilizador, artigo_id, preco):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO historico_preco VALUES (%s,now(),nextval('modifica_id_sequence'),%s,%s);",(preco, artigo_id, utilizador))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#---------------------------------------------------------------------------------------------------------------------


def remover_artigo():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        id_artigo = []
        id_artigo_aluguer = []
        cursor.execute("SELECT id FROM artigos WHERE alugado = false")  # verifica quais artigos ainda não foram alugados
        for linha in cursor.fetchall():
            id_artigo.append(linha[0])

        cursor.execute("SELECT DISTINCT artigos_id FROM aluguer")  # verifica quais artigos estão alugados
        for linha in cursor.fetchall():
            id_artigo_aluguer.append(linha[0])

        if id_artigo == id_artigo_aluguer or id_artigo == []:
            print("Não existem artigos que possam ser removidos!")
            return
        while True:
            id = int(input("Insira o id do artigo a remover: "))
            if (id not in id_artigo) or (id in id_artigo_aluguer):
                print("Não é possivel remover esse artigo! Não existe artigos com esse ID ou esse artigo está neste momento alugado")
            else:
                break

        cursor.execute("DELETE FROM atores_artigos WHERE artigos_id = %s;", (id,))
        connection.commit()

        cursor.execute("DELETE FROM realizadores_artigos WHERE artigos_id = %s;", (id,))
        connection.commit()

        cursor.execute("DELETE FROM historico_preco WHERE artigos_id = %s;", (id,))
        connection.commit()

        cursor.execute("DELETE FROM artigos WHERE id = %s", (id,))
        connection.commit()

        print("O artigo selecionado foi removido com sucesso!")
        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#--------------------------------------------------------------------------------------------------------------------


def enviar_mensagem_todos_clientes():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        while True:
            assunto = input("Qual é o assunto da mensagem: ")
            if assunto == '':
                print("Não pode inserir um assunto vazio")
            else:
                break

        while True:
            texto = input("Qual é o texto da mensagem: ")
            if assunto == '':
                print("Não pode inserir um texto vazio")
            else:
                break
        cursor.execute("INSERT INTO mensagem VALUES (nextval('mensagem_id_sequence'),%s,%s,now());", (texto, assunto))  # Insere na tabela "mensagem" o id da mensagem , o texto, o assunto e a data da mensagem
        connection.commit()

        clientes = []  # Lista com os emails de todos os clientes
        cursor.execute("SELECT utilizador_email FROM cliente")
        for linha in cursor.fetchall():
            clientes.append(linha[0])  # Adiciona na lista os varios emails dos clientes

        cursor.execute("SELECT id FROM mensagem ORDER BY id DESC LIMIT 1")  # Seleciona o id da mensagem mais recente
        id_mensagem = cursor.fetchone()  # Guarda em id_mensagem o valor desse id
        for i in clientes:  # Percorre a lista com os emails dos clientes
            cursor.execute("INSERT INTO leitura VALUES(false,%s,%s,%s);", (i, id_mensagem[0],i))  # Insere na tabela "leitura" o id da mensagem e o email dos clientes a quem foi enviada a mensagem
            connection.commit()

        print("Mensagem para todos os clientes enviada com sucesso!")
        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#--------------------------------------------------------------------------------------------------------------------


def enviar_mensagem_cliente_especifico():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        while True:
            assunto = input("Qual é o assunto da mensagem: ")
            if assunto == '':
                print("Não pode inserir um assunto vazio")
            else:
                break

        while True:
            texto = input("Qual é o texto da mensagem: ")
            if assunto == '':
                print("Não pode inserir um texto vazio")
            else:
                break
        cursor.execute("INSERT INTO mensagem VALUES (nextval('mensagem_id_sequence'),%s,%s,now());", (texto, assunto))  # Insere na tabela "mensagem" o id da mensagem , o texto, o assunto e a data da mensagem
        connection.commit()

        clientes = []  # Lista com os emails de todos os clientes
        cursor.execute("SELECT utilizador_email FROM cliente")
        for linha in cursor.fetchall():
            clientes.append(linha[0])  # Adiciona na lista os varios emails dos clientes

        while True:
            id = input("Insira o email do cliente a quem quer enviar a mensagem: ")
            if id not in clientes:  # Verifica se o email inserido pertence realmente a um cliente
                print("Não é possivel selecionar esse cliente. Esse cliente não existe!")
            else:
                break
        cursor.execute("SELECT id FROM mensagem ORDER BY id DESC LIMIT 1")  # Seleciona o id da mensagem mais recente
        id_mensagem = cursor.fetchone()  # Guarda em id_mensagem o valor desse id
        cursor.execute("INSERT INTO leitura VALUES(false,%s,%s,%s);", (id, id_mensagem[0],id))  # Insere na tabela "leitura" o id da mensagem e o email especifico do cliente a quem foi enviada a mensagem
        connection.commit()

        print("Mensagem para cliente em especifico enviada com sucesso!")
        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#---------------------------------------------------------------------------------------------------------------------


def aumentar_saldo(utilizador):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente")
        for linha in cursor.fetchall():
            email = linha[1]
            saldo = linha[0]
            print("Email:\t", email, "\tSaldo: ", saldo)  # Apresenta os emails e saldos de todos os clientes

        email_cliente = []
        cursor.execute("SELECT utilizador_email FROM cliente")
        for linha in cursor.fetchall():
            email_cliente.append(linha[0])  # Guarda em "email_cliente" os emails de todos os clientes

        while True:
            email_input = input(
                "Insira o email do utilizador que pretende aumentar o saldo: ")  # Guarda em "email_input" o email do utilizador que pretende aumentar o saldo
            if email_input not in email_cliente:  # Compara com a lista dos emails de todos os clientes se o email de cliente introduzido existe
                print("Esse utilizador não existe...")
            else:
                break

        aumento = float(input("Quanto deseja aumentar: "))
        cursor.execute("SELECT saldo FROM cliente WHERE utilizador_email = %s;", (email_input,))
        for linha in cursor.fetchall():
            saldo_antigo = linha[0]
        novo_saldo = saldo_antigo + aumento

        cursor.execute("UPDATE cliente SET saldo = %s WHERE utilizador_email = %s;", (novo_saldo, email_input))
        connection.commit()

        print("O saldo foi aumentado com sucesso!")
        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-----------------------------------------------------------------------------------------------------------------------
#FUNÇÕES EXTRA DE ADMIN
#-----------------------------------------------------------------------------------------------------------------------


def get_id_produtora(nome):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT id FROM produtora WHERE nome = %s;", (nome,))
        for linha in cursor.fetchall():
            return linha[0]
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------------------------------


def cria_produtora(produtora):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO produtora VALUES (nextval('produtora_id_sequence'),%s);", (produtora,))
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-----------------------------------------------------------------------------------------------------------------------


def get_id_ator(nome):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT id FROM atores WHERE nome = %s;", (nome,))
        for linha in cursor.fetchall():
            return linha[0]
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------------------------------


def cria_ator(ator):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO atores VALUES (nextval('atores_id_sequence'),%s);", (ator,))
        connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#--------------------------------------------------------------------------------------------------------------------------


def get_id_realizador(nome):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT id FROM realizadores WHERE nome = %s;", (nome,))
        for linha in cursor.fetchall():
            return linha[0]

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-----------------------------------------------------------------------------------------------------------------------


def cria_realizador(realizador):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO realizadores VALUES (nextval('realizadores_id_sequence'),%s);", (realizador,))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-------------------------------------------------------------------------------------------------------------------------


def get_id_artigo(titulo):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT id FROM artigos WHERE titulo = %s;", (titulo,))
        for linha in cursor.fetchall():
            return linha[0]

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------------------------------


def insere_atores_artigo(id_artigo, id_atores):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO atores_artigos VALUES (%s,%s);", (id_atores, id_artigo))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------------------------------


def insere_realizadores_artigo(id_artigo, id_realizadores):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("INSERT INTO realizadores_artigos VALUES (%s,%s);", (id_realizadores, id_artigo))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-----------------------------------------------------------------------------------------------------------------------


def ver_historico_preco():  # Função para ver historico de preco de um artigo
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        id_artigo = []  # Lista com id's de artigos
        cursor.execute("SELECT id FROM artigos WHERE em_stock = true")
        for linha in cursor.fetchall():
            id_artigo.append(linha[0])  # Insere na lista os id's dos artigos que estão disponiveis
        print(id_artigo)  # Apresenta os artigos disponiveis
        while True:
            id = int(input("Insira o id do artigo que pretende ver o historico de preco: "))
            if id not in id_artigo:
                print("Não é possivel selecionar esse artigo. Esse artigo nao se encontra disponivel ou nao existe!")
            else:
                break
        cursor.execute("SELECT preco,data FROM historico_preco WHERE artigos_id = %s;", (id,))
        for linha in cursor.fetchall():
            preco = linha[0]
            data = linha[1]

            print("Preco: ", preco, "Data de modificacao: \t", data.strftime("%A, %d %B %Y %I:%M%p"))

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-----------------------------------------------------------------------------------------------------------------------
#FUNÇÕES DE ESTATISTICA DE ADMIN
#-----------------------------------------------------------------------------------------------------------------------


def total_clientes():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente")
        count = cursor.rowcount
        print("Nº total de clientes registados: ", count)
        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-------------------------------------------------------------------------------------------------------------------------


def total_artigos():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM artigos")
        count = cursor.rowcount
        print("Nº total de artigos registados no sistema: ", count)
        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------------------------------


def valor_artigos_alugados_nestemomento():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT sum(preco) FROM aluguer WHERE confirmacao=true;")
        for linha in cursor.fetchall():
            print("O valor total de todos os artigos alugados neste momento é ", linha[0],"€")

        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------------------------------


def valor_alugueres():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT sum(preco) FROM aluguer WHERE confirmacao=true;")
        for linha in cursor.fetchall():
            print("O valor total de alugueres é ", linha[0],"€")

        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#-------------------------------------------------------------------------------------------------------------------------


def total_artigos_tipo():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM artigos WHERE tipo='serie';")
        count = cursor.rowcount
        print("Nº total de artigos do tipo serie: ", count)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM artigos WHERE tipo='filme';")
        count2 = cursor.rowcount
        print("Nº total de artigos do tipo filme: ", count2)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM artigos WHERE tipo='documentario';")
        count3 = cursor.rowcount
        print("Nº total de artigos do tipo documentario: ", count3)

        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------------------------------

def artigos_mais_alugados():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        print()
        print("Ordem decrescente de artigos mais alugados:")
        cursor = connection.cursor()
        cursor.execute("SELECT artigos_id, COUNT(*) FROM aluguer GROUP BY artigos_id ORDER BY COUNT(*) DESC, artigos_id ASC")
        for linha in cursor.fetchall():
            artigos_id = linha[0]
            contador = linha[1]
            cursor.execute("SELECT titulo FROM artigos WHERE id=%s",(artigos_id,))
            for linha2 in cursor.fetchall():
                titulo = linha2[0]

            print("ID:\t", artigos_id,"\tTitulo: ", titulo, "\tNumero de alugueres: ", contador)

        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

#-------------------------------------------------------------------------------------------------------------------------


def artigos_falta_stock():  # Artigos indisponiveis ("em_stock"=false)
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()
        cursor.execute("SELECT titulo, id FROM artigos WHERE em_stock=false;")
        if cursor.rowcount == 0:
            print("Não existe nenhum artigo com falta de stock!")
            return

        for linha in cursor.fetchall():
            print("Titulo: ", linha[0], "ID: ", linha[1])

        print()

    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


#------------------------------------------------------------------------------------------------- > PESQUISAS

def pesquisa_atores(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()

        op1 = input("Insira o nome do ator: ")
        cursor.execute("SELECT artigos_id, artigos.titulo, artigos.id, artigos.preco, artigos.tipo "
                       "FROM atores_artigos "
                       "INNER JOIN artigos ON atores_artigos.artigos_id = artigos.id "
                       "WHERE atores_id IN (SELECT id FROM atores WHERE nome LIKE '%"+op1+"%') "
                        "ORDER BY {0} {1}".format(crit,ord))
        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            titulo = linha[1]
            id = linha[2]
            preco = linha[3]
            tipo = linha[4]
            print("\nID:", id)
            print("Tipo:", tipo)
            print("Titulo:", titulo)
            print("Preco:", preco,"€")
        '''while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break'''

        if i == 0:
            print("\n!Não existem artigos deste atores!")
        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break

        menu.menu_cliente(user)


    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()


def pesquisa_atores_aluguer(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()



        op1 = input("Insira o nome do ator: ")
        print()
        cursor.execute("SELECT atores_artigos.artigos_id, artigos.titulo, aluguer.id, aluguer.artigos_id, aluguer.data,"
                       "aluguer.preco, artigos.tipo FROM atores_artigos "
                       "INNER JOIN artigos ON atores_artigos.artigos_id=artigos.id "
                       "INNER JOIN aluguer ON atores_artigos.artigos_id = aluguer.artigos_id "
                       "WHERE atores_id IN (SELECT id FROM atores WHERE nome LIKE '%"+op1+"%')"
                       "AND aluguer.confirmacao = true AND cliente_utilizador_email = '{0}'"
                       "ORDER BY {1} {2} ".format(user,crit,ord))
        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            artigos_id = linha[0]
            titulo = linha[1]
            id_aluguer =  linha[2]
            data = linha[4]
            valor = linha[5]
            tipo = linha[6]
            print("\nID do aluguer: ", id_aluguer)
            print("ID do artigo: ", artigos_id)
            print("Titulo do artigo: ", titulo)
            print("Preco: ", valor,"€")
            print("Tipo:", tipo)
            print("Data em que foi alugado: ", data)
        '''while True:
            move_on = input("\nEnter para continuar")
            if move_on == '':
                break'''

        if i == 0:
            print("Não comprou artigos desse ator")

        while True:
            move_on = input("\nEnter para continuar")
            if move_on == '':
                break
        menu.menu_cliente(user)
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()

def pesquisa_realizadores(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()

        op1 = input("\nInsira o nome do realizadores: ")
        cursor.execute("SELECT artigos_id, artigos.titulo, artigos.id, artigos.preco, artigos.tipo "
                       "FROM realizadores_artigos "
                       "INNER JOIN artigos ON realizadores_artigos.artigos_id = artigos.id "
                       "WHERE realizadores_id IN (SELECT id FROM realizadores WHERE nome LIKE '%"+op1+"%') "
                        "ORDER BY {0} {1}".format(crit,ord))
        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            titulo = linha[1]
            id = linha[2]
            preco = linha[3]
            tipo = linha[4]
            print("\nID:",id)
            print("Tipo:",tipo)
            print("Titulo:",titulo)
            print("Preco:",preco,"€")


        if i == 0:
            print("!Não existem artigos deste realizador!")

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        menu.menu_cliente(user)


    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def pesquisa_realizadores_aluguer(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()



        op1 = input("Insira o nome do realizador: ")
        print()
        cursor.execute("SELECT realizadores_artigos.artigos_id, artigos.titulo, aluguer.id, aluguer.artigos_id, aluguer.data,"
                       "aluguer.preco, artigos.tipo FROM realizadores_artigos "
                       "INNER JOIN artigos ON realizadores_artigos.artigos_id=artigos.id "
                       "INNER JOIN aluguer ON realizadores_artigos.artigos_id = aluguer.artigos_id "
                       "WHERE realizadores_id IN (SELECT id FROM realizadores WHERE nome LIKE '%"+op1+"%')"
                       "AND aluguer.confirmacao = true AND cliente_utilizador_email = '{0}'"
                       "ORDER BY {1} {2} ".format(user,crit,ord))
        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            artigos_id = linha[0]
            titulo = linha[1]
            id_aluguer = linha[2]
            data = linha[4]
            valor = linha[5]
            tipo = linha[6]
            print("\nID do aluguer: ", id_aluguer)
            print("ID do artigo: ", artigos_id)
            print("Titulo do artigo: ", titulo)
            print("Tipo:", tipo)
            print("Preco: ", valor,"€")
            print("Data em que foi alugado: ", data)


        if i == 0:
            print("Não comprou artigos desse realizador")

        while True:
            move_on = input("\nEnter para continuar")
            if move_on == '':
                break

        menu.menu_cliente(user)
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()

def pesquisa_produtora(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()

        op1 = input("\nInsira o nome da Produtora: ")
        cursor.execute("SELECT artigos.titulo, artigos.id, artigos.preco, artigos.tipo "
                       "FROM artigos "
                       "WHERE produtora_id IN (SELECT id FROM produtora WHERE nome LIKE '%"+op1+"%') "
                        "ORDER BY {0} {1}".format(crit,ord))
        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            titulo = linha[0]
            id = linha[1]
            preco = linha[2]
            tipo = linha[3]
            print("\nID:",id)
            print("Tipo:",tipo)
            print("Titulo:",titulo)
            print("Preco:",preco,"€")


        if i == 0:
            print("!Não existem artigos desta Produtora!")

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        menu.menu_cliente(user)


    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def pesquisa_produtora_aluguer(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()



        op1 = input("Insira o nome do Produtora: ")
        print()
        cursor.execute("SELECT artigos.id, artigos.titulo, aluguer.id, aluguer.artigos_id, aluguer.data,"
                       "aluguer.preco, artigos.tipo FROM artigos "
                       "INNER JOIN aluguer ON artigos.id = aluguer.artigos_id "
                       "WHERE produtora_id IN (SELECT id FROM produtora WHERE nome LIKE '%"+op1+"%')"
                       "AND aluguer.confirmacao = true AND cliente_utilizador_email = '{0}'"
                       "ORDER BY {1} {2} ".format(user,crit,ord))
        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            artigos_id = linha[0]
            titulo = linha[1]
            id_aluguer =  linha[2]
            data = linha[4]
            valor = linha[5]
            tipo = linha[6]
            print("\nID do aluguer: ", id_aluguer)
            print("ID do artigo: ", artigos_id)
            print("Titulo do artigo: ", titulo)
            print("Tipo:", tipo)
            print("Preco: ", valor,"€")
            print("Data em que foi alugado: ", data)


        if i == 0:
            print("Não comprou artigos dessa Produtora")

        while True:
            move_on = input("\nEnter para continuar")
            if move_on == '':
                break

        menu.menu_cliente(user)
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()

def pesquisa_titulo(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()

        op1 = input("\nInsira o titulo do artigo: ")
        cursor.execute("SELECT titulo, id, preco, tipo FROM artigos WHERE titulo LIKE '%" + op1 + "%' ORDER BY {0} {1};".format(crit, ord))

        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            titulo = linha[0]
            id = linha[1]
            preco = linha[2]
            tipo = linha[3]
            print("\nID:",id)
            print("Tipo:",tipo)
            print("Titulo:",titulo)
            print("Preco:",preco,"€")


        if i == 0:
            print("!Não existem artigos com esse titulo!")

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        menu.menu_cliente(user)


    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def pesquisa_titulo_aluguer(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()



        op1 = input("Insira o titulo do artigo: ")
        print()
        cursor.execute("SELECT artigos.id, artigos.titulo, aluguer.id, aluguer.artigos_id, aluguer.data,"
                       "aluguer.preco, artigos.tipo FROM artigos "
                       "INNER JOIN aluguer ON artigos.id = aluguer.artigos_id "
                       "WHERE artigos.titulo LIKE '%"+op1+"%' "
                       "AND aluguer.confirmacao = true AND cliente_utilizador_email = '{0}'"
                       "ORDER BY artigos.{1} {2} ".format(user,crit,ord))
        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            artigos_id = linha[0]
            titulo = linha[1]
            id_aluguer =  linha[2]
            data = linha[4]
            valor = linha[5]
            tipo = linha[6]
            print("\nID do aluguer: ", id_aluguer)
            print("ID do artigo: ", artigos_id)
            print("Titulo do artigo: ", titulo)
            print("Tipo:", tipo)
            print("Preco: ", valor,"€")
            print("Data em que foi alugado: ", data)


        if i == 0:
            print("Não comprou artigos com esse titulo")

        while True:
            move_on = input("\nEnter para continuar")
            if move_on == '':
                break

        menu.menu_cliente(user)
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()

def pesquisa_tipo(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()

        op1 = input("\nInsira o tipo do artigo: ")
        cursor.execute("SELECT titulo, id, preco, tipo FROM artigos WHERE tipo LIKE '%" + op1 + "%' ORDER BY {0} {1};".format(crit, ord))

        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            titulo = linha[0]
            id = linha[1]
            preco = linha[2]
            tipo = linha[3]
            print("\nID:",id)
            print("Tipo:",tipo)
            print("Titulo:",titulo)
            print("Preco:",preco,"€")


        if i == 0:
            print("!Não existem artigos desse tipo!")

        while True:
            move_on = input("Enter para continuar")
            if move_on == '':
                break
        menu.menu_cliente(user)


    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()

def pesquisa_tipo_aluguer(user,crit,ord):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="postgres",
                                      host="localhost",
                                      port="5432",
                                      database="Projecto_BD")

        cursor = connection.cursor()



        op1 = input("Insira o tipo do artigo: ")
        print()
        cursor.execute("SELECT artigos.id, artigos.titulo, aluguer.id, aluguer.artigos_id, aluguer.data,"
                       "aluguer.preco, artigos.tipo FROM artigos "
                       "INNER JOIN aluguer ON artigos.id = aluguer.artigos_id "
                       "WHERE artigos.tipo LIKE '%"+op1+"%' "
                       "AND aluguer.confirmacao = true AND cliente_utilizador_email = '{0}'"
                       "ORDER BY artigos.{1} {2} ".format(user,crit,ord))
        i = 0
        for linha in cursor.fetchall():
            i = cursor.rowcount
            artigos_id = linha[0]
            titulo = linha[1]
            id_aluguer =  linha[2]
            data = linha[4]
            valor = linha[5]
            tipo = linha[6]
            print("\nID do aluguer: ", id_aluguer)
            print("ID do artigo: ", artigos_id)
            print("Titulo do artigo: ", titulo)
            print("Tipo:", tipo)
            print("Preco: ", valor,"€")
            print("Data em que foi alugado: ", data)


        if i == 0:
            print("Não comprou artigos desse tipo")

        while True:
            move_on = input("\nEnter para continuar")
            if move_on == '':
                break

        menu.menu_cliente(user)
    except (Exception, psycopg2.Error) as error:
        print("Error ", error)

    finally:
        # closing database connection.
        if(connection):
            cursor.close()
            connection.close()
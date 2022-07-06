#!/bin/env python3

from datetime import date
import datetime
''' Aqui definimos o maximo de falhas avaliadas '''
MAX_ITEMS_LISTA_VAZADOS = 6
MIN_ITEMS_LISTA_VAZADOS = 1
'''Lista das falhas reportadas atribuimos o limite para manter o controle no experimento'''
senha = 'senha'
email = 'email'
ajudaSenha = 'ajuda de senha'
telefone = 'telefone'
nome = 'nome'
ip = 'ip'
''' Listas das empresas'''

listaDeFalhas = [
    "nome_empresa:Adobe;descricao:Teve em 2013, 38 milhões de dados vazados confirmados pela própria empresa. Os invasores tiveram acesso ao servidor, vazando informações dos clientes;data:20/01/2013;informacoes_vazadas:" +
    senha+','+email+','+ajudaSenha+',' + ip+','+telefone+','+nome,
    "nome_empresa:Catho;descricao:Em aproximadamente março de 2020, o site de recrutamento brasileiro Catho foi comprometido e, posteriormente, apareceu ao lado de outros 20 sites violados listados para venda em um mercado da dark web. A violação incluiu quase 11 milhões de registros com 1,2 milhão de endereços de e-mail únicos. Nomes, nomes de usuário e senhas de texto simples também foram expostos. Os dados foram fornecidos ao HIBP por breachbase.pw.;data:20/08/2020;informacoes_vazadas:" +
    email+','+ip+','+telefone+','+nome,
    "nome_empresa:Descomplica;descricao:Em março de 2021, a empresa brasileira EdTech Descomplica sofreu uma violação de dados que foi posteriormente postada em um fórum popular de hackers. Os dados incluíam quase 5 milhões de endereços de e-mail, nomes, os primeiros 6 e últimos 4 dígitos e a data de validade dos cartões de crédito, históricos de compras e hashes de senha.;data:20/01/2021;informacoes_vazadas:" +
    ip+','+telefone+','+nome,
    "nome_empresa:Facebook;descricao:Uma das maiores redes sociais no mundo teve 87 milhões de dados vazados em 2016. O caso repercutiu ainda mais quando a Cambridge Analytica foi acusada de compartilhar as informações dos usuários para influenciar os resultados das eleições daquele ano;;data:20/04/2020;informacoes_vazadas:" +
    ip+','+telefone,
    "nome_empresa:GooglePlus;descricao: Em 2018 o Google+ expôs os usuários a dois vazamentos de dados. No primeiro, 500 mil usuários foram atingidos, no segundo, 50 milhões. A empresa encerrou as atividades do aplicativo e explicou que o vazamento só foi possível por conta de um erro na interface;data:08/11/2018;informacoes_vazadas:" +
    senha+','+email+','+ajudaSenha+',' + ip+','+telefone+','+nome,
    "nome_empresa:Uber;descricao:Em 2016 a empresa teve informações de clientes e motoristas vazados, mas só assumiu em 2017. Devido ao encobrimento do caso, além de ter pago 100 mil dólares para os invasores, a Uber teve que desembolsar 148 milhões de dólares em multa. No total foram 57 milhões de dados vazados, entre eles nome, telefone, número de cartão e endereço de e-mail;data:06/09/2016;informacoes_vazadas:" +
    email+','+ip+','+telefone+','+nome,
    "nome_empresa:Yahoo;descricao:Os ataques contra a empresa ocorreram em 2013 e 2017 contando ao final com 3 bilhões de usuários afetados em todo o mundo. ;data:20/11/2013;informacoes_vazadas:" +
    ip+','+telefone+','+nome,
    "nome_empresa:Target;descricao:Os usuários afetados pelo vazamento de dados da empresa ultrapassou 40 milhões. O caso aconteceu em 2013 e teve muitos prejuízos para os clientes, entre as informações pessoais vazadas ;data:18/04/2013;informacoes_vazadas:" +
    ip+','+telefone,
    "nome_empresa:PlayStation Network;descricao:No ano de 2011 a empresa on-line de jogos teve dados de consumidores vazados, entre eles nome, endereço de e-mail e localização. O vazamento de dados atingiu 77 milhões de usuários e manteve o site fora do ar por dias;data:30/07/2011;informacoes_vazadas:" +
    senha+','+email+','+ajudaSenha+',' + ip+','+telefone+','+nome,
    "nome_empresa:Dell;descricao:A empresa que é uma das maiores de distribuição de computadores nos Estados Unidos foi alvo, em 2018, de um ciberataque que expôs cerca de 100.000 dados sensíveis de seus clientes.;data:09/03/2018;informacoes_vazadas:" +
    email+','+ip+','+telefone+','+nome,
    "nome_empresa:C&A;descricao:A C&A é uma das maiores redes varejistas do Brasil e em 2018 viu cerca de 2 milhões de dados de clientes cadastrados no sistema de vales-presente e trocas de suas lojas vazarem depois de um ciberataque realizado por hackers. ;data:13/09/2018;informacoes_vazadas:" +
    ip+','+telefone+','+nome,
    "nome_empresa:Banco Inter;descricao:Em 2018, o Banco Inter, um dos pioneiros em oferecer contas digitais no país, registrou um vazamento que deixou vulnerável cerca de 19 mil correntistas.;data:02/05/2018;informacoes_vazadas:" +
    ip+','+telefone,
    "nome_empresa:McDonald's;descricao:Em outubro de 2019, mais de 2 milhões de registros sensíveis da rede McDonald’s Brasil vazaram e foi possível acessar dados pessoais como nome completo.;data:08/10/2019;informacoes_vazadas:" +
    senha+','+email+','+ajudaSenha+',' + ip+','+telefone+','+nome,
    "nome_empresa:ebay;descricao:Em maio de 2014, um vazamento de dados expôs as contas de 145 milhões de usuários (nomes, endereços, datas de nascimento e senhas criptografadas) da eBay, uma das maiores empresas de comércio eletrônico do mundo.;data:07/02/2014;informacoes_vazadas:" +
    email+','+ip+','+telefone+','+nome,
    "nome_empresa:Sony Pictures;descricao:Em 2014, a Sony Pictures, que está no comando das produções cinematográficas, teve os dados de funcionários e executivos vazados.;data:20/08/2014;informacoes_vazadas:" +
    ip+','+telefone+','+nome,
    "nome_empresa:Steam;descricao: Steam sofreu um ataque ciberpirata no ano de 2011. Os criminosos invadiram os servidores da Valve e tiveram acesso a informações pessoais como, senhas, emails, telefone.;data:03/09/2011;informacoes_vazadas:" +
    senha+','+email+','+telefone,
    "nome_empresa:Netshoes;descricao:No final de 2017 e início de 2018, a organização teve duas listas de credenciais vazadas com informações de quase 2 milhões de clientes. Entre os dados que foram expostos estavam nome completo, e-mail e outras informações pessoais.;data:20/12/2017;informacoes_vazadas:" +
    senha+','+email+','+ajudaSenha+',' + ip+','+telefone+','+nome,
    "nome_empresa:Under Armour;descricao:O ataque não foi direto ao grupo de equipamentos esportivos americano, mas a uma filial da empresa, o MyFitnessPal. O ciberataque atingiu informações de 150 milhões de usuários.;data:04/02/2018;informacoes_vazadas:"+
    email+','+ip+','+telefone+','+nome,
    "nome_empresa:JPMorgan Chase;descricao:o maior banco dos Estados Unidos não escapou das ações dos criminosos digitais. Em 2014, a JPMorgan Chase informou que os dados de 76 milhões de pessoas jurídicas e 7 milhões de empresas foram invadidos por hackers. Entre as informações estavam apenas o nome, ip, telefones.;data:25/04/2014;informacoes_vazadas:" +
    ip+','+telefone+','+nome,
    "nome_empresa:T-Mobile;descricao: Servidores da empresa foram acessados por um “grupo internacional” de hackers através de uma Interface de Programação de Aplicações (API);data:20/08/2018;informacoes_vazadas:" +
    ip+','+telefone,

]
'''Listas para receberem os itens na primeira filtragem'''
listaMaisVulneravel_0 = []
listaMaisVulneravel_1 = []
listaMaisVulneravel_2 = []
listaMaisVulneravel_3 = []
'''Lista de tipos Disponiveis para ordenação ao alterar insira uma
sequencia de array seguindo o padrão ListaMaisVulneravelBy{tipo}_{quantidade}_items = []
'''
listaDeTipos = [senha, email, nome, telefone]
''' Listas para receberem os itens por quantidade'''
listaMaisVulneravelBySenha_6_items = []
listaMaisVulneravelBySenha_5_items = []
listaMaisVulneravelBySenha_4_items = []
listaMaisVulneravelBySenha_3_items = []
listaMaisVulneravelBySenha_2_items = []
listaMaisVulneravelBySenha_1_items = []
listaMaisVulneravelByEmail_6_items = []
listaMaisVulneravelByEmail_5_items = []
listaMaisVulneravelByEmail_4_items = []
listaMaisVulneravelByEmail_3_items = []
listaMaisVulneravelByEmail_2_items = []
listaMaisVulneravelByEmail_1_items = []
listaMaisVulneravelByTelefone_6_items = []
listaMaisVulneravelByTelefone_5_items = []
listaMaisVulneravelByTelefone_4_items = []
listaMaisVulneravelByTelefone_3_items = []
listaMaisVulneravelByTelefone_2_items = []
listaMaisVulneravelByTelefone_1_items = []
listaMaisVulneravelByNome_6_items = []
listaMaisVulneravelByNome_5_items = []
listaMaisVulneravelByNome_4_items = []
listaMaisVulneravelByNome_3_items = []
listaMaisVulneravelByNome_2_items = []
listaMaisVulneravelByNome_1_items = []


# organiza os dados em 4 array por nivel de falha do mais alto pro mais baixo
# gerando listas das entidades com as traits selecionadas
#
print('este programa adotou os seguintes parametros de ordenação')
print('''
1° - senha - ajuda de senha \\\\ aqui consideramos que estao sempre juntos
2° - email
3° - nome
4° - telefone
e como criterio de desempate a data do vazamento
''')
''' Aqui fazemos a primeira separação onde pegamos e inserimos
    nos arrays correspondentes a cada falha  os array nomeados como maisVulneravel_[ 0 - 4 ]'''
for empresa in listaDeFalhas:
    empresaItems = empresa.split(";")
    for items in empresaItems:
        item = items.split(':')

        if item[0] == 'informacoes_vazadas':

            if(senha in item[1] and ajudaSenha in item[1]):
                ''' Aqui inserimos no array de senha e ajuda de senha '''
                listaMaisVulneravel_0.insert(0, empresa)
            elif(telefone in item[1]):
                ''' Aqui inserimos no array de telefone'''
                listaMaisVulneravel_1.insert(0, empresa)
            elif(nome in item[1]):
                ''' Aqui inserimos no array de nome'''
                listaMaisVulneravel_2.insert(0, empresa)
            elif(email in item[1]):
                ''' Aqui inserimos no array de email '''
                listaMaisVulneravel_3.insert(0, empresa)


def ordena_por_quantidade_e_tipo(array, tipo):
    ''' Aqui verificamos a quantidade de falhas e ordenamos
        por quantidade os arrays separados por tipo'''
    for empresa in array:
        empresaItems = empresa.split(";")
        for items in empresaItems:
            item = items.split(':')
            if item[0] == 'informacoes_vazadas':
                informacoes_vazadas = item[1].split(',')
                for qnt in range(MIN_ITEMS_LISTA_VAZADOS, MAX_ITEMS_LISTA_VAZADOS+1):
                    if(len(informacoes_vazadas) == qnt):
                        '''Aqui verificamos a quantidade de falhas e inserimos no
                        array apropriado  para depois ordenarmos por data
                        '''
                        #  a funcão global permite chamar o array ou função
                        # passando a string do nome dela permintindo uma
                        # composição conforme abaixo
                        globals()[
                            'listaMaisVulneravelBy'+tipo.capitalize() + '_'+str(qnt)+'_items'].append(empresa)


def retorna_data(array_empresa):
    ''' aqui retornamos a data em formato inteiro do timestamp'''
    empresaItems = array_empresa.split(';')
    for items in empresaItems:
        item = items.split(':')
        if item[0] == 'data':
            element = datetime.datetime.strptime(item[1], "%d/%m/%Y")
            timestamp = datetime.datetime.timestamp(element)
            return int(round(timestamp))


def ordena_por_data_tipo(array):
    ''' Aqui verificamos a data das falhas e ordenamos'''
    if(len(array) >= 2):
        for n in range(len(array)-1, 0, -1):
            for i in range(n):
                # print(array[i])
                # print(array[i+1])
                data1 = retorna_data(array[i])
                data2 = retorna_data(array[i+1])
                if data1 < data2:
                    # swapping data if the element is less than next element in the array
                    array[i], array[i + 1] = array[i + 1], array[i]

    return array


''' aqui ordenamos os arrays separados por tipos de vulnerabilidade por quantidades de vulnerabilidades'''
ordena_por_quantidade_e_tipo(listaMaisVulneravel_0, senha)
ordena_por_quantidade_e_tipo(listaMaisVulneravel_1, telefone)
ordena_por_quantidade_e_tipo(listaMaisVulneravel_2, nome)
ordena_por_quantidade_e_tipo(listaMaisVulneravel_3, email)

for tipo in listaDeTipos:
    for qnt in range(1, MAX_ITEMS_LISTA_VAZADOS+1):
        ''' aqui atribuimos o array ordenado por data a ele mesmo atualizando o proprio'''
        globals()[
            'listaMaisVulneravelBy'+tipo.capitalize() + '_'+str(qnt)+'_items'] = ordena_por_data_tipo(globals()[
                'listaMaisVulneravelBy'+tipo.capitalize() + '_'+str(qnt)+'_items'])


listaPorSenha = listaMaisVulneravelBySenha_6_items + \
    listaMaisVulneravelBySenha_5_items + \
    listaMaisVulneravelBySenha_4_items + \
    listaMaisVulneravelBySenha_3_items + \
    listaMaisVulneravelBySenha_2_items + \
    listaMaisVulneravelBySenha_1_items
listaPorEmail = listaMaisVulneravelByEmail_6_items + \
    listaMaisVulneravelByEmail_5_items + \
    listaMaisVulneravelByEmail_4_items + \
    listaMaisVulneravelByEmail_3_items + \
    listaMaisVulneravelByEmail_2_items + \
    listaMaisVulneravelByEmail_1_items
listaPorNome = listaMaisVulneravelByNome_6_items + \
    listaMaisVulneravelByNome_5_items + \
    listaMaisVulneravelByNome_4_items + \
    listaMaisVulneravelByNome_3_items + \
    listaMaisVulneravelByNome_2_items + \
    listaMaisVulneravelByNome_1_items
listaPorTelefone = listaMaisVulneravelByTelefone_6_items + \
    listaMaisVulneravelByTelefone_5_items + \
    listaMaisVulneravelByTelefone_4_items + \
    listaMaisVulneravelByTelefone_3_items + \
    listaMaisVulneravelByTelefone_2_items + \
    listaMaisVulneravelByTelefone_1_items

listaOrdenada = listaPorSenha + listaPorTelefone + listaPorNome + listaPorEmail

for linha in range(len(listaOrdenada)):
    print('''
    posição {}:
    empresa: {}    
    '''.format(linha, listaOrdenada[linha]))

#!/usr/bin/python3
#1 - lista_dados_por_cpf()
#Listar os órgãos, códigos e editais dos concursos públicos que se
#encaixam no perfil do candidato tamando como base o CPF do candidato

#2 - lista_dados_por_codigo()
#Listar o nome, data de nascimento e o CPF dos candidatos que se encaixam
#no perfil do concurso tomando com base o Código do Concurso do concurso público


#Linguagem últilizada: python3

#importação módulos
import re, os

#verifica se existe no mesmo diretório os arquivos de texto para a 
#referida pesquisa
if 'concursos.txt' not in os.listdir('.'):
	input('O arquivo concursos.txt não está no mesmo diretório')
	exit(0)
elif 'candidatos.txt' not in os.listdir('.'):
	input('Arquivo de texto candidatos.txt não encontrado')
	exit(0)

#Função para listar órgão, códigos e editais
#recebe um argumento (CPF - string) no seguinte formato: 123.456.789-00
def lista_dados_por_cpf():
    #variável para contagem
    count = 1
    #variável para receber o CPF passado pelo usuário
    cpf = input('Insira aqui um CPF no formato 123.456.789-00 para iniciar a busca: ')
    while len(cpf) < 14:
        print('Valor inserido inválido. Tente novamente')
        cpf = input('Insira aqui um CPF no formato 123.456.789-00 - ')

    #apenas abre o arquivo de texto e o coloca em uma lista    
    with open('candidatos.txt') as cand:
        candidatos = cand.readlines()

    #apenas abre o arquivo de texto e o coloca em uma lista
    with open('concursos.txt') as conc:
        concursos = conc.readlines()

    #nesse seguimento de laço "for" é que consigo verificar
    #os concursos compátiveis com a profissão do candidato por CPF
    lista_concursos = []
    for can in candidatos:
        if cpf in can:
            prof = re.search('\[.*', can).group().replace('[','').replace(']','')
            for con in concursos:
                if '[' in con:
                    edital = re.search('../....', con).group()
                for profp in prof.split(','):
                    if profp.startswith(' '):
                        profp = profp.replace(' ','', 1)
                    if profp in con and edital not in lista_concursos:
                        lista_concursos.append(edital)
                        print(count, '-', con.replace(re.search('\[.*' ,con).group(), '').strip())
                        count += 1
    if count > 1:
        print('Esses são os orgãos, códigos e editais compátiveis com o cpf',cpf,'\n')
    else:
        print('Nada encontrado.\n')




#função para listar o nome, data de nascimento e o CPF dos candidatos que
#se encaixam no perfil do concurso tomando com base o Código do Concurso do concurso público
def lista_dados_por_codigo():
    #variável para contar
    count = 1
    #variável onde guardará o codgio passado pelo usuário
    codigo = input('Insira um código para iniciar a pesquisa por código: ')
    if len(codigo) < 6:
        print('Valor inserido é inválido. Tente novamente')
        codigo = input('Insira um código para iniciar a pesquisa por codigo: ')

    #apenas abre o arquivo de texto e o coloca em uma lista    
    with open('candidatos.txt') as cand:
        candidatos = cand.readlines()

    #apenas abre o arquivo de texto e o coloca em uma lista
    with open('concursos.txt') as conc:
        concursos = conc.readlines()

    lista_candidatos = []

    #seguimento de laço "for" para verificar
    #os concursos compátiveis com os candidados buscando por código do concurso
    #obs:Se houver códigos repetidos com editais diferentes, serão mecionados.
    for con in concursos:
        if codigo in con:
            profissao = re.search('\[.*', con).group().replace('[','').replace(']','')
            for profi in profissao.split(','):
                for can in candidatos:
                    if '[' in can:
                        lista_cpf = re.search('...........-..', can).group()
                    if profi.startswith(' '):
                        profi = profi.replace(' ','', 1)
                    if profi in can and lista_cpf not in lista_candidatos:
                        lista_candidatos.append(lista_cpf)
                        print(count, '-',can.replace(re.search('\[.*' ,can).group(), '').strip())
                        count += 1
    if count > 1:
        input('Acima estão os candidatos compátiveis com o código ('+codigo+') passado.')
    else:
        input('Nenhum compátivel.\nEnter para terminar.')


#apenas executando as duas funções cridadas acima
lista_dados_por_cpf()
lista_dados_por_codigo()

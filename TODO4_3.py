# Nome: Mariana Lobão.
# TODO4

dict_informações_candidatos = dict()

quantidade_candidatos_registro = int(input(
    'Digite a quantidade de candidatos que deseja registrar em nosso sistema: '))

contador = 0

while contador < quantidade_candidatos_registro:
    nomecandidato = input('Digite o nome do candidato: ').lower()
    vagacandidato = input(
        'Digite a vaga para qual gostaria de registrar o candidato: ').lower()
    resumocandidato = input(
        'Digite as palavras chaves presentes no resumo do currículo do candidato: ').lower()
    lista_vaga_resumo = []
    lista_vaga_resumo = [vagacandidato, resumocandidato]
    dict_informações_candidatos[nomecandidato] = lista_vaga_resumo
    contador = contador + 1

candidados_analistadedados = dict()
candidatos_cientistadedados = dict()
analistadedados_requisitos = dict()
cientistadedados_requistos = dict()

for chave in dict_informações_candidatos:
    if 'analista' in dict_informações_candidatos[chave][0]:
        candidados_analistadedados[chave] = dict_informações_candidatos[chave]
    elif 'cientista' in dict_informações_candidatos[chave][0]:
        candidatos_cientistadedados[chave] = dict_informações_candidatos[chave]

for chave in candidados_analistadedados:
    if 'python' in candidados_analistadedados[chave][1] or 'power bi' in candidados_analistadedados[chave][1] or 'sql' in candidados_analistadedados[chave][1] or 'boa comunicação' in candidados_analistadedados[chave][1]:
        analistadedados_requisitos[chave] = candidados_analistadedados[chave]

for chave in candidatos_cientistadedados:
    if 'python' in candidatos_cientistadedados[chave][1] or 'banco de dados' in candidatos_cientistadedados[chave][1] or 'machine learning' in candidatos_cientistadedados[chave][1] or 'resolução de problemas' in candidatos_cientistadedados[chave][1] or 'estatística' in candidatos_cientistadedados[chave][1]:
        cientistadedados_requistos[chave] = candidatos_cientistadedados[chave]

print('---------------------')

print('Os candidatos que se candidataram a vaga de Analista de dados foram: ',
      candidados_analistadedados)

print('Os candidatos que se candidataram para a vaga de Ciêntista de dados foram: ',
      candidatos_cientistadedados)

print('Os candidatos para a vaga de Analista de Dados que atendem aos requisitos são: ',
      analistadedados_requisitos)

print('Os candidatos para a vaga de Cientista de Dados que atendem aos requisitos são: ',
      cientistadedados_requistos)

# filtro_resultado: dict = {"fernando":{"localizacao":"Belo Horizonte","tipo_do_imovel":"Apartamento","numero_de_quartos":{"1+":"","2+":"","3+":"3","4+":""},"valor":{"minimo":"265000","maximo":"300000"},"area":{"minimo":"24,00","maximo":"65,00"},"numero_vagas":{"1+":"1","2+":"","3+":"","4+":""}}}

# def ordena_remove_vazio_json(lista: list) ->list:
#     json: dict = {}
#     try:
#         for i in lista:
#             for u in lista[i]:
#                 itens: list = lista[i][u]
#                 if type(itens) == dict:
#                     iten2: dict = {chave: valor for chave, valor in itens.items() if valor}
#                     json[u] = iten2
#                 else:
#                     json[u] = itens
#     except:
#         pass
#     return json

# filtro = ordena_remove_vazio_json(filtro_resultado)
# print(filtro)

## EXERCICIOS

# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

#1:
# lista = [1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(lista)):
#     print(lista[i]**2)

#2:
# lista = ["Python", "Java", "C++", "JavaScript"]
# lista.remove("C++")
# lista.append("Ruby")
# print(lista)

#3:
# continuar: bool = True
# d = {}
# lista = {}
# while continuar == True:
#     try:
#         livro: str = str(input("Nome do livro: "))
#         title: str = str(input("Titulo do livro: "))
#         autor: str = str(input("Autor do livro: "))
#         ano: int = int(input("Ano: "))
#         d[livro] = ({"title":title,"autor":autor,"ano":ano})
#         s: str = input("Deseja continuar? (Sim) (Nao) ")
#         if s == "Nao":
#             continuar = False
#             print(d)
#     except:
#         print("Algum erro ocorreu")

#4:
# def contagem_de_caracteres_repetidos(list: list) ->list :
#     try:
#         count = {}
#         for p in list:
#             count[p] = count.get(p,0) + 1
#         return count
#     except:
#         print("Ocorreu um erro")
# print(contagem_de_caracteres_repetidos("fernando fer fernando martins martins"))

#5:
# compras: list = ["maçã", "banana", "cereja"]
# preco: dict =  {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

# def soma_carrinho(list: list,dict:dict)->list:   
#     valor_total: int = 0   
#     for i in range(0,len(list)):
#         valor_total += dict[list[i]]
#     return valor_total
# print(soma_carrinho(compras,preco))

#6: Objetivo: Dada uma lista de emails, remover todos os duplicados.

# emails = ['fernando@gmail.com','fernando@gmail.com','felipe@gmail.com','felipe@gmail.com']
# print(list(set(emails)))

#7: 7. Filtragem de Dados 
#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

# idades = ['18','17','19','32','15']
# for i in range(len(idades)):
#     if int(idades[i]) >= 18:
#         print(idades[i])

#8: 8. Ordenação Personalizada
#Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

# pessoas = [{"nome":"Oernando","idade":"32"},{"nome":"Maria","idade":"36"}]
# pessoas.sort(key=lambda pessoas: pessoas["nome"])
# print(pessoas)

#9: Agregação de Dados
#Objetivo: Dado um conjunto de números, calcular a média.

# obj = [1,2,9,20]
# avger = sum(obj) /len(obj)
# print(avger)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

# v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([v for v in v if v %2 == 0])
# print([v for v in v if v %2 != 0])

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

# produtos = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]

# for i in produtos:
#     if i["id"] == 2:
#         i["preço"]= 120
#         print(produtos)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# d1 = {"n":1}
# d2 = {"n2":2}
# d1.update(d2)
# print(d1)

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
# p = {v for v in estoque if estoque[v] >0}
# print(p)

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

# estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
# print(f"{estoque.keys()}, {estoque.values()}")


# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

txt = "Fernando e muito lindo meu deus"
dc = {}
for i in txt:
    if i in dc:
        dc[i] += 1
    else:
        dc[i]=1
print(dc)
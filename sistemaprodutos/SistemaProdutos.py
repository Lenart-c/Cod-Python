nomes = []
precos = []
qtds = []


def lista_teste():
    produtos_teste = [
        ("Arroz", 20.0, 10),
        ("Feijão", 7.5, 5),
        ("Macarrão", 4.0, 2),
        ("Açúcar", 3.5, 0),
        ("Sal", 2.0, 1),
        ("Óleo", 8.0, 4),
        ("Café", 15.0, 3),
        ("Leite", 5.0, 6),
        ("Pão", 1.5, 0),
        ("Manteiga", 6.0, 2)
    ]
    for nome, preco, quantidade in produtos_teste:
        nomes.append(nome)
        precos.append(preco)
        qtds.append(quantidade)

lista_teste()

def menu():
    print("1 - adicionar produtos")
    print("2 - alterar produtos")
    print("3 - listar produtos")  
    print("4 - adicionar estoque") 
    print("5 - excluir produtos")
    print("0 - sair")

def receber_preco():
    try:
        preco = float(input())
        if preco < 0:
            print("Digite um valor possitivo!")
            return
        return preco
    except ValueError:
        print("Valor Invalido!")
        return

def receber_qtd():
    try:
        qtd = int(input())
        if qtd < 0:
            print("Digite um valor possitivo")
            return
    except ValueError:
        print("Valor invalido!")
        return

def opcao():
    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("Digite um valor valido!")

def escolha_id():
    try:
        idx = int(input("Escolha o ID do item: ")) - 1
        if (idx < 0 or idx >= len(nomes)):
            print("Valor inexistente!")
            return None
        return idx
    except ValueError:
        print("Digite um valor valido!")
        return None

def lista_vazia():
    if not nomes:
        print("Lista Vazia!")
        return True
    return False
    
def produtos(): #ADICIONA O PRODUTO
    
    nome_prod = input("Insera o produto: ") #Passa o nome do produto
    preco_prod = print("Digite um valor: "),receber_preco() #Passa o valor do produto
    qtd_prod = print("Insira a quantidade de produtos: "),receber_qtd() #Passa a quantidade de produtos

    nomes.append(nome_prod) #Adiciona o nome do produto
    precos.append(preco_prod) # Adiciona o preco do produto
    qtds.append(qtd_prod) #Adiciona a quantidades de produto

    print(f"{nome_prod} foi adicionado!")

def listar_prod():

    if lista_vazia():
        return

    for i in range(len(nomes)):
        print(f"Lista: {i+1}, Nome: {nomes[i]}, Preço {precos[i]}, Quantidade: {qtds[i]}")

def adicionar_estoque():
    if lista_vazia():
        return
        
    
    listar_prod()

    id_produto = escolha_id()

    if id_produto is None:
        print("Digite uma lista existente!")
        return
    
    try:
        adiciona_quantidade = int(input("Digite quantos produtos deseja adicionar: "))
        if adiciona_quantidade < 0:
            print("Produtos não pode ser negativo!")
            return
    except ValueError:
        print("Valor invalido!")
        return
    
    qtds[id_produto] += adiciona_quantidade

    print(f"{adiciona_quantidade} foram adicionados ao {nomes[id_produto]}")

def alterar_prod(): #ALTERA O PRODUTO
    if lista_vazia():
        return

    while True:

        print ("--- ESCOLHA UMA OPÇÃO:")
        print("1 - Alterar nome ")
        print("2 - Alterar preço")
        print("3 - Alterar quantidade")
        print("0 - sair")

        op = opcao()
        

        match op:
            case 1: #ALTERA O NOME   
                listar_prod()
                produto_id = escolha_id()       
                if produto_id is None:
                    return                              
                new_nome = input("Escolha o novo nome: ") 
                if (new_nome.replace(" ", "").isalpha()):
                    nomes[produto_id] = new_nome
                    print(f"Nome foi alterado para {new_nome}")
                else: print("Digite um nome valido!")
            case 2: #ALTERA O PREÇO 
                listar_prod()
                produto_id = escolha_id()
                if produto_id is None:
                    return
                new_preco = print("Digite o novo preço: "), receber_preco()
                precos[produto_id] = new_preco
                print(f"Preço de {nomes[produto_id]} foi alterado")
            case 3: #ALTERA A QUANTIDADE
                listar_prod()
                produto_id = escolha_id()
                if produto_id is None:
                    return
                new_qtd = print("Digite a nova quantidade: "), receber_qtd()         
                qtds[produto_id] = new_qtd
                print(f"Quantidade de {nomes[produto_id]} foi alterada")
            case 0: #SAIR
                print("saindo...")
                return False
            case _: #DEFALT
                print("Digite uma opção valida!")              

def excluir_prod(): #Exclui o produto
    global nomes, precos, qtds

    if lista_vazia():
        return
    
    listar_prod()

    produto_id = escolha_id()

    if produto_id is None:
        return

    produto_removido = nomes[produto_id]

    novos_nome = []
    novos_preco = []
    novos_qtd = []

    for i in range(len(nomes)):
        if i != produto_id:
            novos_nome.append(nomes[i]) 
            novos_preco.append(precos[i])
            novos_qtd.append(qtds[i])

    nomes = []
    precos = []
    qtds = []

    for i in range(len(novos_nome)):
        nomes.append(novos_nome[i])
        precos.append(novos_preco[i])
        qtds.append(novos_qtd[i])

    print(f"{produto_removido} foi excluido com sucesso!")

def main():
    while True:

        menu()
        op = opcao()

        match op:
            case 1:
                produtos()
            case 2:
                alterar_prod()
            case 3:
                listar_prod()
            case 4:
                adicionar_estoque()
            case 5:
                excluir_prod()
            case 0:
                print("saindo...")
                return False
            case _:
                print("Informe uma opção válida")
                

if __name__ == '__main__':
    main()

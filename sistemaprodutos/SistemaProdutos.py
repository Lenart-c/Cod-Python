nomes = []
precos = []
qtds = []

def menu():
    print("1 - adicionar produtos")
    print("2 - alterar produtos")
    print("3 - listar produtos")   
    print("4 - excluir produtos")
    print("0 - sair")

def escolha_id():
    try:
        idx = int(input("Escolha o ID do item: ")) - 1
        if (idx < 0 or idx > len(nomes)):
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

    nome_prod = input(str("Insera o produto: ")) #Passa o nome do produto
    preco_prod = float(input("Insira o valor do produto: ")) #Passa o valor do produto
    qtd_prod = int(input("Insira a quantidade de produtos:")) #Passa a quantidade de produtos

    nomes.append(nome_prod) #Adiciona o nome do produto
    precos.append(preco_prod) # Adiciona o preco do produto
    qtds.append(qtd_prod) #Adiciona a quantidades de produto


def listar_prod():

    if lista_vazia():
         return

    for i in range(len(nomes)):
        print(f"Lista: {i+1}, Nome: {nomes[i]}, Preço {precos[i]}, Quantidade: {qtds[i]}")



def alterar_prod(): #ALTERA O PRODUTO
    if lista_vazia():
        return

    listar_prod()
    print ("--- ESCOLHA UMA OPÇÃO:")
    print("1 - Alterar nome ")
    print("2 - Alterar preço")
    print("3 - Alterar quantidade")
    print("0 - sair")
    
    op = int(input("Digite a opção desejada: "))

    produto_id = escolha_id()

    if produto_id is None:
        return


    match op:
        case 1: #ALTERA O NOME                                        
            new_nome = input("Escolha o novo nome: ") 
            if (new_nome.replace(" ", "").isalpha):
                nomes[produto_id] = new_nome
                print("Nome alterado!")
            else: print("Digite um nome valido!")
        case 2: #ALTERA O PREÇO 
            new_preco = float(input("Escolha o novo preço: "))
            precos[produto_id] = new_preco
        case 3: #ALTERA A QUANTIDADE
            new_qtd = int(input("Coloque a nova quantidade: "))
            qtds[produto_id] = new_qtd
        case 0: #SAIR
            print("saindo...")
        case _: #DEFALT
            print("I")

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
        nomes.append(novos_nome)
        precos.append(novos_preco)
        qtds.append(novos_qtd)


def main():
    while True:

        menu()
        op = int(input("escolha uma opcão: "))

        match op:
            case 1:
                produtos()
            case 2:
                alterar_prod()
            case 3:
                listar_prod()
            case 4:
                excluir_prod()
            case 0:
                print("saindo...")
                return False
            case _:
                print("Informe uma opção válida")
                

if __name__ == '__main__':
    main()

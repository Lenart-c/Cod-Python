nome = []
preco = []
qtd = []

def menu():
    print("1 - adicionar produtos")
    print("2 - alterar produtos")
    print("3 - listar produtos")   
    print("0 - sair")



def produto(): #ADICIONA O PRODUTO

    nome_prod = input(str("Insera o produto: ")) #Passa o nome do produto
    preco_prod = float(input("Insira o valor do produto: ")) #Passa o valor do produto
    qtd_prod = int(input("Insira a quantidade de produtos:")) #Passa a quantidade de produtos


    nome.append(nome_prod) #Adiciona o nome do produto
    preco.append(preco_prod) # Adiciona o preco do produto
    qtd.append(qtd_prod) #Adiciona a quantidades de produto


def listar_produtos():
    for i in range(len(nome)):
        print(f"{i+1}, {nome[i]}, {preco[i]}, {qtd[i]}")



def alterar_prod(): #ALTERA O PRODUTO

    print ("--- ESCOLHA UMA OPÇÃO:")
    print("1 - Alterar nome ")
    print("2 - Alterar preço")
    print("3 - Alterar quantidade")
    print("0 - sair")
    
    op = int(input("Digite a opção desejada: "))

    produto_id = int(input("Escolha o ID do item: ")) - 1


    match op:
        case 1: #ALTERA O NOME                                        
            new_nome = input("Escolha o novo nome: ") 
            if (new_nome.replace(" ", "").isalpha):
                nome[produto_id] = new_nome
                print("Nome alterado!")
            else: print("Digite um nome valido!")
        case 2: #ALTERA O PREÇO 
            new_preco = float(input("Escolha o novo preço: "))
            preco[produto_id] = new_preco
        case 3: #ALTERA A QUANTIDADE
            new_qtd = int(input("Coloque a nova quantidade: "))
            qtd[produto_id] = new_qtd
        case 0: #SAIR
            print("saindo...")
        case _: #DEFALT
            print("I")




def main():
    while True:

        menu()
        op = int(input("escolha uma opcão: "))

        match op:
            case 1:
                produto()
            case 2:
                alterar_prod()
            case 3:
                listar_produtos()
            case 0:
                print("saindo...")
                return False
            case _:
                print("Informe uma opção válida")
                

if __name__ == '__main__':
    main()

contatos = []

def adicionarContato():
    nome = input("Nome do contato: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    if "@" not in email:
        print("Email inválido!")
    else:
        contato = {"nome": nome, "telefone": telefone, "email": email}
        contatos.append(contato)
        print("Contato adicionado com sucesso.")

def listarContatos():
    if not contatos:
        print("Não ha contatos na lista.")
    else:
        print("Lista de contatos:")
        for contato in contatos:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

def buscarContato():
    nome = input("Digite o nome do contato: ")
    for contato in contatos:
        if contato["nome"] == nome:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
            return
    print(f"Contato '{nome}' não encontrado.")

def removerContato():
    nome = input("Digite o nome do contato que deseja remover: ")
    for contato in contatos:
        if contato["nome"] == nome:
            contatos.remove(contato)
            print(f"Contato '{nome}' removido com sucesso.")
            return
    print(f"Contato '{nome}' não encontrado.")

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar um novo contato")
    print("2 - Listar todos os contatos")
    print("3 - Buscar um contato pelo nome")
    print("4 - Remover um contato pelo nome")
    print("5 - Sair do programa")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        adicionarContato()
    elif opcao == "2":
        listarContatos()
    elif opcao == "3":
        buscarContato()
    elif opcao == "4":
        removerContato()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
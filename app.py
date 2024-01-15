from Classes import ContactBook
contato = ContactBook("Admin","(99)999999999","admin@admin.com")
while True:
    option = input('1 - Adicionar contato \n2 - Listar contatos \n3 - Procurar contato \n4 - Remover contato \n5 - Sair \n> ')
    match(option):
        case '1':
            name = input("Digite o nome do contato: ")
            phone = input("Digite o telefone do contato: ")
            email = input("Digite o e-mail do contato: ")
            contato = ContactBook(name,phone,email)
            contato.add_contact(contato)                
        case '2':
            contato.list_contacts()
        case '3':
            name = input("Digite o nome do contato: ")
            contato.search_contact(name)
        case '4':
            name = input("Digite o nome do contato: ")
            contato.remove_contact(name)
        case '5':
            break
        case _:
            print('\nOpção inválida, tente de 1 até 5.\n')
agenda = []

def add_contact():
    print("\n-------------------------------------------------------------------------------------------------------------------")
    name = input("\nInforme o nome do contato que deseja adicionar: ")
    telephone = input("Informe o telefone: ")
    mail = input("Informe o email:")
    mark_favorite = (input("Marcar esse contato como favorito? (S/N) ")).upper()

    favorite = True if mark_favorite == 'S' else False

    new_contact = {"name" : name, 
                   "telephone" : telephone,
                   "mail" : mail,
                   "favorite": favorite}
    
    save_new_contact(agenda, new_contact)
    return

def save_new_contact(agenda, new_contact):
    agenda.append(new_contact)
    print(f"\nO contato '{new_contact['name']}' foi adicionado com sucesso!")
    return

def edit_contact():
    list_contact()
    print("\n-------------------------------------------------------------------------------------------------------------------")

    index = input("\nInforme o id do contato que deseja editar: ")
    index_contact = int(index) - 1

    if(index_contact  >= 0 and index_contact < len(agenda)):
        option = input("\nO que deseja editar?\n 1. Nome\n 2. Telefone\n 3. Email\n 4. Remover favorito\n 5. Voltar\nInforme a opção escolhida: ")

        match option:
            case "1":
                print(f"\nNome atual: {agenda[index_contact]['name']}")
                new_name = input("Informe o novo nome: ")
                save_edit_contact(agenda, index_contact, "name", new_name)
            case "2":
                print(f"\nTelefone atual: {agenda[index_contact]['telephone']}")
                new_telephone = input("Informe o novo telefone:")
                save_edit_contact(agenda, index_contact, "telephone", new_telephone)
            case "3":
                print(f"\nEmail atual: {agenda[index_contact]['mail']}")
                new_mail = input("Informe o novo email:")
                save_edit_contact(agenda, index_contact, "mail", new_mail)
            case "4":
                remove_favorite(index_contact)
            case "5":
                return
            case _:
                print("Opção inválida") 
    else:
        print("\nID inválido.")
    return

def save_edit_contact(agenda, index_contact, modification, new_information):

    match modification:
        case "name":
            agenda[index_contact]['name'] = new_information
        case "telephone":
            agenda[index_contact]['telephone'] = new_information
        case "mail":
            agenda[index_contact]['mail'] = new_information

    print("\nContato editado com sucesso.") 
    favorite = "★" if agenda[index_contact]['favorite'] else " "
    print(f"[{favorite} ] {agenda[index_contact]['name']} \nTelefone: {agenda[index_contact]['telephone']} \nEmail: {agenda[index_contact]['mail']}") 
    return

def delete_contact():
    list_contact()
    print("\n-------------------------------------------------------------------------------------------------------------------")

    index = input("\nInforme o id do contato que deseja deletar: ")
    index_contact = int(index) - 1

    if(index_contact  >= 0 and index_contact < len(agenda)):
        confirm = (input(f"\nTem cereteza que deseja deletar o contato '{agenda[index_contact]['name']}'? (S/N) ")).upper()
        if confirm == "S":
            save_remove_contact(agenda, index_contact)
        else:
            print("\nNenhum contato foi removido.")
            return
    else:
        print("\nID inválido.")
    return

def save_remove_contact(agenda, index_contact):
    print(f"\nContato {agenda[index_contact]['name']} removido.")
    agenda.remove(agenda[index_contact])
    return

def list_contact():
    print("\n-------------------------------------------------------------------------------------------------------------------")
    if (len(agenda) == 0):
        print("\nLista vazia no momento.")
        return
    
    print("\nLista de Contatos: \n")
    for index, contact in enumerate(agenda, start=1):
        favorite = "★" if contact['favorite'] else " "
        print(f"{index}. [ {favorite} ] {contact['name']}\n   Telefone: {contact['telephone']}\n   Email: {contact['mail']}")
    return

def add_favorite():
    list_contact()
    print("\n-------------------------------------------------------------------------------------------------------------------")

    index = input("\nInforme o id do contato que deseja favoritar: ")
    index_contact = int(index) - 1

    if(index_contact  >= 0 and index_contact < len(agenda)):
        agenda[index_contact]['favorite'] = True
        print(f"\nContato {agenda[index_contact]['name']} marcado como favorito.")
    else:
        print("\nID inválido.")
    return

def remove_favorite(index_contact):
    agenda[index_contact]['favorite'] = False
    print(f"\nContato {agenda[index_contact]['name']} desmarcado como favorito.")
    return

def list_favorite():
    print("\n-------------------------------------------------------------------------------------------------------------------")
    print("\nLista de Contatos Favoritos: \n")
    count = 0;
    for index, contact in enumerate(agenda, start=1):
        if(contact['favorite']):
            count += 1
            favorite = "★"
            print(f"{index}. [ {favorite} ] {contact['name']}\n   Telefone: {contact['telephone']}\n   Email: {contact['mail']}")
    
    if (count == 0):
        print("\nLista vazia no momento.")
    
    return

def leave():
    print("\n-------------------------------------------------------------------------------------------------------------------")
    print("\nSaindo da agenda...\n")
    exit()

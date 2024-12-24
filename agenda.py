import modulo_agenda

menu_options = {
    "ADD_CONTACT": "1",
    "EDIT_CONTACT": "2",
    "DELL_CONTACT": "3",
    "LIST_CONTACT": "4",
    "ADD_FAV_CONTACT": "5",
    "LIST_FAV_CONTACT": "6",
    "EXIT": "7"
}

while True:
    print("\n-------------------------------------------------------------------------------------------------------------------")
    print("\nAgenda\n")
    print("1. Adicionar contato")
    print("2. Editar contato")
    print("3. Deletar contato")
    print("4. Listar contatos")
    print("5. Adicionar como favorito")
    print("6. Listar favoritos")
    print("7. Sair\n")

    option = input("Escolha uma opção: ")

    menu_functions = {
        menu_options["ADD_CONTACT"]: modulo_agenda.add_contact,
        menu_options["EDIT_CONTACT"]: modulo_agenda.edit_contact,
        menu_options["DELL_CONTACT"]: modulo_agenda.delete_contact,
        menu_options["LIST_CONTACT"]: modulo_agenda.list_contact,
        menu_options["ADD_FAV_CONTACT"]: modulo_agenda.add_favorite,
        menu_options["LIST_FAV_CONTACT"]: modulo_agenda.list_favorite,
        menu_options["EXIT"]: modulo_agenda.leave
    }

    if option in menu_functions:
        menu_functions[option]() 
    else:
        print("Opção inválida! Tente novamente.")
from notes import Note, mydb

note = Note()

while True:
    action = input('''Choose an action:
    create, show, delete, update title, update content, save(saves to csv), exit: ''')

    if action == 'exit':
        mydb.close()
        break

    elif action == 'create':
        title = input('Enter note title: ')
        description = input('Enter contents here: ')
        note.create_note(title, description)

    elif action == 'show':
        note.show_notes()

    elif action == 'delete':
        id = input('Which note would you like to delete(use note id): ')
        note.delete_note(id)

    elif action == 'update title':
        id = input('Add note id: ')
        title = input('Add new title: ')
        note.update_title(title, id)

    elif action == 'update content':
        id = input('Add note id: ')
        description = input('Add new content: ')
        note.update_description(description, id)

    elif action == 'save':
        note.save_to_csv()

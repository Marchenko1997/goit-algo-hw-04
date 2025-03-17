def add_contact(arg, contacts):
    if len(arg) != 2:
        return "Enter your name and phone number."
    
    name, phone = arg
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(arg, contacts):
    if len(arg) !=2:
        return "Enter your name and phone number."
    
    name, phone = arg
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for'{name}' updated."
    return f"Contact '{name}' is not found."

def show_phone(arg, contacts):
    if len(arg) != 1:
          return "Enter the contact name."
    name = arg[0]
    phone = contacts.get(name)
    if phone:
        return f"Phone number for '{name}': {phone}"
    return f"Contact '{name}' is not found."

def show_all(contacts):
    if not contacts:
        return "The contact list is empty."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def handle_command(command, arg, contacts):
    if command == "hello":
         return "How can I help you?"
    elif command == "add":
        return add_contact(arg, contacts)
    elif command == "change":
        return change_contact(arg, contacts)
    elif command == "phone":
        return show_phone(arg, contacts)
    elif command == "show":
        return show_all(contacts)
    else:
        return "Invalid command. Please try again."
    
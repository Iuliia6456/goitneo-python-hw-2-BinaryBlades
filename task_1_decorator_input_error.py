import re

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me the correct data"
    return wrapper

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    pattern = re.compile(r'\d{10}$')
    if not re.match(pattern, args[1]):
        raise ValueError (print("Phone number must have 10 digits in format 0501111111"))
    contacts[name.lower()] = phone
    return "Contact added."

@input_error
def change_username_phone(args, contacts):
    name, new_phone = args
    pattern = re.compile(r'\d{10}$')
    if not re.match(pattern, args[1]):
        raise ValueError (print("Phone number must have 10 digits in format 0501111111"))
    if name.lower() in contacts:
        contacts[name.lower()] = new_phone
        return "Contact updated."
    else:
        return "No such username"
        
@input_error
def phone_username(args, contacts):
    if len(args) != 1:
        raise ValueError (print(("Wrong format, please enter the data in format: phone <name>")))
    if args[0] in contacts:
        return contacts[args[0].lower()]
    else:
        return "No such username"

@input_error    
def all(contacts):
    if not contacts:
        raise ValueError (print("The list of contacts is empty, please enter add <name> <phone>"))
    result = ''
    for key, value in contacts.items():
        result += f"{key}: {value}\n"
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input) 
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("""How can I help you?
                   For adding the contact please enter the data in format: add <name> <phone> (10 digits in format 0501111111)
                   For changing the contact please enter the data in format: change <name> <new phone> (10 digits in format 0501111111)
                   For getting a phone number please enter the data in format: phone <name>
                   For getting the list of all contacts enter: <all>
                   For exit please enter: <close> or <exit> """)
        elif "add" in command :
            print(add_contact(args, contacts))
        elif "change" in command:
            print(change_username_phone(args, contacts))
        elif "phone" in command :
            print(phone_username(args, contacts))
        elif "all" in command:
            print(all(contacts))
        else:
            print("Invalid command. Please verify the command and try again")
    print(contacts)

if __name__ == "__main__":
    main()
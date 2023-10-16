
import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    name, new_phone = args
    if name.lower() in contacts:
        contacts[name.lower()] = new_phone
        return "Contact updated."

def phone_username(args, contacts):
    if args[0] in contacts:
        return contacts[args[0].lower()]
    else:
        return "No such username"
    
def all(contacts):
    if not contacts:
        return ("The list of contacts is empty, please enter add <name> <phone>")
    result = ''
    for key, value in contacts.items():
        result += f"{key}: {value}\n"
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    pattern = re.compile('\+?\d{1,4}\(?[0-9]+\)?[0-9-]+')
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input) 
            if not user_input:
                raise ValueError("Empty value, please enter a command") 
        except ValueError:
            print("Empty value, please enter a command")
            continue
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("""How can I help you?
                   For adding the contact please enter the data in format: add <name> <phone> (+_______)
                   For changing the contact please enter the data in format: change <name> <new phone> (+_______)
                   For getting a phone number please enter the data in format: phone <name>
                   For getting the list of all contacts enter: <all>
                   For exit please enter: <close> or <exit> """)
        elif "add" in command and len(args) <= 1:
            print("Wrong format, please enter the data in format: add <name> <phone> (+_______)")
        elif "add" in command and len(args) == 2 and len(args[1]) < 7:
            print("You entered wrong phone number, please enter numbers starting with +")
        elif "add" in command and len(args) == 2 and re.match(pattern, args[1]):
            print(add_contact(args, contacts))
        elif "add" in command and len(args) == 2 and not re.match(pattern, args[1]):
            print("You entered wrong phone number, please enter numbers starting with +")
        elif "add" in command and len(args) > 2:
            print("Too many values are entered, please enter the data in format: add <name> <phone> (+_______")
        
        elif "change" in command and len(args) <= 1:
            print("Wrong format, please enter the data in format: change <name> <new phone> (+_______)")
        elif "change" in command and len(args) == 2 and len(args[1]) < 7:
            print("You entered wrong phone number, please enter numbers starting with +")
        elif "change" in command and len(args) == 2 and re.match(pattern, args[1]):
            print(change_username_phone(args, contacts))
        elif "change" in command and len(args) == 2 and not re.match(pattern, args[1]):
            print("You entered wrong phone number, ")
        elif "change" in command and len(args) > 2:
            print("Too many values are entered, please enter the data in format: change <name> <new phone> (+_______)")

        elif "phone" in command and len(args) == 0:
            print("Wrong format, please enter the data in format: phone <name>")
        elif "phone" in command :
            print(phone_username(args, contacts))
        elif "all" in command:
            print(all(contacts))
        
        else:
            print("Invalid command. Please verify the command and try again")
    print(contacts)

if __name__ == "__main__":
    main()
from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
    
class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validated_phone()

    def validated_phone(self):
        pattern = re.compile(r'\d{10}$')
        if not re.match(pattern, self.value):
            raise ValueError (print("Phone number must have 10 digits in format 0501111111"))
    
class Record:
    def __init__(self, name):
        self.name = Name(name.lower())
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, old, new):
         self.phones = [new if str(i) == old else i for i in self.phones]

    def remove_phone(self, phone):         
         for i in self.phones:
             if str(i) == phone:
                 return self.phones.remove(i)

    def find_phone(self, phone):         
         for i in self.phones:
             if str(i) == phone:
                 return i
         return "The phone is not found"
                 
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        lower_name = name.lower()
        if lower_name in self.data:
            return self.data[lower_name]
        return "The user is not found"
        
    def delete(self, name):
        lower_name = name.lower()
        if lower_name in self.data:
            return self.data.pop(lower_name)
      
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

john.remove_phone("5555555555")
found_phone2 = john.find_phone("5555555555")
print(f"{john.name}: {found_phone2}")

book.delete("Jane")
jane = book.find("Jane")
print(jane)





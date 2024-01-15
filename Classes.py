class Contact:
    def __init__(self, name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def validate(self,value, format, example):
       import re
       pattern = format
       match = re.match(pattern, value) 
       if not match:
           raise ValueError(f"Precisa ser no forma {example}")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('O nome deve conter apenas letras')
        self._name = value
        
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self,value):
        self._phone = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"
 
class ContactBook(Contact):
    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def list_contacts(self):
        try:
            for contact in self.contacts:
                print(contact)
        except:
            raise Exception("Lista de contatos vazia")
                
    def search_contact(self,name):
        contact = [contact for contact in self.contacts if contact.name == name]
        print(contact[0])
    
    def remove_contact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
        
import cmd

class ContactManager(cmd.Cmd):
    prompt = " (contact)  >>> "

    contacts = {}
    
    def preloop(self):
        '''Method called once before the command loop'''
        self.intro = 'Welcome to the contact Manager Type help or ? to list commands\n'

    def postloop(self):
        '''Method called once after the command loop'''
        print("Exiting the contact Manager")
    
    def do_add(self,line):
        '''Add a contact with a name and phone number'''
        try:
            name, phone = line.split()
            self.contacts[name] = phone
            print(f"contact added: {name} - {phone}")
        except ValueError:
            print("Invalid input. Please enter the name and phone number separate by a space")

    def do_get(self, name):
        '''Retrieve a contact's phone number by name'''
        if name in self.contacts:
            print(f"{name}'s phone number is {self.contacts[name]}")
        else:
            print(f"NO Contact found with the name '{name}'.")

    def do_lists(self, _):
        '''Retrieves a contacts phone number by its name'''
        if not self.contacts:
            print("No contacts available")
        else:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")
        
    def do_delete(self, name):
        '''Delete a contact by name'''
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact deleted successfully: {name}")
        else:
            print(f"No contact found with the given name '{name}'.")

    def do_update(self, line):
        """Update a contact's phone number."""
        try:
            name, new_phone = line.split(' ',  1)
            if name in self.contacts:
                self.contacts[name] = new_phone
                print(f"Contact updated: {name} - {new_phone}")
            else:
                print(f"No contact found with the name '{name}'.")
        except ValueError:
            print("Invalid input. Please enter the name and new phone number separated by a space.")

    def do_quit(self, arg):
        "This quits or exits the program"
        return True

    do_exit = do_quit
    

if __name__ == "__main__":
    ContactManager().cmdloop()
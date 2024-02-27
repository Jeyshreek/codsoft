class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact added successfully!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}, Phone: {self.contacts[name]['Phone']}, Email: {self.contacts[name]['Email']}, Address: {self.contacts[name]['Address']}")
        else:
            print("Contact not found!")

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name]["Phone"] = phone
            self.contacts[name]["Email"] = email
            self.contacts[name]["Address"] = address
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def show_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
        else:
            print("Your contact book is empty!")


def main():
    contact_book = ContactBook()

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. View Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            address = input("Enter the address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == "2":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "3":
            name = input("Enter the name of the contact to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email: ")
            address = input("Enter the new address: ")
            contact_book.update_contact(name, phone, email, address)
        elif choice == "5":
            contact_book.show_contacts()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

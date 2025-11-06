# Phase 1
class LibraryItem:
    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.on_shelf = True  

    def checkout(self):
        if not self.on_shelf:
            return False
        self.on_shelf = False
        return True

    def checkin(self):
        if self.on_shelf:
            return False
        self.on_shelf = True
        return True

    def summary(self):
        status = "Available" if self.on_shelf else "Checked Out"
        return f"ID: {self.item_id} , Title: {self.title} , Author: {self.author} , Status: {status}"

# Phase 3
class Book(LibraryItem):
    def __init__(self, item_id, title, author, pages):
        super().__init__(item_id, title, author)
        self.pages = pages

    def summary(self):
        base_summary = super().summary()
        return f"{base_summary} , Pages: {self.pages}"

class DVD(LibraryItem):
    def __init__(self, item_id, title, author, runtime):
        super().__init__(item_id, title, author)
        self.runtime = runtime

    def summary(self):
        base_summary = super().summary()
        return f"{base_summary} , Runtime: {self.runtime} mins"

# Phase 2
class LibraryCatalog:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.item_id in self.items:
            print("Error: An item with this ID already exists.")
            return False
        self.items[item.item_id] = item
        return True

    def checkout_item(self, item_id):
        item = self.items.get(item_id)
        if not item:
            print("Item not found.")
            return False
        if item.checkout():
            print(f"Item '{item.title}' checked out successfully.")
            return True
        else:
            print("Item is already checked out.")
            return False

    def checkin_item(self, item_id):
        item = self.items.get(item_id)
        if not item:
            print("Item not found.")
            return False
        if item.checkin():
            print(f"Item '{item.title}' checked in successfully.")
            return True
        else:
            print("Item is already on the shelf.")
            return False

    def list_items(self):
        if not self.items:
            print("No items in the library.")
            return
        for item in self.items.values():
            print(item.summary())

# Phase 4
def main():
    catalog = LibraryCatalog()
    while True:
        print("\n=== Community Library System ===")
        print("1. Add a new Book")
        print("2. Add a new DVD")
        print("3. Check out an item")
        print("4. Check in an item")
        print("5. List all items")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            item_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            pages = input("Enter number of pages: ")
            book = Book(item_id, title, author, pages)
            catalog.add_item(book)

        elif choice == "2":
            item_id = input("Enter DVD ID: ")
            title = input("Enter DVD Title: ")
            director = input("Enter DVD Director: ")
            runtime = input("Enter runtime in minutes: ")
            dvd = DVD(item_id, title, director, runtime)
            catalog.add_item(dvd)

        elif choice == "3":
            item_id = input("Enter the ID of the item to check out: ")
            catalog.checkout_item(item_id)

        elif choice == "4":
            item_id = input("Enter the ID of the item to check in: ")
            catalog.checkin_item(item_id)

        elif choice == "5":
            catalog.list_items()

        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

class ShoppingListManager:
    def __init__(self):
        self.shopping_list = []

    def add_item(self, item):
        self.shopping_list.append(item)
        print(f"Added '{item}' to the shopping list.")

    def display_list(self):
        if self.shopping_list:
            print("Shopping List:")
            for index, item in enumerate(self.shopping_list, start=1):
                print(f"{index}. {item}")
        else:
            print("Shopping List is empty.")

    def main_menu(self):
        print("Welcome to the Shopping List Manager!")

        while True:
            print("\nChoose an option:")
            print("1. Add item to the shopping list")
            print("2. Display shopping list")
            print("3. Quit")

            choice = input("Enter your choice (1/2/3): ").strip()

            if choice == '1':
                item = input("Enter the item to add: ").strip()
                self.add_item(item)
            elif choice == '2':
                self.display_list()
            elif choice == '3':
                print("Thank you for using the Shopping List Manager!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    manager = ShoppingListManager()
    manager.main_menu()


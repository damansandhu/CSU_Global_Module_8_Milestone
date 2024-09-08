## Milestone 1 - Online Shopping Cart

class ItemToPurchase:
    # Default constructor initializing the attributes
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Method to calculate and return the total cost of the item
    def get_total_cost(self):
        return self.item_price * self.item_quantity

    # Method to print the item cost
    def print_item_cost(self):
        total_cost = self.get_total_cost()
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

# Function to safely get item price
def get_price():
    while True:
        try:
            price = float(input("Enter the item price:\n"))
            if price < 0:
                raise ValueError("Price cannot be negative.")
            return price
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid price.")

# Function to safely get item quantity
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the item quantity:\n"))
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            return quantity
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer quantity.")

# Main section of the code
if __name__ == "__main__":
    # Prompting user for the first item
    print("Item 1")
    item1_name = input("Enter the item name:\n")
    item1_price = get_price()
    item1_quantity = get_quantity()
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    # Prompting user for the second item
    print("Item 2")
    item2_name = input("Enter the item name:\n")
    item2_price = get_price()
    item2_quantity = get_quantity()
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    # Printing the item costs
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculating and printing the total cost
    total_cost = item1.get_total_cost() + item2.get_total_cost()
    print(f"Total: ${total_cost:.2f}")


## Milestone 2
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def get_total_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        total_cost = self.get_total_cost()
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, item_name: str):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item: ItemToPurchase):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                found = True
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.get_total_cost() for item in self.cart_items)

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart: ShoppingCart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option:\n")

        if choice == 'q':
            break
        elif choice == 'a':
            add_item_to_cart(cart)
        elif choice == 'r':
            item_name = input("Enter name of item to remove:\n")
            cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name:\n")
            new_quantity = int(input("Enter the new quantity:\n"))
            updated_item = ItemToPurchase(item_name, 0, new_quantity)  # Only quantity is modified
            cart.modify_item(updated_item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        else:
            print("Invalid option. Please try again.")


def add_item_to_cart(cart: ShoppingCart):
    print("ADD ITEM TO CART")
    item_name = input("Enter the item name:\n")
    item_description = input("Enter the item description:\n")
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n"))
    new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
    cart.add_item(new_item)


# Main function to run the program
if __name__ == "__main__":
    # Step 7: Prompting user for name and date
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    cart = ShoppingCart(customer_name, current_date)

    print(f"\nCustomer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")

    # Call the menu function
    print_menu(cart)

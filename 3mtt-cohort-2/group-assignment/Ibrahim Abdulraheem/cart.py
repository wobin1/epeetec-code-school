class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_name):
        self.items = [item for item in self.items if item.product.name != product_name]

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            for item in self.items:
                print(f"{item.product.name} : {item.quantity} @ ${item.product.price} each")
            print(f"Total: ${self.calculate_total():.2f}")

# Example usage
if __name__ == "__main__":
    # Create some products
    apple = Product("Apple", 0.5)
    banana = Product("Banana", 0.3)
    orange = Product("Orange", 0.7)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(apple, 3)
    cart.add_item(banana, 2)
    cart.add_item(orange, 5)

    # Display the cart contents
    cart.display_cart()

    # Remove an item from the cart
    cart.remove_item("Banana")

    # Display the cart contents again
    cart.display_cart()

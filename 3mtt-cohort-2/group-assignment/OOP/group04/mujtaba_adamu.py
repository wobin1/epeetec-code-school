class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} (x{self.quantity}) - Total: ${self.total_price():.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                if item.quantity > 1:
                    item.quantity -= 1
                else:
                    self.items.remove(item)
                return
        print(f"Item '{product_name}' not found in the cart.")

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("Shopping Cart:")
        for item in self.items:
            print(item)
        print(f"Total Cost: ${self.calculate_total():.2f}")


def main():
    cart = ShoppingCart()
    
    # Sample products
    apple = Product("Apple", 0.50)
    banana = Product("Banana", 0.30)
    bread = Product("Bread", 2.00)

    # Adding items to the cart
    cart.add_item(apple, 3)
    cart.add_item(banana, 5)
    cart.add_item(bread, 2)

    # Display cart contents
    cart.display_cart()

    # Remove an item and display again
    cart.remove_item("Banana")
    cart.display_cart()

    # Remove an item that doesn't exist
    cart.remove_item("Orange")

    # Final total
    print(f"Final Total: ${cart.calculate_total():.2f}")


if __name__ == "__main__":
    main()

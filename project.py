import csv
from datetime import datetime
import getpass  # for hiding the password input

# Global list of authenticated users (to simulate simple login system)
auth_users = {
    "admin": "pass",  # A default admin login for testing
    "employee": "pass"
}

# Login system
def login():
    print("\nLogin Required:")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    
    if username in auth_users and auth_users[username] == password:
        print(f"Login successful! Welcome {username}.")
        return True
    else:
        print("Invalid username or password.")
        return False

# Contact validation for customers and employees
def is_valid_contact(contact_info):
    return contact_info.isdigit() and len(contact_info) == 10

# Customer Class
class Customer:
    def __init__(self, customer_id, name, address, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def save_to_file(self):
        with open("customers.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.customer_id, self.name, self.address, self.contact_info])

    @staticmethod
    def load_customers():
        customers = []
        try:
            with open("customers.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    customers.append(Customer(*row))
        except FileNotFoundError:
            print("No customers found.")
        return customers

# Employee Class
class Employee:
    def __init__(self, employee_id, name, position, contact_info):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.contact_info = contact_info

    def save_to_file(self):
        with open("employees.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.employee_id, self.name, self.position, self.contact_info])

    @staticmethod
    def load_employees():
        employees = []
        try:
            with open("employees.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    employees.append(Employee(*row))
        except FileNotFoundError:
            print("No employees found.")
        return employees

# MenuItem Class
class MenuItem:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = float(price)

    def save_to_file(self):
        with open("menu_items.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.item_id, self.name, self.description, self.price])

    @staticmethod
    def load_menu():
        menu = []
        try:
            with open("menu_items.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    menu.append(MenuItem(*row))
        except FileNotFoundError:
            print("No menu items found.")
        return menu

# Order Class
class Order:
    def __init__(self, order_id, customer_id, order_date, total_amount, status="success"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.total_amount = total_amount
        self.status = status

    def save_to_file(self):
        with open("orders.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.order_id, self.customer_id, self.order_date, self.total_amount, self.status])

    @staticmethod
    def load_orders():
        orders = []
        try:
            with open("orders.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    orders.append(Order(*row))
        except FileNotFoundError:
            print("No orders found.")
        return orders

# OrderDetail Class
class OrderDetail:
    def __init__(self, order_detail_id, order_id, item_id, item_name, quantity, price):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = int(quantity)
        self.price = float(price)

    def save_to_file(self):
        with open("order_details.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.order_detail_id, self.order_id, self.item_id, self.item_name, self.quantity, self.price])

# Payment Class
class Payment:
    def __init__(self, payment_id, order_id, payment_method, amount):
        self.payment_id = payment_id
        self.order_id = order_id
        self.payment_method = payment_method
        self.amount = float(amount)

    def save_to_file(self):
        with open("payments.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.payment_id, self.order_id, self.payment_method, self.amount])

    @staticmethod
    def process_payment(order_id, total_amount):
        payment_method = input("Enter payment method (cash, card, mobile): ")
        payment_id = f"PAY{order_id[3:]}"  # Generate payment ID based on order ID
        payment = Payment(payment_id, order_id, payment_method, total_amount)
        payment.save_to_file()
        print(f"Payment of {total_amount} processed via {payment_method}")

# Main Functions

def display_menu():
    print("\n1. Add Customer")
    print("2. View Customers")
    print("3. Add Menu Item")
    print("4. View Menu")
    print("5. Place Order")
    print("6. View Orders")
    print("7. Manage Inventory")
    print("8. View Payments")
    print("9. Add Employee")
    print("10. Generate Sales Report")
    print("11. Exit")

def add_customer():
    if login():
        customer_id = input("Enter customer ID: ")
        name = input("Enter customer name: ")
        address = input("Enter customer address: ")
        contact_info = input("Enter customer contact info (10-digit number): ")
        if not is_valid_contact(contact_info):
            print("Invalid contact number. Must be 10 digits.")
            return
        customer = Customer(customer_id, name, address, contact_info)
        customer.save_to_file()
        print(f"Customer {name} added successfully!")

def view_customers():
    if login():
        customers = Customer.load_customers()
        for customer in customers:
            print(f"ID: {customer.customer_id}, Name: {customer.name}, Address: {customer.address}, Contact: {customer.contact_info}")

def add_menu_item():
    if login():
        item_id = input("Enter item ID: ")
        name = input("Enter item name: ")
        description = input("Enter item description: ")
        price = input("Enter item price: ")
        menu_item = MenuItem(item_id, name, description, price)
        menu_item.save_to_file()
        print(f"Menu item {name} added successfully!")

def view_menu():
    menu = MenuItem.load_menu()
    if menu:
        for item in menu:
            print(f"ID: {item.item_id}, Name: {item.name}, Description: {item.description}, Price: {item.price}")
    else:
        print("No menu items found.")

def place_order():
    customers = Customer.load_customers()
    if not customers:
        print("No customers available. Please add a customer first.")
        return

    view_customers()
    customer_id = input("Enter the customer ID for this order: ")

    menu = MenuItem.load_menu()
    if not menu:
        print("No menu items available. Please add menu items first.")
        return

    print("\nAvailable Menu Items:")
    view_menu()

    order_id = f"ORD{len(Order.load_orders()) + 1}"
    total_amount = 0
    order_details = []

    while True:
        item_id = input("Enter the item ID to order (or 'done' to finish): ")
        if item_id == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        
        item = next((item for item in menu if item.item_id == item_id), None)
        if item:
            order_detail = OrderDetail(f"OD{len(order_details) + 1}", order_id, item.item_id, item.name, quantity, item.price)
            order_details.append(order_detail)
            total_amount += item.price * quantity
            order_detail.save_to_file()
            print(f"Added {quantity} of {item.name} to the order.")
        else:
            print("Item ID not found.")

    order = Order(order_id, customer_id, datetime.now(), total_amount)
    order.save_to_file()
    Payment.process_payment(order_id, total_amount)

def view_orders():
    if login():
        orders = Order.load_orders()
        for order in orders:
            print(f"Order ID: {order.order_id}, Customer ID: {order.customer_id}, Date: {order.order_date}, Total: {order.total_amount}, Status: {order.status}")

def manage_inventory():
    if login():
        item_id = input("Enter item ID for inventory management: ")
        quantity = int(input("Enter quantity to add/remove (negative to remove): "))
        print(f"Inventory for item ID {item_id} updated by {quantity}.")

def view_payments():
    if login():
        payments = []
        try:
            with open("payments.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    payments.append(Payment(*row))
        except FileNotFoundError:
            print("No payments found.")
            return

        for payment in payments:
            print(f"Payment ID: {payment.payment_id}, Order ID: {payment.order_id}, Amount: {payment.amount}, Method: {payment.payment_method}")

def generate_sales_report():
    if login():
        orders = Order.load_orders()
        payments = []

        # Load payments
        try:
            with open("payments.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    payments.append(Payment(*row))
        except FileNotFoundError:
            print("No payments found.")
            return

        total_revenue = 0
        total_orders = len(orders)
        for payment in payments:
            total_revenue += payment.amount

        print("\n--- Sales Report ---")
        print(f"Total Orders: {total_orders}")
        print(f"Total Revenue: ${total_revenue:.2f}")

        # Optional: Display orders with payment details
        for order in orders:
            payment = next((p for p in payments if p.order_id == order.order_id), None)
            if payment:
                print(f"Order ID: {order.order_id}, Customer ID: {order.customer_id}, Total: ${order.total_amount}, Payment Method: {payment.payment_method}, Amount Paid: {payment.amount}")
            else:
                print(f"Order ID: {order.order_id}, Customer ID: {order.customer_id}, Total: ${order.total_amount} (Payment success)")

def add_employee():
    if login():
        employee_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        contact_info = input("Enter employee contact info (10-digit number): ")
        if not is_valid_contact(contact_info):
            print("Invalid contact number. Must be 10 digits.")
            return
        employee = Employee(employee_id, name, position, contact_info)
        employee.save_to_file()
        print(f"Employee {name} added successfully!")

def view_employees():
    if login():
        employees = Employee.load_employees()
        for employee in employees:
            print(f"ID: {employee.employee_id}, Name: {employee.name}, Position: {employee.position}, Contact: {employee.contact_info}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            add_menu_item()
        elif choice == "4":
            view_menu()
        elif choice == "5":
            place_order()
        elif choice == "6":
            view_orders()
        elif choice == "7":
            manage_inventory()
        elif choice == "8":
            view_payments()
        elif choice == "9":
            add_employee()
        elif choice == "10":
            generate_sales_report()
        elif choice == "11":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

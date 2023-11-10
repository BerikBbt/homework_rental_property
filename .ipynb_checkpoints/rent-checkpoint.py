# class Reental_Property:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.expence = []
#         self.incomes =[]
#         self.roi = None

#     def add_expense(self, expense_type, amount):
#         self.expenses.append(expense_type, amount)
    
#     def add_income(self, income_type, amount):
#         self.expenses.append(income_type, amount)

#     def calculate_roi(self):





class rental_roperty:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.expenses = []
        self.incomes = []
        self.roi = None

    def add_expense(self, expense_type, amount):
        self.expenses.append((expense_type, amount))

    def add_income(self, income_type, amount):
        self.incomes.append((income_type, amount))

    def calculate_roi(self):
        total_income = sum(amount for _, amount in self.incomes)
        total_expense = sum(amount for _, amount in self.expenses)
        self.roi = (total_income - total_expense) / total_expense * 100

    def display_roi(self):
        if self.roi is not None:
            print(f"ROI for {self.name}: {self.roi:.2f}%")
        else:
            print("ROI has not been calculated yet.")


class Tenant:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def view_properties(self):
        for property in self.properties:
            print(f"Property: {property.name}, Address: {property.address}")

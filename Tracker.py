import json
from expense import Expense

class FinanceTracker:
    def __int__(self):
        self.expenses = []

    def add(self,expense):
        self.expenses.append(expense)

    def show(self):
        for index, expense in enumerate(self.expenses, start=1):

            print(
                index,
                expense.name,
                expense.amount,
                expense.categroy,
                expense.date
            )


    # To Calculate The Total of Expense
    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount

        return total

    # We Need Search category to now defrant category
    def search(self, category):
        result = []
        for expense in self.expenses:
            if expense.category == category :
                result.append(expense)
        return result

    # If their are expense we don't want we can delete it
    def delete(self, number):
        index = number - 1
        if index < len(self.expenses):
            self.expenses.pop(index)

    def save(self):
        data = []
        for expense in self.expenses :
            data.append({
                "name": expense.name,
                "amount":expense.amount,
                "category": expense.category,
                "date": expense.date
            })

        with open("expenses.json", "w") as file:
            json.dump(data, file)



    def load(self):
        try:
            with open("expenses.json", "r") as file:
                data = json.load(file)

                for item in data:
                    expense = Expense(
                        item["name"],
                        item["amount"],
                        item["category"],
                        item["date"]
                    )

                    self.expenses.append(expense)

        except FileNotFoundError:
            pass

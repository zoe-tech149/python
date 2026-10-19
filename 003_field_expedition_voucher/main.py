original_budget = 2000.00

transport_expense = 850.00
food_supplies_expense = 425.00
research_materials_expense = 310.00

total_expenses = transport_expense + food_supplies_expense + research_materials_expense

remaining_budget = original_budget - total_expenses

print("Expense Voucher")

print()

print(f"Original budget:   R{original_budget:.2f}")

print()

print("Expenses:")
print(f"Transport: R{transport_expense:.2f}")
print(f"Food and supplies: R{food_supplies_expense:.2f}")
print(f"Research materials: R{research_materials_expense:.2f}")

print(f"Total expenses: R{total_expenses:.2f}")

print(f"Remaining budget: R{remaining_budget:.2f}")
salary = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))
savings = salary - monthly_expenses
projected_savings = (savings * 12) + (savings * 12 * 0.05)
print("Your monthly savings are $", savings,
      "Projected savings after one year, with interest, is: $", projected_savings)
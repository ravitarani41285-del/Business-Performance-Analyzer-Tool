print("=================================")
print("   BUSINESS PERFORMANCE ANALYZER")
print("=================================")

sales = float(input("Enter total sales: "))
expenses = float(input("Enter total expenses: "))

profit = sales - expenses

if profit > 0:
    status = "PROFIT"
elif profit < 0:
    status = "LOSS"
else:
    status = "BREAK-EVEN"

print("\n------ BUSINESS RESULT ------")
print("Total Sales:", sales)
print("Total Expenses:", expenses)
print("Profit/Loss:", profit)
print("Status:", status)

if sales > 0:
    profit_margin = (profit / sales) * 100
else:
    profit_margin = 0

print("Profit Margin:", round(profit_margin, 2), "%")

if profit > 0:
    print("Business Performance: STRONG")
elif profit == 0:
    print("Business Performance: STABLE")
else:
    print("Business Performance: NEEDS IMPROVEMENT")

print("-----------------------------")
print("Analysis Completed")
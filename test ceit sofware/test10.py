
import json

with open('transactions.json') as json_file:
    data = json.load(json_file)

total_income = 0
total_expenses = 0

for transaction in data:
    amount = transaction['amount']

    if amount > 0:
        total_income += amount
    else:
        total_expenses += abs(amount) 

print("ລວມລາຍຮັບ:", '{:,}'.format(total_income), "ກີບ")
print("ລວມລາຍຈ່າຍ:", '{:,}'.format(total_expenses), "ກີບ")




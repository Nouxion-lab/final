import json

with open('transactions.json') as json_file:
    data = json.load(json_file)

monthly_data = {}

for transaction in data:
    date = transaction['created_at']
    amount = transaction['amount']

    month_key = date[:7]  

    if month_key not in monthly_data:
        monthly_data[month_key] = {'total_income': 0, 'total_expenses': 0}

    if amount > 0:
        monthly_data[month_key]['total_income'] += amount
    else:
        monthly_data[month_key]['total_expenses'] += abs(amount)

sorted_months = sorted(monthly_data.keys())

for month in sorted_months:
    data = monthly_data[month]
    display_month = month[5:] 
    print("--------------------------------------------")
    print("ເດືອນ", display_month)
    print("ລວມລາຍຮັບ:", '{:,}'.format(data['total_income']), "ກີບ")
    print("ລວມລາຍຈ່າຍ:", '{:,}'.format(data['total_expenses']), "ກີບ")
import random
print()
company1 = {"sales_income": 100, "costs": 90, "funds": 100, "level": 1}
user_money = 100

def time(user_money):

    # Add stocks to funds
    user_stock = int(input("How much do you want to give the company? "))
    company1["funds"] += user_stock

    # Company upgrades if it has enough funds
    if company1["funds"] >= 100:
        company1["funds"] -= 100
        company1["level"] += 1
        company1["sales_income"] += 100
        user_money += company1["sales_income"] * 0.01 * user_stock
        company1["costs"] = (company1["costs"] * 0.9) + (company1["sales_income"] * 0.01 * user_stock)
        print(company1)
        print(user_money)

time(user_money)


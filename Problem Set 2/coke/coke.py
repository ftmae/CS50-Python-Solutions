accepted_coins = [5,10,25]
amount_due = 50
paid = 0

while(paid < amount_due):
    print(f"Amount Due: {amount_due-paid}")
    coin = int(input("Insert Coin: "))
    if coin in accepted_coins:
        paid += coin
    else:
        print("Coin Inserted is Not Accepted")

print(f"Change Owed: {paid-amount_due}")



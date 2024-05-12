command = input()
account = 0.0

while command != "NoMoreMoney":
    amount_transfer_account = float(command)
    if amount_transfer_account > 0:
        account += amount_transfer_account
        print(f"Increase: {amount_transfer_account:.2f}")
    else:
        print("Invalid operation!")
        break
    command = input()
print(f"Total: {account:.2f}")

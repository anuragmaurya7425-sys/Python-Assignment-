# Write a program using finally and custom exceptions

class nagativeAmountError(Exception):
    pass

try:
    amount = int(input("Enter amount to withdraw :"))
    
    if amount < 0:
        raise nagativeAmountError("Amount can not be nagative !")
    
    balance = 10000
    
    if amount > balance:
        print("Insufficient balance ")
    else:
        balance -= amount
        print("Withdraw successful✔👍")
        print(f"Remaining balance is :{balance}")

except nagativeAmountError as e :
    print(f"Costom error :{e}")

except ValueError:
    print("Error! :Please enter a valid number ")

finally:
    print("Transaction process complete ✔🤞")
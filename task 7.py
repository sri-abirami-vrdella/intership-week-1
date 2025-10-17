"""Create a Python program that simulates a simple ATM withdrawal
 process using exception handling to manage user input errors and
 insufficient balance situations."""


#custom exceptions
class negativeamountError(Exception):
    pass

class InsufficientbalanceError(Exception):
    pass

class notmultipleof100Error(Exception):
    pass

class cardnoandpinnotmatchError(Exception):
    pass

#initial balance
balance=0

try:
    card_no=int(input("Enter card no: "))
    pin=int(input("Enter pin: "))
    if card_no==12345678 and pin==5009:
        while True:
            a=int(input("\nEnter your choice:\n1.withdraw\n2.deposit\n3.check balance\n "))
            #---------withdraw block-------------
            if a==1:
                try:
                    amount=int(input("Enter your amount: "))
                    if amount<0:
                        raise negativeamountError("amount cannot be negative")
                    elif amount>balance:
                        raise InsufficientbalanceError("There is no sufficient balance")
                    else:
                        balance=balance-amount
                except (negativeamountError,InsufficientbalanceError) as e:
                    print(e)
                else:
                    print("Amount withdrawn successfully\n")
                finally:
                    print("Your balance is:",balance)

            #------------deposit block--------------------
            elif a==2:
                amount=int(input("Enter your amount: "))
                try:
                    if amount<0:
                        raise negativeamountError("amount cannot be negative")
                    elif amount%100!=0:
                        raise notmultipleof100Error ("Deposit amount should be multiple of 100 ")
                    else:
                        balance=balance+amount
                except (negativeamountError, notmultipleof100Error) as e:
                    print(e)
                else:
                    print("amount deposited successfully\n")
                finally:
                    print("Your balance is:",balance)


            #----------check balance blocl
            else:
                print("you balance = ",balance)
    else:
        raise cardnoandpinnotmatchError("cardno or pin doesnot match")
except ValueError:
    print("Invalid input")
except cardnoandpinnotmatchError as e:
    print(e)
except :
    print("something went wrong")
finally:
    print("Thank you for using, visit again")


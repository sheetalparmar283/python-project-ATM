balance = 5000
correct_pin = 1234
print("===welcome to the python ATM ===")
attempts = 3
authenticated = False 
while attempts > 0:
    user_pin = int(input("enter your pin : "))
    if user_pin == correct_pin:
        print("verified")
        authenticated = True
        break
    else:
        attempts = attempts-1
        print("wrong pin,attempt left:{attempts}")
if not authenticated:
    print("card blocked! too many wrong attempts")
else:
    while True:
        print("\n---ATM menu---")
        print("1---balance check---")
        print("2---deposit money---")
        print("3---withdraw money---")
        print("4---Exit---")   
        choice = input("select choice")
        match choice:
            case "1":
                print(f"your balance:RS{balance}")
            case "2":
                amount = int(input("enter amount"))
                if amount > 0:
                    balance = balance + amount
                    print(f"deposited RS{amount}, updated balance{balance}")
                else:
                    print("invalid amount")
            case "3":
                amount = int(input("enter withdrawl amount"))
                if amount <= balance:
                   if balance-amount <= 500:
                       print("you have min balance of 500 only")
                   else:
                       balance = balance - amount
                       print(f"withdraw RS: {amount},remain: {balance}") 
                else:
                    print("insufficient balance")
            case "4":
                print("thank you for using ATM,please take ur card")
                break
            case _:
                print("invalidchoice,please enter 1,2,3,4")  
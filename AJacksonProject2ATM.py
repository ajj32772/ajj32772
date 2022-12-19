


# This Program provide functionality about ATM operation
# we can check total balance
# we can withdraw money
# we can desposit money




Accounts = {"Harry":300, "John": 700, "David": 100, "Honey": 900, "Adam":500}



# definig showBalance function
def showBalance(username):
    total = Accounts[username]
    print(username,"! you have total balance:",total, "$")



#defining withdraw money function

def withdraw(username,amount):
    total = Accounts[username]
    # cheking if account has money equal or greater than withdraw amount or not
    if amount > total:
        print(" Sorry! you have not enough amount to withdraw")
    else:
        total = total - amount
        Accounts[username] = total  # updating total of current user
        print(" withdraw Successfully! Now your remaining total balacne is:",total,"$")



# defining deposit function to add money in user account
def deposit(username,amount):
    total = Accounts[username] #getting previus total
    total = total + amount
    Accounts[username] = total #updating total to current user
    print("deposit successfully! Now your total balance is:",total,"$")




# defining showMenu()function
def showMenu():
    print("what would you want to do..................")
    print("Enter 1 for check total balance.")
    print("Enter 2 for withdraw Money.")
    print("Enter 3 for Deposit Money.")
    print("Enter end to finish.")




def main():
    choice = input("Enter Your Choice:")
    while choice != "end":
        choice = int(choice)
        
        if choice == 1:
            username = input("Enter username to check the balance: ")
            showBalance(username)
            
        elif choice == 2:
            amount = int(input("How much amount you want to withdraw:"))
            username = input("Enter username")
            withdraw(username,amount)
            
            
        elif choice == 3:
            amount = int(input("How much amount you want to deposit:"))
            username = input("Enter username")
            deposit(username,amount)
            
        else:
            print("Invalid choice")
            
            
        showMenu()
        choice = input("Enter Your Choice:")
            
        
                             


print("======Welcome at ATM=====")
showMenu()
main()
print("Thanks! for using ATM")







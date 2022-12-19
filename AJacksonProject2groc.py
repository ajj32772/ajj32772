


#creating Grocery Store inventory dictionary
Inventory = {"egg":20, "yogurt":40, "salt":60, "milk":30, "honey":100, "pepper":70}



# function to show items with prices
def showItemList():
    print("Grocery Store Item Rate List")
    print("============================")
    print("item\t\t\tprice")
    for item in Inventory:
        print(item,"\t\t\t",Inventory[item],"$",sep = "")
    print("type done to finish shopping...")



# adding item in list
def addItems(item):
    itemList.append(item)
    priceList.append(Inventory[item])



# function to show bill
def showBill():
    print("Your Shopping Cart")
    print("====================")
    print("item\t\tprice")
    
    #getting purchase item
    for item in itemList:
        print(item,"\t\t",Inventory[item],"$",sep = "")
        
    #calculated total bill of shopping
    print("====================")
    print("total:\t\t",sum(priceList),"$",sep = "")
          


# main function to entery point of program
def main():
    
    showItemList()
    
    item = input("What would you like to add in your list:")
    
    while item.lower() != "done":
        addItems(item) # adding item in list
        showItemList() # showing grocery store item list
        item = input("What would you like to add in your list:")
        
    # showing bill of purchase item
    showBill()
    
        


itemList = []
priceList = []
main()






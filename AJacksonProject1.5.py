

# Unit Converter for length

# function to display options for coversion
def displayOptions():
    print("1-Mile to Kilometre")
    print("2-Yard to Metre")
    print("3-Metre to Foot")
    print("4-Foot to Centimetre")
    print("5-Inch to Centimeter")
    print("stop- finish the conversion----")



def Converter(choice):
    choice = int(choice)
    if choice == 1:
        Mile = int(input("Enter value in Miles:"))
        Kilometre =  Mile * 1.609 
        return str(Kilometre) + " Kilometres"
    
    elif choice == 2:
        yard = int(input("Enter value in yard:"))
        Metre = yard * 0.9144
        return str(Metre) + " Metres"
    
    elif choice == 3:
        Metre = int(input("Enter value in Metre:"))
        Foot =Metre * 3.281
        return str(Foot) + " Feet"
    
    elif choice == 4:
        Foot = int(input("Enter value in Foot:"))
        Centimetre = Foot * 100
        return str(Centimetre) + " Centimetre"
    
    elif choice == 5:
        Inch = int(input("Enter value in Inch:"))
        Centimetre = Inch * 2.54
        return str(Centimetre) + " Centimetre"
    else:
        print("Invalid option! Select again")
    
        


#defining main function
def main():
    displayOptions()
    
    choice = input("Choose any option from list:") 
    
    while choice.lower() != "stop":
        
        result = Converter(choice)
        
        print("Converted Successfully.....",result)
        
        displayOptions()
    
        choice = input("Choose any option from list:")
        
    print(".....Thanks for Using our Unit Converter.....")




print("==========| Welcome on Length Unit Converter |==========")
main()






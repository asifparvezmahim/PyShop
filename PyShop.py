product_list=[
        {"id": 1 , "name": "Wallet" , "price": 200},
        {"id": 2 , "name": "Belt" , "price": 800},
        {"id": 3 , "name": "Perfume" , "price": 600}
]

my_cart=[]
def menu():
    print("Press 1 to Visit Our Products")
    print("Press 2 to Purchase Our Products")
    print("Press 3 to Remove Product From Cart")
    print("Press 4 to View Cart")
    print("Press 5 to Check Out")
    print("Press 6 to Stop")

def show_product_list():
    for product in product_list:
        print(product)
    print("\n\n")

def purchase_product():
    print(product_list)
    product_id=int(input("Enter Product ID: "))
    for product in product_list:
        if product["id"]==product_id:
            print(product)
            print("Do You Want to Add Cart ?\nIf YES , Press 1\nElse Press 2")
            dicission_taking=int(input("Enter Your Choice :"))
            if dicission_taking==1:
                my_cart.append(product)
                print("Product is added successfully\nThank You for Shopping With Us")
                print("Your Updated Cart: ",my_cart)
            elif dicission_taking==2:
                print("Thank You")
            else:
                print("Key is Not Valid")
            return       
    print("No Product Found")

def remove_from_cart():
    print("Your Cart: ",my_cart)
    id=int(input("Enter Product ID You Want to Remove From Cart: "))
    for cart_item in my_cart:
        if cart_item["id"]==id:
            my_cart.remove(cart_item)
            print("Product is Removed Successfully")
            print("Your Updated Cart is : ",my_cart)
            return
    print("No Product Found with This ID")
    
def view_cart():
    print("Your Cart: ",my_cart)


def checkout():
    total=0
    for cart_item in my_cart:
        total=total+cart_item["price"]
    print ("Your Total Bill: ",total)
    print("Do You Want To Confirm Your Order?")
    print ("If Yes, Press 1\nElse Press Any Key")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        print("Billing is Complete\nThank You For Shopping With PyShop")
    else:
        print("Thank You !!!")


#main code starts
print("----WELCOME TO PyShop----")
while True:
    menu()
    print("Chose Your Option")
    chosen_opt=int(input("Type a Valid Number: "))
    if chosen_opt==1:
        show_product_list()
    elif chosen_opt==2:
       purchase_product()
    elif chosen_opt==3:
       remove_from_cart()
    elif chosen_opt==4:
        view_cart()
    elif chosen_opt==5:
        checkout()
    elif chosen_opt==6:
        break
    else:
        print("Please Enter a Valid Number")
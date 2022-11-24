product=[]

ent=input("Enter product:")
lower=ent.lower()

product.append(lower)
def add_another():
    ent=input("Would you like to add another Y?N:")
    low=ent.lower()
    if low == "y":
        x=input("Adding another item:")
        low=x.lower()
        product.append(low)
        add_another()
    elif low =="n":
        print("Showing your items:",product)
        print("Thanks for shopping with us 😃")
    else:
        print("Invalid entry")
        add_another()        
add_another()


def search():
    ent=input("Do you want to search for item Y?N:")
    low=ent.lower()
    if low =="y":
        w=input("Enter search item:")
        w_low=w.lower()
        if w_low in product:
            count=product.count(w_low)
            print("Product found")
            print("The number of",w_low,"in product is:",count)
            total=len(product)
            print("Total number of product is:",total)
            search()
        else:
            print(w_low,"not found")
            search()
    elif low == "n":
        print("Exiting...")
    else:
        print("Invalid input try again")
        search()
search()

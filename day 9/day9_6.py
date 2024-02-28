bid = {}


oif = False
while not oif:
    name = input("enter the name: ")
    price = input("enter the bid: ")
    bid[name]= price
    cont = input("are there any more bids: ")
    if cont == "no":
         for key in bid:
            print(key,bid[key])
            oif =True
    elif cont == "yes":
        high(bid)
        oif = False
       
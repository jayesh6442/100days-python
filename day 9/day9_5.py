bid = {}
bidding_finished= False
def high(bidding_record):
    highest_bit = 0
    for bidr  in  bidding_record:
        bidding_amount=bidding_record[bidr]
        if bidding_amount > highest_bit:
            highest_bit = bidding_amount
            winner=bidr
    print(f'the winner is {winner} with bid of {highest_bit}' )
while not bidding_finished: 
    name = input("enter the name")
    prise = int(input("enter the bid"))
    bid[name]=prise
    should_continue = input("are ther any more bids\n")
    if should_continue =="no":
        bidding_finished =  True 
        high(bid)
    elif should_continue =="yes":
        print("jsdaf")

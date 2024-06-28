##import os 
def find_winner(bidder_details):
    highest_bid=0
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print("The Winner Is",winner,"with a bid price of",highest_bid)

bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name=input("enter your name:")
    bid_price=int(input("Enter your bid price:"))
    bidder_data[name]=bid_price
    more_bidders=input("Are there more bidders? Type 'Yes' or 'no': ").lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
##    elif more_bidders=='yes':
##        os.system('cls')

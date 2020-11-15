from art import logo
from os import system


bids = {}
takingBids = True


while takingBids:
    print(logo)
    name = input("What is your name?\n")
    bid = float(input("What is your bid?\n$"))
    bids[name] = bid
    system('cls')
    continueBidding = input("Are there more bidders, YES or NO?\n").lower()
    system('cls')
    if continueBidding == "no":
        takingBids = False


winningBid = max(bids, key=bids.get)

print(f"{winningBid} won the auction with a bid of ${bids[winningBid]}.")
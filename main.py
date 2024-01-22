import os
from art import logo

print(logo)

def clear():
  os.system('cls')

bids = {}
bidding_finished = True

def find_highest_bidder(bidding_record):
  max_bid = max(bids.values())
  for key, value in bids.items():
    if value == max_bid:
      print(f"The winner is {key} with a bid of {value}")


while bidding_finished:
  name = input("What is your name?:")
  price = int(input ("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if should_continue == 'yes':
    clear()
  elif should_continue == 'no':
    find_highest_bidder(name)
    bidding_finished = False
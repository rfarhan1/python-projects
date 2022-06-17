import os
import art


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



print(art.logo)

auction_log = {}


def add_entry(participant_name, value):
    auction_log[participant_name] = value


continue_bid = True
while continue_bid:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    add_entry(name, bid)
    more_entry = input("Type 'Yes' to continue entry. Otherwise type 'No': ").lower()
    if more_entry == "no":
        continue_bid = False
    clear_console()
highest_bid = 0
winner = ""

for people in auction_log:
    if auction_log[people] > highest_bid:
        highest_bid = auction_log[people]
        winner = people

print(f"Winner is {winner} bidding ${highest_bid}")

print(auction_log)

with open("input_day4.txt") as file:
    lines = [line.strip() for line in file]

card_info = {"card": 0, "winning_numbers": [], "card_numbers": []}

for line in lines:
    card = line.split(":")[0].split()[1]
    print(card)
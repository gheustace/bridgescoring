# team, bid amt., suit, multiplier, result
current_bid = []
us = [0, [0], False]
them = [0, [0], False]

def add_score(team, other_team):
    multiplier = current_bid[3]
    vulnerable = False
    expected = current_bid[1] + 6
    actual = current_bid[4]
    if team[1][0] >= 100:
        vulnerable = True
    if actual >= expected: # overtricks or even
        if current_bid[2] != 40:
            if vulnerable:
                if len(team[1]) == 1:
                    team[1].append(0)
                team[1][1] += current_bid[2] * (expected - 6) * multiplier
            else:
                team[1][0] += current_bid[2] * (expected - 6) * multiplier
        else:
            if vulnerable:
                if len(team[1]) == 1:
                    team[1].append(0)
                team[1][1] += 40 * multiplier
                team[1][1] += 30 * (expected - 7) * multiplier
            else:
                team[1][0] += 40 * multiplier
                team[1][0] += 30 * (expected - 7) * multiplier
            current_bid[2] = 30
        if multiplier == 1:
            team[0] += (actual - expected) * current_bid[2]
        if multiplier == 2:
            if vulnerable:
                team[0] += (actual - expected) * 200
            else:
                team[0] += (actual - expected) * 100
        if multiplier == 4:
            if vulnerable:
                team[0] += (actual - expected) * 400
            else:
                team[0] += (actual - expected) * 200
        if expected == 12: # slam bonus
            if vulnerable:
                team[0] += 750
            else:
                team[0] += 500
        if expected == 13: # grand slam bonus
            if vulnerable:
                team[0] += 1500
            else:
                team[0] += 1000
    elif actual < expected: # undertricks
        if multiplier == 1:
            if vulnerable:
                other_team[0] += (expected - actual) * 100
            else:
                other_team[0] += (expected - actual) * 50
        if multiplier == 2:
            if vulnerable:
                other_team[0] += 200
                other_team[0] += (expected - actual - 1) * 300
            else:
                other_team[0] += 100
                other_team[0] += (expected - actual - 1) * 200
        if multiplier == 4:
            if vulnerable:
                other_team[0] += 400
                other_team[0] += (expected - actual - 1) * 600
            else:
                other_team[0] += 200
                other_team[0] += (expected - actual - 1) * 400
    if len(team[1]) != 1:
        if team[1][1] >= 100: # rubber bonus
            if other_team[1][0] > 100:
                team[0] += 500
            else:
                team[0] += 700
    return [team, other_team]
 
def view_score():
    space1 = len(str(us[0]))
    space2 = len(str(us[1][0]))
    if len(us[1]) != 1:
        space3 = len(str(us[1][1]))
    print("-----us-----||----them----")
    print(f"{us[0]}" + (12 - space1) * " " + f"||{them[0]}")
    print("------------||------------")
    print(f"{us[1][0]}" + (12 - space2) * " " + f"||{them[1][0]}")
    if len(us[1]) != 1 or len(them[1]) != 1:
        print("------------||------------")
        if len(us[1]) != 1 and len(them[1]) != 1:
            print(f"{us[1][1]}" + (12 - space3) * " " + f"||{them[1][1]}")
        elif len(us[1]) == 1 and len(them[1]) != 1:
            print(12 * " " + f"||{them[1][1]}")
        elif len(us[1]) != 1 and len(them[1]) == 1:
            print(f"{us[1][1]}" + (12 - space3) * " " + "||")
    print("\n")

def new_round():
    current_bid.clear()
    team = """Who is bidding:
1) Us
2) Them

Your Selection: """
    player = input(team)
    while True:
        if player == "1":
            current_bid.append("us")
            break
        elif player == "2":
            current_bid.append("them")
            break
        else:
            print("Enter a valid command.")
            player = input(team)
    amount = input("How many: ")
    current_bid.append(int(amount))
    bid = """What suit would you like to bid:
1) Clubs
2) Diamonds
3) Hearts
4) Spades
5) No Trump

Your Selection: """
    suit = input(bid)
    while True:
        if suit == "1" or suit == "2":
            current_bid.append(20)
            break
        elif suit == "3" or suit == "4":
            current_bid.append(30)
            break
        elif suit == "5":
            current_bid.append(40)
            break
        else:
            print("Enter a valid command.")
            suit = input(bid)
    doubled = """Double or redouble:
1) None
2) Double
3) Redouble

Your Selection: """
    multiplier = input(doubled)
    while True:
        if multiplier == "1":
            current_bid.append(1)
            break
        elif multiplier == "2":
            current_bid.append(2)
            break
        elif multiplier == "3":
            current_bid.append(4)
            break
        else:
            print("Enter a valid command.")
            multiplier = input(doubled)
    score = input("Tricks won: ")
    current_bid.append(int(score))
    global us
    global them
    if current_bid[0] == "us":
        to_add = add_score(us, them)
        us = to_add[0]
        them = to_add[1]
    else:
        to_add = add_score(them, us)
        them = to_add[0]
        us = to_add[1]

menu = """Select on of the following options:
1) View Score
2) New Round
3) Exit

Your Selection: """

def main():
    command = input(menu)
    while command != "3":
        if command == "1":
            view_score()
        elif command == "2":
            new_round()
        else:
            print("Enter a valid command.")
        command = input(menu)
    print("Program exited.")


if __name__ == "__main__":
    main()
else:
    pass

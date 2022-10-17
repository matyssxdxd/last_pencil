# Winning strategy function for bot
def jack_bot(pencil):
    if pencil == 1:
        jack_turn = 1
    elif pencil == 2 or pencil % 4 == 2:
        jack_turn = 1
    elif pencil == 3 or pencil % 4 == 3:
        jack_turn = 2
    elif pencil == 4 or pencil % 4 == 0:
        jack_turn = 3
    elif pencil % 4 == 1:
        jack_turn =2
    return jack_turn


players = ["John", "Jack"]
turn_choice = [1, 2, 3]

# Asks user to input how many pencils it would like to use for the game        
print("How many pencils would you like to use: ")
while True:
    try:
        pencil_count = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
        continue
    if pencil_count <= 0:
        print("The number of pencils should be positive")
        continue
    break

# User chooses if he starts the game or bot (Jack)
print("Who will be the first (John, Jack): ")
while True:
    player = input()
    if player not in players:
        print("Choose between 'John' and 'Jack': ")
        continue
    break

# The game itself
while True:
    if pencil_count == 0:
        print(f"{player} won!")
        break
    print(pencil_count * "|")
    print(f"{player}'s turn: ")
    if player == "Jack":
        print(jack_bot(pencil_count))
        turn = jack_bot(pencil_count)
        player = "John"
    else:
        while True:  # Asks for user to input how many pencils he would take, prevents errors with input
            try:
                turn = int(input())
            except ValueError:
                print("Possible values: '1', '2', '3'")
                continue
            if turn not in turn_choice:
                print("Possible values: '1', '2', '3'")
                continue
            elif turn > pencil_count:
                print("Too many pencils were taken")
                continue
            player = "Jack"
            break
    pencil_count = pencil_count - turn
            
    
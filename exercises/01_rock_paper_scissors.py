import random

def print_result (user, cp, winner):
    global user_V
    global cp_V
    global ties
    print('*' * 80)
    print(f"\t\tResult: {user} VS {cp} => WINNER: {winner}")
    if winner == 'User':
        user_V += 1
    elif winner == 'Computer':
        cp_V += 1
    else:
        ties += 1
    print("\t\t ----------- PUNCTUATION -----------")
    print(f"\t\t\tUser: {user_V} CP: {cp_V} Ties:{ties}")
    print('*' * 80)

user_V = 0
cp_V = 0
ties = 0
game = True
while game:
    while (user_V < 2 and cp_V < 2):
        print("\t\t\tPLAY TO THE BEST OF THREE")
        user_option = input('CHOOSE ONE: rock, paper OR scissors: ').lower()
        options = ('rock','paper', 'scissors')
        computer_option= random.choice(options)

        if user_option == computer_option:
            print_result(computer_option, computer_option, 'TIE')
        elif user_option == 'rock':
            if computer_option == 'paper':
                print_result('rock', 'paper', 'Computer')
            elif computer_option == 'scissors':
                print_result('rock', 'scissors', 'User')
        elif user_option == 'paper':
            if computer_option == 'rock':
                print_result('paper', 'rock', 'User')
            elif computer_option == 'scissors':
                print_result('paper', 'scissors', 'Computer')
        elif user_option == 'scissors':
            if computer_option == 'paper':
                print_result('scissors', 'paper', 'User')
            elif computer_option == 'rock':
                print_result('scissors', 'rock', 'Computer')
        else:
            print("That is not an option!")

    if user_V == 2:
        print("\t\t>>>>>> USER IS THE WINNER!!!! <<<<<<<")
    if cp_V == 2:
        print("You lose try again...")

    set_flag = True
    while set_flag:
        set = input('Other set? yes or no: ').lower()
        if set == 'no':
            game = False
            set_flag = False
            print('Thanks for playing')
        elif set == 'yes':
            set_flag = False
            user_V = 0
            cp_V = 0
            ties = 0
        else:
            print('Option invalid')
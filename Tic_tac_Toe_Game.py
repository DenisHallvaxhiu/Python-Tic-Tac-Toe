from IPython.display import clear_output

game_list=[" "," "," "," "," "," "," "," "," "]
choice_list =["1","2","3","4","5","6","7","8","9"]
game_on = True
def display_game(game_list):
    clear_output(True)
    print( "   |   |   ")
    print(f" {game_list[6]} | {game_list[7]} | {game_list[8]}")
    print( "   |   |   ")
    print("-----------")
    print( "   |   |   ")
    print(f" {game_list[3]} | {game_list[4]} | {game_list[5]}")
    print( "   |   |   ")
    print("-----------")
    print( "   |   |   ")
    print(f" {game_list[0]} | {game_list[1]} | {game_list[2]}")
    print( "   |   |   ")
    

def position_choice(turn):
    
    choice = "wrong"
    
    while choice not in ["1","2","3","4","5","6","7","8","9"]:  
        choice = input(f"{turn} - Pick a position (1-9)\n")
        if choice not in ["1","2","3","4","5","6","7","8","9"]:
            print("Invalid choice")
        elif game_list[int(choice)-1]!=" ":
            choice="wrong"
            print("Already choosen!")
            
    return int(choice)
    
def player():
    choice = " "
    
    while choice not in ["X","O"]:
        
        choice = input("Which player are you? (X or O)\n")
        if choice not in ["X","O"]:
            print("Invalid choice")
    
    return choice

def place_maker(player,position):
    game_list[position-1]=player
    display_game(game_list)

def win_check():
        if game_list[0] == game_list[1] == game_list[2]!=" " : return True
        elif game_list[3] == game_list[4] == game_list[5]!=" " : return True
        elif game_list[6] == game_list[7] == game_list[8]!=" " : return True
        elif game_list[0] == game_list[3] == game_list[6]!=" " : return True
        elif game_list[1] == game_list[4] == game_list[7]!=" " : return True
        elif game_list[2] == game_list[5] == game_list[8]!=" " : return True
        elif game_list[0] == game_list[4] == game_list[8]!=" " : return True
        elif game_list[2] == game_list[4] == game_list[6]!=" " : return True
        elif " " not in game_list: return "Draw"
        else: return False

def switch_turn(turn):
    if turn=="X":
        return "O"
    else:
        return "X"

def continue_playing():
    choice = " "
    
    while choice not in ["Y","N"]:
        
        choice = input("Would you like to continue? (Y or N)\n")
        if choice not in ["Y","N"]:
            print("Invalid choice")
    
    if choice == "Y":
        return True
    else:
        return False


turn = player()

while game_on:
    position = position_choice(turn)
    place_maker(turn,position)
    if win_check()==True: 
        game_list=[" "," "," "," "," "," "," "," "," "]
        print(f"Congratulation {turn}")
        play_again = continue_playing()
        if play_again:
            turn = player()
            continue
        else:
            break
    elif win_check()=="Draw":
        game_list=[" "," "," "," "," "," "," "," "," "]
        print("Draw!!")
        play_again = continue_playing()
        if play_again:
            turn = player()
            continue
        else:
            break
        
    turn = switch_turn(turn)
    

import random

# Define your numbers
numbers = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

def check_winner(board, player):

    winning_combinations = [
        ["1","2","3"], ["4","5","6"], ["7","8","9"],  
        ["1","4","7"], ["2","5","8"], ["3","6","9"],  
        ["1","5","9"], ["3","5","7"]                  
    ]
    

    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

game_on = True
while game_on:

    print(
        f"  {numbers['1']}  |  {numbers['2']}  |  {numbers['3']}  \n"
        "-----------------\n"
        f"  {numbers['4']}  |  {numbers['5']}  |  {numbers['6']}  \n"
        "-----------------\n"
        f"  {numbers['7']}  |  {numbers['8']}  |  {numbers['9']}  \n"
    )
    choice = input("Player1\nWhere do you want to play? ")
    if choice in numbers and str(numbers[choice]) == choice:
        numbers[choice] = "X"
        if check_winner(numbers, "X"):
            print("Player 1 wins!")
            break
    else:
        continue


    print(
        f"  {numbers['1']}  |  {numbers['2']}  |  {numbers['3']}  \n"
        "-----------------\n"
        f"  {numbers['4']}  |  {numbers['5']}  |  {numbers['6']}  \n"
        "-----------------\n"
        f"  {numbers['7']}  |  {numbers['8']}  |  {numbers['9']}  \n"
    )
    choice2 = input("Player2\nWhere do you want to play? ")
    if choice2 in numbers and str(numbers[choice2]) == choice2:
        numbers[choice2] = "O"
        if check_winner(numbers, "O"):
            print("Player 2 wins!")
            break
    else:
        continue



    
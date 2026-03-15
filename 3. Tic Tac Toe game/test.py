import random

# Define your numbers (board)
numbers = {str(i): str(i) for i in range(1, 10)}

def print_board(board):
    print(
        f"  {board['1']}  |  {board['2']}  |  {board['3']}  \n"
        "-----------------\n"
        f"  {board['4']}  |  {board['5']}  |  {board['6']}  \n"
        "-----------------\n"
        f"  {board['7']}  |  {board['8']}  |  {board['9']}  \n"
    )

def check_winner(board, player):
    # All possible winning combinations
    combos = [
        ["1","2","3"], ["4","5","6"], ["7","8","9"],
        ["1","4","7"], ["2","5","8"], ["3","6","9"],
        ["1","5","9"], ["3","5","7"]
    ]
    for combo in combos:
        if all(board[pos] == player for pos in combo):
            return True
    return False

def ai_move(board):
    # Pick a random empty spot
    empty = [k for k,v in board.items() if v not in ["X","O"]]
    return random.choice(empty)

game_on = True
while game_on:
    # Player turn
    print_board(numbers)
    player_choice = input("Your turn! Pick a spot (1-9): ")
    if player_choice in numbers and numbers[player_choice] not in ["X","O"]:
        numbers[player_choice] = "X"
        if check_winner(numbers, "X"):
            print_board(numbers)
            print("You win! 🎉")
            break
    else:
        print("Invalid move. Try again.")
        continue

    # AI turn
    ai_choice = ai_move(numbers)
    numbers[ai_choice] = "O"
    print(f"AI played at {ai_choice}")
    if check_winner(numbers, "O"):
        print_board(numbers)
        print("AI wins! 💻")
        break

    # Check tie
    if all(v in ["X","O"] for v in numbers.values()):
        print_board(numbers)
        print("It's a tie! 🤝")
        break
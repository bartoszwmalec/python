import random, sys

# definition of icons used in console for better user experience
moves: dict = {'rock':'🗿', 'paper':'📄', 'scissors':'✂️'}
# valid_moves limits the possibilities to allow only to proper choices
valid_moves: list[str] = list(moves.keys())

print("Welcome to RPS!")

# STEP 2: INFINITE LOOP (for waiting for user interaction)
while True:
    user_move: str = input('Rock, paper or scissors?: (Type \'exit\' to quit).   ').lower()

    if user_move == 'exit':
        print('Thanks for playing.')
        sys.exit()

    if user_move not in valid_moves:
        print('Please make a valid move!')
        continue

    # AI makes a random move - one choice from the list of valid_moves
    ai_move: str = random.choice(valid_moves)

    print("-" * 30)
    print(f"Your move: {moves[user_move]}")
    print(f"AI move: {moves[ai_move]}")
    print("\n")

    # Check moves
    if user_move == ai_move:
        print('It\'s a tie!')
    elif user_move == 'rock' and ai_move == 'scissors':
        print('You win!')
    elif user_move == 'scissors' and ai_move == 'paper':
        print('You win!')
    elif user_move == 'paper' and ai_move == 'rock':
        print('You win!')
    else:
        print("AI wins...")

    print("-" * 30)

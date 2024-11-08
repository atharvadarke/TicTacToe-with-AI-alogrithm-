import random 
board=[' ' for _ in range(0,9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    
def check_winner(player):
    winner_conditions = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for conditions in winner_conditions:
        if board[conditions[0]]==board[conditions[1]]==board[conditions[2]]==player:
            return True
    return False
        
def check_draw():
    return ' ' not in board

def minimax(is_maximizing):
    if check_winner('X'):
        return -1
    elif check_winner('O'):
        return 1
    elif check_draw():
        return 0
        
    if is_maximizing:
        best_score = -float('inf')
        for i in range(0,9):
            if board[i]==' ':
                board[i]='O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(0,9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score,score)
        return best_score

def make_move(position,player):
    if board[position]==' ':
        board[position] = player
        return True
    return False
    
def make_human():
    try:
        position = int(input("Make your move(1-9): "))-1
        if position<0 or position>8:
            print("invalid input, try again")
            make_human()
        if not make_move(position,'X'):
            print("position is already taken")
            make_human()
            
    except ValueError:
        print("Enter a proper integer value")
        make_human()
        
def make_computer():
    best_score = -float('inf')
    best_index = None              #This the index of the best move
    for i in range(0,9):
        if board[i]==' ':
            board[i]='O'
            score = minimax(False)
            board[i] = ' '
            if score>best_score:
                best_score = score
                best_index = i
    
    if best_index is not None:
        make_move(best_index,'O')            

def play_game():
    print("welcome")
    print_board()
    
    while True:
        
        make_human()
        print_board()
        if check_winner('X'):
            print("You won!")
            break
        if check_draw():
            print("Game draw")
            break
        print("Computer is playing")
        make_computer()
        print_board()
        if check_winner('O'):
            print("Computer won!")
            break
        if check_draw():
            print("Game draw")
            break
        

play_game()

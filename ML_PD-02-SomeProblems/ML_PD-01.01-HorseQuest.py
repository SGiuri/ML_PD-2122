import random
import numpy as np


# Scriviamo una funzione che inizializzi il gioco, creando una "board" e posizionando il cavallo nella sua posizione iniziale.
# Consideriamo la possibilita' di far partire il cavallo da una delle sue posizioni "standard"
# o da una posizione casuale nella scacchiera:

def initialize_game(horse_default_position=True):
    board = np.zeros((8,8))

    # Caselle possibili di partenza del cavallo in condizioni di default
    starting_spots = [(0,1),(0,6),(7,1),(7,6)]

    if horse_default_position:
        starting_spot = random.choice(starting_spots)
    else:
        # starting_spot = (random.randint(0,7),random.randint(0,7))
        pos = random.randint(0,63)
        # unravel restituisce le coordinate della posizione in forma matriciale
        starting_spot = np.unravel_index(pos, board.shape)

    board[starting_spot] = 1

    return board


# Scrviamo una funzione che legge una board e restituisce:
# - il numero di mosse raggunto dal cavallo
# - una tupla con la posizione attuale, orizzontale e verticale
def get_horse_current_position(board):

    # utilizzo la funzione argmax che restituisce le coordinate del valore massimo
    # dopo aver linearizzato la matrice e poi unravel_index per ottenere le
    # coordinate di quel punto:
    coordinate_valore_massimo_linearizzate = np.argmax(board)
    current_h, current_v = np.unravel_index(coordinate_valore_massimo_linearizzate,
                                            board.shape)
    current_move_number = board[(current_h, current_v)]

    return current_move_number, (current_h, current_v)


# Scriviamo una funzione che legge una board e restituisce una lista delle possibili mosse disponibili
def get_available_moves(board):
    # Leggo la scacchiera e individuo il cavallo:
    _, current_position = get_horse_current_position(board)
    mosse_del_cavallo = [(2,1), (2,-1), (1,2), (1,-2),
                       (-2,1),(-2,-1), (-1,2), (-1,-2)]
    available_moves = []

    for mossa in mosse_del_cavallo:
        # calcolo la riga e la colonna in cui cascherebbe il cavallo con questa mossa:
        final_row, final_col = (current_position[0] + mossa[0],
                                current_position[1] + mossa[1])

        if check_position(final_row, final_col, board):
            available_moves.append((final_row, final_col))
    return available_moves


def check_position(final_row,final_col, board):
    # verifico che questa riga esista nella scacchiera
    if final_row not in range(0,8):
        return False
    # verifico che questa colonna esista nella scacchiera
    if final_col not in range(0,8):
        return False

    # Se arrivo fin qui, il cavallo e' dentro alla scacchiera.
    # Se in quella posizione trovo uno 0, nessun cavallo ha mai
    # trottato su quella posizione --> e' una posizione valida
    if board[(final_row,final_col)] == 0:
        return True

    # Se trovo un numero diverso da zero, in quella casella c'e' gia'
    # stato un cavallo --> Posizione NON valida
    return False





# Scriviamo una funzione che date le mosse a disposizione, ne sceglie casualmente una e la restituisce
def random_move(available_moves):
    a_random_move = random.choice(available_moves)

    return a_random_move


def random_move_heuristic(available_moves):
    heuristic_table = np.array([   [70., 60., 55., 55., 55., 55., 61., 70.],
                                   [60., 52., 37., 40., 39., 37., 53., 61.],
                                   [53., 38., 28., 30., 30., 28., 38., 52.],
                                   [55., 39., 30., 33., 33., 30., 39., 55.],
                                   [54., 40., 30., 33., 33., 30., 40., 54.],
                                   [52., 38., 28., 30., 30., 29., 38., 52.],
                                   [62., 53., 38., 40., 40., 37., 53., 62.],
                                   [70., 62., 53., 54., 55., 53., 61., 70.]])

    probability_list = []
    # Costruisco una lista delle probabilita' che contiene ciascuna delle mosse
    # disponibili con una molteplicita' pari al valore della tavola euristica
    # per quella posizione

    # per ciascuna mossa disponibile tra le mosse dispnonibili
    for available_move in available_moves:
        # ripeto un append per il numero di volte che compare
        # sulla tabella euristica per quella mossa
        for _ in range(int(heuristic_table[available_move])):
            # aggiungi la mossa alla lista
            probability_list.append(available_move)

        # probability_list += [available_move for j in range(heuristic_table[available_move])]
    return random.choice(probability_list)



# Scriviamo una funzione che legge una board e fa fare al cavallo una mossa scegliendo tra le disponibili casualmente

def move_horse(board, available_moves):
    current_move_number, _ = get_horse_current_position(board)

    horse_move = random_move_heuristic(available_moves)

    board[horse_move] = current_move_number + 1

    return board


# Scriviamo una funzione che gioca una partita completa sino a che il cavallo non puo' piu' muoversi
# A fine partita, se il parametro "verbose" e' impostato su true, stampa a video la board.
# Restituisce la board
def play_one_game(verbose = False, horse_default_start_position = True):
    # Inizializzo il gioco
    board = initialize_game(horse_default_position=horse_default_start_position)
    
    # 
    available_moves = get_available_moves(board)
    while len(available_moves) > 0:
        board = move_horse(board, available_moves)
        available_moves = get_available_moves(board)

    if verbose:
        print(board)
        print(np.max(board))

    return board
    

# Scriviamo una funzione che gioca n partite e restituisce un po' di statistiche:
# - Numero partite vinte o miglior partita,
# - Board completate o miglior Board
# - Punteggio raggiunto in media e mediana,
# - Frequenza di occupazione di alcune caselle nella board
# - vvee
def play_n_games(n= 10, verbose = False, horse_default_start_position = True):
    history_board = np.zeros((8,8))


    max_boards = 0

    for j in range(n):
        board = play_one_game(verbose = verbose,
                      horse_default_start_position = horse_default_start_position)
        history_board[board>0] += 1
        if np.max(board) > max_boards:
            max_boards = np.max(board)
            best_board = board.copy()

    # return statistics
    return best_board, history_board

# Gioca partite fino a che non raggiunge e 64 caselle
def play_multiple_games(verbose = False, horse_default_start_position = True):

    max_boards = 0

    while max_boards < 64:
        board = play_one_game(verbose = verbose,
                      horse_default_start_position = horse_default_start_position)
        if np.max(board) > max_boards:
            max_boards = np.max(board)
            best_board = board.copy()

    # return statistics
    return best_board




best_board, history_board = play_n_games(100_000, horse_default_start_position = False)

print(best_board)
print(np.max(best_board))

print(history_board)

# import seaborn as sns
# import matplotlib.pyplot as plt
#
# sns.heatmap(history_board)
# plt.show()





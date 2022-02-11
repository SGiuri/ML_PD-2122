import random

random.seed(42)
# Le librerie dei framework specifici:
import numpy as np  # Libreria che gestisce ad altissima efficienza gli array
# Le librerie dei framework specifici:
import matplotlib.pyplot as plt  # Motore grafico di python per realizzare diagrammi e fuznoni
import seaborn as sns  # Libreria che usa il motore grafico di MatplotLib con funzionalita' grafiche avanzate


# %%

def get_current_position(board):
    current_h, current_v = np.unravel_index(board.argmax(axis=None), board.shape)
    current_move_number = board.max()

    return current_move_number, (current_h, current_v)


def get_available_moves(board):
    current_move_number, (current_h, current_v) = get_current_position(board)
    moves = [(2, -1),
             (1, -2),
             (-1, -2),
             (-2, -1),
             (-2, 1),
             (-1, 2),
             (1, 2),
             (2, 1)]
    available_moves = []
    for move in moves:
        poss_h, poss_v = current_h + move[0], current_v + move[1]
        if 0 <= poss_v <= 7 and 0 <= poss_h <= 7:
            if board[poss_h, poss_v] == 0:
                available_moves.append((poss_h, poss_v))
                # print(move)
    return available_moves


def move_horse(board, heuristic=False):
    available_moves = get_available_moves(board)

    if len(available_moves) == 0:
        # print(f"No more moves after {current_move_number} moves")

        return board.max()
    if heuristic:
        board[random_heuristic_move(available_moves)] = board.max() + 1
    else:
        board[random_move(available_moves)] = board.max() + 1


def initialize_game(horse_default_position=True):
    board = np.zeros((8, 8))
    # inizial positions: (0, 2), (0, 5), (7, 2), (7, 5)
    if horse_default_position:
        inizial_position = random.choice([(0, 2), (0, 5), (7, 2), (7, 5)])
    else:
        inizial_position = np.unravel_index(random.randint(0, 63), board.shape)
    board[inizial_position] = 1
    return board


def random_move(available_moves):
    return random.choice(available_moves)


# %%

def random_heuristic_move(available_moves):
    heuristic_board = np.array([[70., 61., 53., 54., 55., 53., 61., 71.],
                                [61., 53., 37., 40., 40., 38., 54., 61.],
                                [53., 38., 28., 30., 30., 29., 37., 52.],
                                [54., 39., 31., 33., 32., 29., 40., 55.],
                                [54., 40., 30., 33., 33., 30., 40., 54.],
                                [53., 37., 28., 31., 30., 28., 38., 53.],
                                [61., 53., 37., 39., 40., 38., 53., 61.],
                                [71., 61., 53., 55., 54., 52., 61., 71.]])
    heuristic_moves = []
    for move in available_moves:
        molteplicita = int(heuristic_board[move])
        moves = [move for j in range(molteplicita)]
        # print(moves)
        heuristic_moves += moves
    return random.choice(heuristic_moves)


# %%

board = initialize_game()
available_moves = get_available_moves(board)


# print(available_moves)
# move_horse_heur(board)

# %%
def play_one_game(heuristic=False, horse_default_position=False):
    board = initialize_game(horse_default_position=horse_default_position)
    available_moves = get_available_moves(board)
    while len(available_moves) > 0:
        move_horse(board, heuristic=heuristic)
        available_moves = get_available_moves(board)
    if board.max() == 64:
        print(board)
        board[board == 1] = 0
        available_moves = get_available_moves(board)
        if len(available_moves) > 0:
            print("Il percorso e' chiuso")
        else:
            print("il percorso e' aperto")
        board[board == 0] = 1
    return board


# %%
def plot_results(results):
    valori, frequenza = np.unique(results, return_counts=True)

    # imposto lo stile con sfondo grgietto
    sns.set_style("darkgrid")

    # scrivo la stringa che contiene il titolo
    title = f"Diagramma delle frequenze di {len(results)} tiri di dado"
    # creo l'oggetto axes, il digramma vero e proprio

    axes = sns.barplot(x=valori, y=frequenza)

    # metto su axes il titolo
    axes.set_title(title, fontsize=14)

    # metto le etichette sull'asse x e sull'asse y
    axes.set(xlabel="Valore", ylabel="Frequenza")

    # alzo il limite massimo sull'asse y per farci stare alcune informazioni sulla
    axes.set_ylim(top=max(frequenza) * 1.15)
    axes.set_xlim(max(valori))
    # plt.xticks([10,20,30,40,50,60])
    # mostra il diaramma a video (necessario su configurazioni non IPython)
    plt.show()


# %%
def play_multiple_games(iteration=10,
                        heuristic=False,
                        horse_default_position=False):
    complete_boards = []
    iteration = iteration
    first_board = play_one_game(heuristic=heuristic,
                                horse_default_position=horse_default_position)
    if first_board.max() == 64:
        complete_boards.appens(first_board)
    results = np.array([first_board.max()])

    first_one_board = first_board.copy()
    first_one_board[first_one_board > 0] = 1.0
    cumulative_board = first_one_board.copy()

    for j in range(iteration - 1):
        board = play_one_game(heuristic=heuristic,
                              horse_default_position=horse_default_position)
        if board.max() == 64:
            complete_boards.append(board)
        results = np.concatenate((results, [board.max()]))
        one_board = board.copy()
        one_board[one_board > 0] = 1.0
        cumulative_board += one_board
    plot_results(results)
    print("Heuristic", heuristic)
    print(results.min(), results.max(), results.mean())
    return cumulative_board, results, complete_boards


# %%
# random.seed(42)
#
# print("Start Non Heur")
# cumulative_board1, results1, cb1 = play_multiple_games(iteration = 1_000_000,
#                         heuristic = False)
# %%
random.seed(42)
print("Start Heur")
cumulative_board2, results2, cb2 = play_multiple_games(iteration=1_000_000,
                                                       heuristic=True,
                                                       horse_default_position=True)
print("Done")
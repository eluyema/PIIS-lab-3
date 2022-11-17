import chess
from algorithm import Negamax, Negascout, PVS

class Game:
    def __init__(self, board: chess.Board, method):
        self.board = board
        self.basicDepth = 4
        self.method = method
    
    def _moveUser(self):
        print("Now is your turn! Your passible moves: ", self.board.legal_moves,'\n')
        move = input("Enter your move: ")
        self.board.push_san(move)
    
    def _moveComputer(self):
        bestMove = chess.Move.null

        if self.method == 'negamax':
            bestMove = Negamax(self.board, self.basicDepth)[1]
        elif self.method == 'negascout':
            bestMove = Negascout(self.board,self.basicDepth, -1000000,1000000)[1]
        elif self.method == 'pvs':
            bestMove = PVS(self.board,self.basicDepth, -1000000,1000000)[1]
        else:
            bestMove = Negamax(self.board, self.basicDepth)[1]

        print('Best move is: ', bestMove)
        self.board.push(bestMove)

        return

    def start(self):
        currentTurn = chess.WHITE
        while not self.board.is_checkmate():
            print(self.board,'\n')
            if currentTurn == chess.WHITE:
                print('Your turn!\n\n')
                self._moveUser()
                currentTurn = chess.BLACK
            else:
                print('Computer move!\n\n')
                self._moveComputer()
                currentTurn = chess.WHITE
        print(self.board)
        if(currentTurn == chess.WHITE):
            print('\n\nComputer won! :( ')
        if(currentTurn == chess.BLACK):
            print('You won! :D ')

import chess

def evaluate(board: chess.Board):
    return -9999

def Negamax(board, depth):
    finalScore = float('-inf')

    if depth == 0:
        return evaluate(board)

    for move in board.legal_moves:
        board.push(move)
        nextScore = -Negamax(board, depth-1)
        board.pop()
        if finalScore > nextScore:
            finalScore = nextScore
    return finalScore 

class Game:
    def __init__(self, board: chess.Board, method):
        self.board = board
        self.basicDepth = 3
        self.method = method
    
    def _moveUser(self):
        print("Now is your turn! Your passible moves: ", self.board.legal_moves,'\n')
        move = input("Enter your move: ")
        self.board.push_san(move)
    
    def _moveComputer(self):
        bestMove = chess.Move.null
        bestScore = float('-inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            if self.method == 'negomax':
                score = Negamax(self.board, self.basicDepth)
            else:
                move = Negamax(self.board, self.basicDepth)
            self.board.pop()

            if score > bestScore:
                bestScore = score
                bestMove = move

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
        if(currentTurn == chess.BLACK):
            print('Computer won! :( ')
        if(currentTurn == chess.BLACK):
            print('You won! :D ')

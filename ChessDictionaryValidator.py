# ChessDictionaryValidator.py
print("Name:Tejaswini M",
       "AUID:1AY24AI111",
       "Section:O")
def is_valid_chess_board(board):
    valid_positions = [f"{file}{rank}" for file in 'abcdefgh' for rank in '12345678']
    valid_piece_names = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']

    white_pieces = 0
    black_pieces = 0
    white_pawns = 0
    black_pawns = 0

    for position, piece in board.items():
        if position not in valid_positions:
            return False

        if not (piece.startswith('w') or piece.startswith('b')):
            return False

        name = piece[1:]
        if name not in valid_piece_names:
            return False

        if piece.startswith('w'):
            white_pieces += 1
            if name == 'pawn':
                white_pawns += 1
        else:
            black_pieces += 1
            if name == 'pawn':
                black_pawns += 1

    if white_pieces > 16 or black_pieces > 16:
        return False
    if white_pawns > 8 or black_pawns > 8:
        return False

    return True
       
# Example use
board = {
    'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
    'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
    'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn',
    'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn',
    'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn',
    'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn',
    'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
    'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook',
}

print("Valid chess board." if is_valid_chess_board(board) else "Invalid chess board.")

   
           
   

def checkWinner(board):
	# Check for winner
	if(board[0] == board[1] and board[1] == board[2] and board[1] != ' '):
		return board[0]
	if(board[3] == board[4] and board[4] == board[5] and board[4] != ' '):
		return board[3]
	if(board[6] == board[7] and board[7] == board[8] and board[7] != ' '):
		return board[6]
	if(board[0] == board[3] and board[3] == board[6] and board[3] != ' '):
		return board[0]
	if(board[1] == board[4] and board[4] == board[7] and board[4] != ' '):
		return board[1]
	if(board[2] == board[5] and board[5] == board[8] and board[5] != ' '):
		return board[2]
	if(board[0] == board[4] and board[4] == board[8] and board[4] != ' '):
		return board[0]
	if(board[2] == board[4] and board[4] == board[6] and board[4] != ' '):
		return board[2]

	# Check that game hasn't finished
	for i in board:
		if i == ' ':
			return ''
	
	# If the board is full and there is no winner, it's a tie
	return ' '


def makeMove(board):
	pass
	# Return index of chosen move
	#Step 1: If there is a move that you can make to win, make it
	#Step 2 : If there is a move that you must make or otherwise the opponent will win, you have to make it (just a depth=1 check)
	#Step 3: Make a safer move - Place your piece either on the same row or a column or a diagonal of an opponent piece (that he can still win) so that you reduce a winning path of the opponent)


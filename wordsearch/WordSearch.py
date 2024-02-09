class WordSearch:
    def __init__(self):
        self.reserve_index = {}
        self.visited_twice = False
        self.character_not_existe = False


    def exist(self, board, word):
        m = len(board)
        word_length = len(word)

        for word_index in range (word_length - 1):
            for i in range(m):
                for j in range(len(board[i])):
                    previous = self.get_word_location(word, word_index, board, i, j)
                    current = self.get_word_location(word, word_index + 1, i, j)
                    if(self.check_neighbour(previous, current) or self.visited_twice):
                        return False
                    
        return True

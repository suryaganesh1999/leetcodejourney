class Solution:
    board = 0
    word = 0

    occupiedPositions = 0

    def isWordExists(self, i, j):
        self.occupiedPositions = set()
        for char in self.word[1:]:
            print(char, i, j)
            if not self.neighbourExists(i, j, char):
                return False
        return True


    def neighbourExists(self, i, j, next):
        # Consider Corners
        # Consider Occupied
        m = len(self.board)
        n = len(self.board[0])
        
        # Right
        if j+1<n and (i, j+1) not in self.occupiedPositions and self.board[i][j+1]==next:
            self.occupiedPositions.add((i, j+1))
            self.i = i
            self.j = j+1
            return True

        # Left
        if j-1>=0 and (i, j-1) not in self.occupiedPositions and self.board[i][j-1]==next:
            self.occupiedPositions.add((i, j-1))
            self.i = i
            self.j = j-1
            return True
        
        # Top
        if i-1>=0 and (i-1, j) not in self.occupiedPositions and self.board[i-1][j]==next:
            self.occupiedPositions.add((i-1, j))
            self.i = i-1
            self.j = j
            return True
        
        # Bottom
        if i+1<m and (i+1, j) not in self.occupiedPositions and self.board[i+1][j]==next:
            self.occupiedPositions.add((i+1, j))
            self.i = i+1
            self.j = j
            return True

        return False
            

    def exist(self, board: list[list[str]], word: str) -> bool:
        self.board = board
        self.word = word

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                # If first element match
                curr = board[i][j]
                if curr == word[0]:
                    print((i, j))
                    self.i = i
                    self.j = j
                    if self.isWordExists(i, j):
                        print(self.occupiedPositions)
                        return True
                    else:
                        print(self.occupiedPositions)
        return False
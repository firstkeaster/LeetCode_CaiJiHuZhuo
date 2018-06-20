class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.board = {}
        
    def l_col(self,r,c,i,n): #left counter r,c: row column i:player 
        if (r,c-1) not in self.board:
            return n
        if self.board[(r,c-1)] == i:
            return self.l_col(r,c-1,i,n+1)
        else:
            return n
    def r_col(self,r,c,i,n): #right counter
        if (r,c+1) not in self.board:
            return n
        if self.board[(r,c+1)] == i:
            return self.r_col(r,c+1,i,n+1)
        else:
            return n
    def u_col(self,r,c,i,n): #upper counter
        if (r-1,c) not in self.board:
            return n
        if self.board[(r-1,c)] == i:
            return self.u_col(r-1,c,i,n+1)
        else:
            return n
    def d_col(self,r,c,i,n): #down counter
        if (r+1,c) not in self.board:
            return n
        if self.board[(r+1,c)] == i:
            return self.d_col(r+1,c,i,n+1)
        else:
            return n
        
    def ul_col(self,r,c,i,n): #upperleft counter
        if (r-1,c-1) not in self.board:
            return n
        if self.board[(r-1,c-1)] == i:
            return self.ul_col(r-1,c-1,i,n+1)
        else:
            return n
    def ur_col(self,r,c,i,n): #upperright counter
        #print(self.board)
        if (r-1,c+1) not in self.board:
            return n
        if self.board[(r-1,c+1)] == i:
            return self.ur_col(r-1,c+1,i,n+1)
        else:
            return n
    def dl_col(self,r,c,i,n): #downleft counter
        #print(self.board)
        if (r+1,c-1) not in self.board:
            return n
        if self.board[(r+1,c-1)] == i:
            return self.dl_col(r+1,c-1,i,n+1)
        else:
            return n
    def dr_col(self,r,c,i,n): #downright counter
        if (r+1,c+1) not in self.board:
            return n
        if self.board[(r+1,c+1)] == i:
            return self.dr_col(r+1,c+1,i,n+1)
        else:
            return n
        
    def test_row(self,r,c,i):
        n = self.l_col(r,c,i,1)
        n = self.r_col(r,c,i,n)
        return n >= self.n
    def test_col(self,r,c,i):
        n = self.u_col(r,c,i,1)
        n = self.d_col(r,c,i,n)
        return n >= self.n
    def test_uldr(self,r,c,i):
        n = self.ul_col(r,c,i,1)
        n = self.dr_col(r,c,i,n)
        return n >= self.n
    def test_urdl(self,r,c,i):
        n = self.ur_col(r,c,i,1)
        n = self.dl_col(r,c,i,n)
        return n >= self.n
    
    def test_win(self,r,c,i):
        if self.test_row(r,c,i) or self.test_col(r,c,i) or self.test_uldr(r,c,i) or self.test_urdl(r,c,i):
            return i
        else:
            return 0
    
    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[(row,col)]=player
        return self.test_win(row,col,player)
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

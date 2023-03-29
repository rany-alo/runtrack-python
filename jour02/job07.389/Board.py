class Board:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.tableau = []
        
    def draw(self):
        for x in range(self.i):
            self.tableau.append(['O']*self.j)
        for y in self.tableau:
            print("|".join(y))        

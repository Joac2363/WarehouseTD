class Settings():
    def __init__(self):
        P = "P"
        B = "B"
        E = "E"
#----------------------------------------------------------
#                        Grid Level 1
#----------------------------------------------------------

        self.grids = [
            [
                [0, 0, 0, 0, P, P, P, P, P, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, P, 0, 0, 0, 0, P, P, E],
                [B, P, 0, 0, P, P, 0, 0, P, P, P, 0, P, P, 0, 0],
                [0, P, 0, 0, 0, P, 0, 0, 0, 0, P, 0, P, 0, 0, 0],
                [0, P, P, P, 0, P, 0, 0, 0, P, P, 0, P, 0, 0, 0],
                [0, 0, 0, P, 0, P, P, P, 0, P, 0, 0, P, P, P, 0],
                [0, P, P, P, 0, 0, 0, P, 0, P, P, P, 0, 0, P, 0],
                [0, P, 0, 0, 0, 0, 0, P, 0, 0, 0, P, 0, 0, P, 0],
                [0, P, P, P, P, P, 0, P, 0, 0, P, P, 0, 0, P, 0],
                [0, 0, 0, 0, 0, P, 0, P, 0, 0, P, 0, 0, 0, P, 0],
                [0, 0, 0, 0, 0, P, P, P, 0, 0, P, P, P, P, P, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ],
            [
                [B, P, P, P, P, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, P, P, P, P, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, P, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, P, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, P, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, P, P, E],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, P, P, P, P, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, P, P, P, P, P, P, P, P, P, E],
                [0, 0, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [B, P, P, P, P, 0, P, P, P, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, 0, 0, 0, 0, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, P, P, P, P, P, P, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [B, P, P, P, P, P, P, P, P, P, P, P, P, P, P, E],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],

        ]
        self.tile_dim = [80,80] #X,Y // Integer at or above 1
        self.path = []

        self.rounds = [
            [1],
            [1,1,1,1,1],
            [1,1,2,1,1],
            [2,2,2],
            [2,2,1,2,2],
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,2,2,1,1,1,1],
            [1,2,1,2,1,2,1,2,1,2],
            [2,2,2,2,2,2,2,2,2,2],
            [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]

        ]


#----------------------------------------------------------
#                        Pathfinder
#----------------------------------------------------------

class Path_finder:
    def __init__(self, grid):
        self.grid = grid
        self.y = len(grid)
        self.x = len(grid[0])
        self.path = []
    
    def find_path_start(self):
        temp = [None, None]
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                #First Path
                if self.grid[y][x] == "B":
                    temp = [x, y]
        return temp

    def validate(self, x, y): #Validates if a cell is valid for a path
        v = True
        if not 0 <= y < self.y:
            v = False  
        elif not 0 <= x < self.x:
            v = False
        
        elif self.grid[y][x] == "P" or self.grid[y][x] == "B" or self.grid[y][x] == "E":
            pass
        else:
            v = False
            
        return v
    
    def find_path(self, x, y):
        X = 0
        Y = 1
        #Basecase // If current pos is not valid return none
        if not self.validate(x, y) or [x, y] in self.path:
            return False

        
        self.path.append([x, y])
        #Check for end positon
        if self.grid[y][x] == "E":
            return True

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Check Sourrounding Squares
        for nx, ny in neighbors:
            if self.find_path(x + nx, y + ny):
                return True
        
        # This should only run if the above code doesn't find a path
        # The function should backtrack
        
        self.path.pop()
        return False
    
    
    
    def solve(self):
        start = self.find_path_start()
        if start != [None, None]:
            if self.find_path(start[0], start[1]):
                return self.path
        return None
    
d = Settings()
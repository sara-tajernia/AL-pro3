# AL-pro3
def scan(file_name):
    f = open(file_name, "r")
    coordination = f.readline()
    x, y = map(int, coordination.split())
    table = [[0 for i in range(y)] for j in range(x)]
    heuristic = [[0 for i in range(y)] for j in range(x)]
    for i in range (x):
        data = f.readline().split()
        for j in range(y):
            table[i][j] = data[j]
            heuristic[i][j] = [0, 1]
            if table[i][j] == '1':
                heuristic[i][j].remove(0)
            if table[i][j] == '0':
                heuristic[i][j].remove(1)
    print(table)
    return table, heuristic

class Game:
    def __init__(self, table, heuristic):
        self.table = table
        self.heuristic = heuristic
        self.dimension = len(table)
        self.terminal()
        print()
    def terminal(self):
        for i in range (self.dimension):
            for j in range(self.dimension):
                if len(heuristic[i][j]) == 1:
                    print(heuristic[i][j][0], end=' ')
                elif len(heuristic[i][j]) == 0:
                    print('\n❌ ERROR ❌')
                    exit(0)

                else:
                    print('-', end=' ')
            print()

    def domain(self):
        for i in range (self.dimension):
            for j in range (self.dimension):
                if heuristic[i][j] == [1]:
                    if j<self.dimension-1 and heuristic[i][j+1] == [1]:
                        if j>0 and 1 in heuristic[i][j-1]:
                            heuristic[i][j - 1].remove(1)
                        if j<self.dimension-2 and 1 in heuristic[i][j+2]:
                            heuristic[i][j + 2].remove(1)
                    if i<self.dimension-1 and heuristic[i+1][j] == [1]:
                        if i>0 and 1 in heuristic[i-1][j]:
                            heuristic[i - 1][j].remove(1)
                        if i<self.dimension-2 and 1 in heuristic[i+2][j]:
                            heuristic[i + 2][j].remove(1)
                elif heuristic[i][j] == [0]:
                    if j<self.dimension-1 and heuristic[i][j+1] == [0]:
                        if j>0 and 0 in heuristic[i][j-1]:
                            heuristic[i][j - 1].remove(0)
                        if j<self.dimension-2 and 0 in heuristic[i][j+2]:
                            heuristic[i][j + 2].remove(0)
                    if i<self.dimension-1 and heuristic[i+1][j] == [0]:
                        if i>0 and 0 in heuristic[i-1][j]:
                            heuristic[i -1][j].remove(0)
                        if i<self.dimension-2 and 0 in heuristic[i + 2][j]:
                            heuristic[i + 2][j].remove(0)
        self.terminal()
        print()

    def domain2(self):
        for i in range (self.dimension):
            num1 = num0 = 0
            for j in range (self.dimension):
                if heuristic[i][j] == [1]:
                    num1 += 1
                if heuristic[i][j] == [0]:
                    num0 += 1
            if num0 == self.dimension/2:
                for k in range (self.dimension):
                    if heuristic[i][k] == [0, 1]:
                        heuristic[i][k].remove(0)
            if num1 == self.dimension/2:
                for k in range (self.dimension):
                    if heuristic[i][k] == [0, 1]:
                        heuristic[i][k].remove(1)
        self.terminal()
        print()
        for j in range (self.dimension):
            num1 = num0 = 0
            for i in range (self.dimension):
                if heuristic[i][j] == [1]:
                    num1 += 1
                if heuristic[i][j] == [0]:
                    num0 += 1
            # print(num0, num1)
            if num0 == self.dimension/2:
                for k in range (self.dimension):
                    if heuristic[k][j] == [0, 1]:
                        heuristic[k][j].remove(0)
            if num1 == self.dimension/2:
                for k in range (self.dimension):
                    if heuristic[k][j] == [0, 1]:
                        heuristic[k][j].remove(1)
        self.terminal()
        print()

    def best_domain(self):
        self.domain()
        self.domain2()
        return heuristic


    # def MRV(self):




    def error(self):
        for i in range (self.dimension):
            for j in range (self.dimension):
                if not heuristic[i][j]:
                    print('\n❌ ERROR ❌')


def backup(heuristic):
    heuristic_backup = [[0 for i in range(len(heuristic))] for j in range(len(heuristic))]
    for i in range(len(heuristic)):
        for j in range(len(heuristic)):
            heuristic_backup[i][j] = heuristic[i][j].copy()
    return heuristic_backup


if __name__ == '__main__':
    file_name = 'puzzle1.txt'
    table, heuristic = scan(file_name)
    game = Game(table, heuristic)
    heuristic_backup = backup(heuristic)
    heuristic = game.best_domain()

    while heuristic_backup != heuristic:
        print(heuristic)
        print(heuristic_backup)
        heuristic_backup = backup(heuristic)
        heuristic = game.best_domain()

    game.error()

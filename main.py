def scan():
    f = open('puzzle0.txt', "r")
    coordination = f.readline()
    x, y = map(int, coordination.split())
    table = [[0 for i in range(y)] for j in range(x)]
    heuristic = [[0 for i in range(y)] for j in range(x)]
    for i in range(x):
        data = f.readline().split()
        for j in range(y):
            table[i][j] = data[j]
            heuristic[i][j] = [0, 1]
    print(table)
    return table, heuristic


class Game:
    def __init__(self, table, heuristic):
        self.table = table
        self.heuristic = heuristic
        self.dimension = len(table)

    def h(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if table[i][j] == '1':
                    heuristic[i][j] = [1]
                    if j < self.dimension - 1 and table[i][j + 1] == '1':
                        if j > 0 and 1 in heuristic[i][j - 1]:
                            heuristic[i][j - 1].remove(1)
                        if j < self.dimension - 2 and 1 in heuristic[i][j + 2]:
                            heuristic[i][j + 2].remove(1)
                    if i < self.dimension - 1 and table[i + 1][j] == '1':
                        if i > 0 and 1 in heuristic[i - 1][j]:
                            # print(i, j, heuristic[i][j])
                            heuristic[i - 1][j].remove(1)
                        if i < self.dimension - 2 and 1 in heuristic[i + 2][j]:
                            heuristic[i + 2][j].remove(1)
                elif table[i][j] == '0':
                    heuristic[i][j] = [0]
                    if j < self.dimension - 1 and table[i][j + 1] == '0':
                        if j > 0 and 0 in heuristic[i][j - 1]:
                            heuristic[i][j - 1].remove(0)
                        if j < self.dimension - 2 and 0 in heuristic[i][j + 2]:
                            heuristic[i][j + 2].remove(0)
                    if i < self.dimension - 1 and table[i + 1][j] == '0':
                        if i > 0 and '0' in heuristic[i - 1][j]:
                            heuristic[i - 1][j].remove(0)
                        if i < self.dimension - 2 and 0 in heuristic[i + 2][j]:
                            heuristic[i + 2][j].remove(0)
        print(heuristic)

    def MRV(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if len(self.heuristic[i][j]) == 1 and self.table[i][j] == '-':
                    table[i][j] = str(self.heuristic[i][j][0])
                    print(table[i][j], i, j)

    def error(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if not heuristic[i][j]:
                    print('❌ ERROR ❌')

    def complete(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if table[i][j] == '-':
                    return False
        return True

    def rules(self):
        for i in range(self.dimension):  # each row should have equal zeros and ones
            count_one = 0
            count_zero = 0
            for j in range(self.dimension):
                if table[i][j] == '1':
                    count_one += 1
                if table[i][j] == '0':
                    count_zero += 1
            if count_one != count_zero:
                return False
        for i in range(self.dimension):  # each column should have equal zeros and ones
            count_one = 0
            count_zero = 0
            for j in range(self.dimension):
                if table[j][i] == 1:
                    count_one += 1
                if table[j][i] == 0:
                    count_zero += 1
            if count_one != count_zero:
                return False
        '''
        for the rule that each row and column should have unique strings
        '''
        strings_row = []
        strings_column = []
        for i in range(self.dimension):  # all rows are copied in strings_row
            table_copy = table[i]
            table_copy = ''.join(table_copy)
            strings_row.append(table_copy)
        while len(strings_row) > 0:  # check if there is a repeated string in rows
            element = strings_row.pop(0)
            print(strings_row, "before")
            if '-' not in element and element in strings_row:
                strings_row = []
                print("tekrari")
                return False
        for j in range(self.dimension):  # all columns are copied in strings_column
            table_copy = [row[j] for row in table]
            table_copy = ''.join(table_copy)
            strings_column.append(table_copy)
        while len(strings_row) > 0:  # check if there is a repeated string in columns
            element = strings_row.pop(0)
            print(strings_row, "before")
            if '-' not in element and element in strings_row:
                strings_row = []
                print("tekrari")
                return False


if __name__ == '__main__':
    table, heuristic = scan()
    game = Game(table, heuristic)
    game.h()
    game.error()
    game.MRV()
    game.rules()

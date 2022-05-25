class Individual:

    def __init__(self, representation=None, size=None, replacement=True, valid_set=None):
        self.representation = representation
        self.size = 81
        self.replacement = replacement
        self.valid_set = valid_set


    def __repr__(self):

        board = ''

        for index, item in enumerate(self.representation):
            if index % 9 == 8:
                board += str(item) + '\n'
                if (index % 8 == 2) | (index % 8 == 5):
                    board += str('---------------------') + '\n'
            elif index % 3 == 2:
                board += str(item) + ' | '
            else:
                board += str(item) + ' '

        return board


    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def index(self, value):
        return self.representation.index(value)

    def check_row(self, row):
        lista = [self.__getitem__(i) for i in range(row, row+9)]
        if len(set(lista)) != 9:
            return False
        else:
            return True

    def check_col(self, col):
        lista = [self.__getitem__(i) for i in range(col, 72+col, 9)]
        if len(set(lista)) != 9:
            return False
        else:
            return True

    def check_box(self, box):
        lista = []
        for i in range(self.__len__()):
            if i % 9:
                lista.append(self.__getitem__(i))

        if len(set(lista)) != 9:
            return False
        else:
            return True


board = ''
lista = [0 for i in range(81)]
for index, item in enumerate(lista):
    if index % 9 == 8:
        board += str(item) + '\n'
        if (index % 8 == 2) | (index % 8 == 5):
            board += str('---------------------') + '\n'
    elif index % 3 == 2:
        board += str(item) + ' | '
    else:
        board += str(item) + ' '


a = Individual(lista)
print(a.check_box(0), a.check_col(0), a.check_row(0))
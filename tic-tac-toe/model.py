from events import eventBus

class Model:
    def __init__(self):
        self.coordinate = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
            (0, 4, 8), (2, 4, 6),  # D
        )
        self.fields = [''] * 9
        self.switch = True

    def click(self, coor):
        x, y = coor
        if x < 3 and y < 3 and self.fields[x*3+y] == '':
          self.fields[x*3+y] = 'X' if self.switch else 'O'
          self.switch = not self.switch
          eventBus.emit("switch", x, y, self.fields[x*3+y])

    def get_fields(self):
        return self.fields

    def restart(self):
        self.fields = [''] * 9
        self.switch = True
        eventBus.emit("restart")


    def tic_tac_toe(self):
        vector = lambda item: [self.fields[x] for x in item]
        for item in self.coordinate:
            if vector(item).count('X') == 3 or vector(item).count('O') == 3:
                self.fields[item[0]] = self.fields[item[0]].lower()
                self.fields[item[1]] = self.fields[item[2]].lower()
                self.fields[item[2]] = self.fields[item[1]].lower()
                eventBus.emit("win", item)
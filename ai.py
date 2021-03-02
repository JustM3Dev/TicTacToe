import random


class TicTacToeAI:
    def __init__(self, usr, ai, matrix, last_turn, main):
        self.usr = usr
        self.ai = ai
        self.matrix = matrix
        self.last_turn = last_turn
        self.temp = []
        self.main = main

    def random(self):
        temp = self.temp
        if temp == []:
            for u, entry in enumerate(self.matrix):
                for i, item in enumerate(entry):
                    if item == 0:
                        temp.append(str(u) + str(i))

        print(temp)
        choice = random.choice(temp)
        choice = str(choice)

        print(choice)
        print(choice[0], choice[1])
        if not self.main.field_used(int(choice[0]), int(choice[1])):
            self.temp = []
            self.main.update_table(int(choice[0]), int(choice[1]), self.ai)
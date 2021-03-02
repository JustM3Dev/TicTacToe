import sys
import datetime


class Menu:
    def __init__(self):
        self.items = [""]

    def set_items(self, items: dict):
        # { 'quit': test }
        if items == None:
            raise TypeError("The given argument has to be type of list")
        self.items = items

    def build(self):
        if self.items == None:
            raise TypeError("There has to be at least one menu item")

        msg = None
        msg = "+--------------------------+\n"

        for i, item in enumerate(self.items):
            # 26 - max amount
            # 5  - spaces that exist
            i += 1
            spaces = " " * ((26 - 6) - len(item))
            msg += f"|  [{i}] {item}{spaces}|\n"

        msg += "+--------------------------+"
        return msg

    def display(self):
        if self.items == None:

            return
        msg = self.build()
        print(msg)

    def pick(self):
        item = input("Action: ")
        item = int(item)

        if item > (len(self.items) + 1):
            print("You have to pick a valid item!\n")
            self.pick()
        else:
            items = list(self.items.values())
            items[item - 1]()


def sp():
    print("Singleplayer")


def mp():
    print("Multiplayer")

def omp():
    print("Connecting to our servers...")

def credits():
    print(f"(c) {datetime.datetime.now().year} Ilja Busch")


def source():
    print("https://github.com/JustM3Dev/TicTacToe/")


def quit():
    sys.exit()


menu = Menu()
menu.set_items(
    {
        "Singleplayer": sp,
        "Local Multiplayer": mp,
        "Online Multiplayer": omp,
        "Credits": credits,
        "Source": source,
        "Quit": quit,
    }
)
menu.display()
menu.pick()
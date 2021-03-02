from easy_table import EasyTable
import sys
import datetime
import re
from menu import *

try:
    from extensions import *

    extensions = True
except ImportError:
    extensions = False

try:
    from ai import *

    ai = True
except ImportError:
    ai = False

# Create the table and define the structure
table = EasyTable("Game")
table.setCorners("+", "+", "+", "+")
table.setOuterStructure("|", "-")
table.setInnerStructure("|", "-", "+")


class TicTacToe:
    def __init__(self):
        self.usr = 0
        self.ai = 0
        self.table = []
        self.table_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_turn = 0

    """ 
    Before game runs
    """

    def start(self, options: dict = None):
        if options == None:
            self.set_usr()
        elif options["multiplayer"] != None:
            if options["multiplayer"]["local"]:
                self.local_game()
            else:
                self.online_game()

    def set_usr(self):
        usr = input("\nWho do you want to be? (x/o)\n>>>")
        if usr in ["x", "o"]:
            usermap = {"x": 1, "o": 2}
            self.usr = usermap[usr]
            self.last_turn = self.usr
            if self.usr == 2:
                self.ai = 1
            else:
                self.ai = 2
            print(f"You are playing as {usr}!\n")
            self.tutorial()
        else:
            self.set_usr()

    def base_table(self):
        self.table = [
            {"  ": " A ", "1": "   ", "2": "   ", "3": "   "},
            {"  ": " B ", "1": "   ", "2": "   ", "3": "   "},
            {"  ": " C ", "1": "   ", "2": "   ", "3": "   "},
        ]
        table.setData(self.table)
        table.displayTable()

    """ 
    While game runs
    """

    def format_field(self, row, col):
        fieldmap = {0: "   ", 1: " x ", 2: " o "}
        return fieldmap[self.table_matrix[row][col]]

    def update_table(self, row, col, plr):
        matrix = self.table_matrix
        matrix[row][col] = plr

        self.table = [
            {
                "  ": " A ",
                "1": self.format_field(0, 0),
                "2": self.format_field(0, 1),
                "3": self.format_field(0, 2),
            },
            {
                "  ": " B ",
                "1": self.format_field(1, 0),
                "2": self.format_field(1, 1),
                "3": self.format_field(1, 2),
            },
            {
                "  ": " C ",
                "1": self.format_field(2, 0),
                "2": self.format_field(2, 1),
                "3": self.format_field(2, 2),
            },
        ]
        table.setData(self.table)
        table.displayTable()
        print("\n\n")
        self.game_state()

    def handle_input(self):
        field = input("Enter a field: ").upper()
        match = re.search("([A-C])([1-3])", field)
        if match:
            fieldmap = {"A": 0, "B": 1, "C": 2}
            row = fieldmap[match.group(1)]
            col = int(match.group(2)) - 1
            if not self.field_used(row, col):
                self.update_table(row, col, self.usr)
            else:
                print("Hm... That field is already being used. Pick another one!")
                self.handle_input()
        else:
            print("That field is invalid... Try again.")
            self.handle_input()

    def game_state(self):
        temp = [[0, 0, 0], [0, 0, 0]]

        for entry in self.table_matrix:
            n = entry.count(self.usr)
            u = entry.count(self.ai)
            if n >= 3:
                self.game_won(self.usr)
            elif u >= 3:
                self.game_won(self.ai)
        self.next_turn()

    def next_turn(self):
        if self.last_turn == self.usr:
            self.last_turn = self.ai
            self.game_ai()
        else:
            self.last_turn = self.usr
            self.handle_input()

    def field_used(self, row, col):
        if self.table_matrix[row][col] == [0, 0]:
            return True
        return False

    """ 
    After game
    """

    def game_won(self, plr):
        if plr == 1:
            plr = "x"
        else:
            plr = "o"
        ans = input(
            f"\nYoooo... '{plr}' just won that was a sick game! Wanna try again? (y/n)\n>>>"
        )
        if "y" in ans.lower():
            print("Ok! One second I gotta clean it all up for you!")
            self.cleanup()

    def cleanup(self):
        self.usr = 0
        self.table = []
        self.table_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.start()

    """ 
    TicTacToe Ai
    """

    def game_ai(self):
        ai = TicTacToeAI(self.usr, self.ai, self.table_matrix, self.last_turn, self)
        ai.random()

    """ 
    Tutorial 
    """

    def tutorial(self):
        if self.get_config_value("tutorial") == "True":
            print(
                f"You are playing as '{self.usr}' against a fairly simple AI. In order to win, you have to get three of your symbols in a row. You set a symbol by doing Letter + number. For example: A1 would put the symbol in the first row and first collumn. Have fun!\n"
            )

            with open("config.txt", "w") as file:
                file.write("tutorial=False")
        else:
            self.base_table()
            self.handle_input()

    def get_config_value(self, key: str):
        with open("config.txt", "r") as file:
            content = file.read()

        content = content.split("=")
        for i, item in enumerate(content):
            if item == key:
                return content[i + 1]


game = TicTacToe()


class MenuItems:
    def sp(self):
        game.start()

    def mp(self):
        if not extensions:
            print("You need to install the extension-pack in order to play online!")
            return
        print("Launching local multiplayer...")
        game.start({"multiplayer": {"local": True}})

    def omp(self):
        if not extensions:
            print("You need to install the extension-pack in order to play online!")
            return
        print("Connecting to our network...\n")
        print("This feature is currently unavailable")

    def credits(self):
        print(f"(c) {datetime.datetime.now().year} Ilja Busch")

    def source(self):
        print("https://github.com/JustM3Dev/TicTacToe/")

    def quit(self):
        sys.exit()

    def pick(self):
        def randomAI():
            game.start()

        def unavailable():
            print("This feature is not available yet.")

        def unavailable():
            print("This feature is not available yet.")

        menu = TicTacToeMenu()
        menu.set_items(
            {"Random AI": randomAI, "Fancy AI": unavailable, "Coming soon": unavailable}
        )
        menu.display()
        menu.pick()


try:
    if not ai:
        print(
            "The AI script could not be found. Please try installing it from the repo."
        )
    else:
        menu = TicTacToeMenu()
        items = MenuItems()
        menu.set_items(
            {
                "Against AI": items.pick,
                "Local Multiplayer": items.mp,
                "Online Multiplayer": items.omp,
                "Credits": items.credits,
                "Source": items.source,
                "Quit": items.quit,
            }
        )
        menu.display()
        menu.pick()
except KeyboardInterrupt:
    print("\n\nClosing...")
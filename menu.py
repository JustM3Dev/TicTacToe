class TicTacToeMenu:
    def __init__(self):
        self.items = [""]
        self.temp = 0

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
        i = self.temp
        item = input("Action: ")
        try:
            item = int(item)
        except ValueError:
            print(f"The given action has to be a number between 1 and {len(self.items)}\n")
            i += 1
            self.temp = i
            if i >= 3:
                i = 0
                self.temp = 0
                self.display()
                self.pick()
            else:
                self.pick()
            return

        if item > (len(self.items) + 1):
            print("You have to pick a valid item!\n")
            self.pick()
        else:
            items = list(self.items.values())
            items[item - 1]()
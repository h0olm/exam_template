from . import pickups

class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.score = 0

    def print_status(self, game_grid):
        """Visa spelvärlden och antal poäng."""
        print("--------------------------------------")
        print(f"You have {self.score} points.")
        print(game_grid)
        
    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        if grid.get(self.pos_x + x, self.pos_y + y) == "■":
            print("You hit a wall!")
            return False
        elif grid.get(self.pos_x + x, self.pos_y + y) != "■":
            return True

    def movePlayer(self, dx, dy, g, inventory):
        if self.can_move(dx, dy, g):
            maybe_item = g.get(self.pos_x + dx, self.pos_y + dy)
            self.move(dx, dy)
            self.score += -1

            if isinstance(maybe_item, pickups.Item):
                # we found something
                self.score += maybe_item.value
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                inventory.append(maybe_item)
                g.clear(self.pos_x, self.pos_y)



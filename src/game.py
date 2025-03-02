from .grid import Grid
from .player import Player
from . import pickups

player = Player(17, 5)
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
g.inner_walls()
pickups.randomize(g)

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    player.print_status(g)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]
    #if sats som kallar på moveplayer beroende på vilken input, skickar olika cords beroende på input
    if command == "d":
        player.movePlayer(1, 0, g, inventory)
    elif command == "a":
        player.movePlayer(-1, 0, g, inventory)
    elif command == "s":
        player.movePlayer(0, 1, g, inventory)
    elif command == "w":
        player.movePlayer(0, -1, g, inventory)
    elif command == "i":
           print(f"{' '.join(i.name for i in inventory)}")


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

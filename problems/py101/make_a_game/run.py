from lib.player import Player

if __name__ == "__main__":
    player = Player()
    player_name = input("Yo! What is your name? ")
    player.set_name(player_name)
    print(f"Welcome {player.name} to Pymon!")
    print("Type 'catch' to catch a Pymon!")
    print("Type 'Fight' to fight!")
    print("To stop playing, type quit")

    while player.in_game:
        message = input("What would you like me to repeat? (type quit to exit) ")
        if message == "quit":
            print("Roger that, thanks for playing!")
            player.in_game = False
        elif message == "catch":
            player.catch_pymon()
            print("You just caught a Pymon!")
        elif message == "fight":
            player.fight_baddie()
        elif message == "check":
            player.check_pymon() 
        else:
            print(player.repeat(message))

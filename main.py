from game import Game
from player import Player


def play():
    players = [Player(starting=True), Player(starting=False)]

    new_game = Game(len(players))
    new_game.setup()

    print("\t\t\t~~~ Initial state of the game ~~~")
    print(new_game)

    while there_isnt_a_winner(players):
        for index in range(len(players) + 1):
            if players[index].is_my_turn:
                players[index].is_my_turn = False
                players[index + 1].is_my_turn = True

                print(f"Player {index}'s turn.")

                players[index].take_turn(new_game)
    pass


def there_isnt_a_winner(players: list):
    for player in players:
        if player.is_winner():
            return False
    return True


if __name__ == '__main__':
    play()

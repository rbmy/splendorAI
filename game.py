from DevelopmentCard import DevelopmentCard
from nobleTile import nobleTile
import random

class Game:
    def __init__(self, number_of_players: int):
        self.number_of_players = number_of_players
        self.number_of_rounds = 0
        self.gems = {"emerald": 7, "sapphire": 7, "ruby": 7, "diamond": 7, "onyx": 7, "gold": 5}
        self.noble_tiles = [
            nobleTile(cost={"diamond": 4, "onyx": 4}, prestige_points=3),
            nobleTile(cost={"emerald": 3, "sapphire": 3, "ruby": 3}, prestige_points=3),
            nobleTile(cost={"emerald": 4, "sapphire": 4}, prestige_points=3),
            nobleTile(cost={"ruby": 4, "onyx": 4}, prestige_points=3),
            nobleTile(cost={"emerald": 4, "ruby": 4}, prestige_points=3),
            nobleTile(cost={"ruby": 3, "diamond": 3, "onyx": 3}, prestige_points=3),
            nobleTile(cost={"sapphire": 3, "diamond": 3, "onyx": 3}, prestige_points=3),
            nobleTile(cost={"emerald": 3, "ruby": 3, "onyx": 3}, prestige_points=3),
            nobleTile(cost={"emerald": 3, "sapphire": 3, "diamond": 3}, prestige_points=3),
            nobleTile(cost={"sapphire": 4, "diamond": 4}, prestige_points=3)
        ]
        self.development_card_decks = {
            "***": [
                DevelopmentCard(cost={"emerald": 3, "ruby": 6, "onyx": 3},
                                prestige_points=4, difficulty_level=3, bonus="onyx"),
                DevelopmentCard(cost={"diamond": 3, "sapphire": 6, "emerald": 3},
                                prestige_points=4, difficulty_level=3, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 3, "emerald": 3, "ruby": 3, "onyx": 5},
                                prestige_points=3, difficulty_level=3, bonus="sapphire"),
                DevelopmentCard(cost={"diamond": 5, "sapphire": 3, "ruby": 3, "onyx": 3},
                                prestige_points=3, difficulty_level=3, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 3, "onyx": 7},
                                prestige_points=5, difficulty_level=3, bonus="diamond"),
                DevelopmentCard(cost={"sapphire": 7, "emerald": 3},
                                prestige_points=5, difficulty_level=3, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 3, "sapphire": 3, "emerald": 5, "ruby": 3},
                                prestige_points=3, difficulty_level=3, bonus="onyx"),
                DevelopmentCard(cost={"sapphire": 3, "emerald": 6, "ruby": 3},
                                prestige_points=4, difficulty_level=3, bonus="ruby"),
                DevelopmentCard(cost={"ruby": 7},
                                prestige_points=4, difficulty_level=3, bonus="onyx"),
                DevelopmentCard(cost={"emerald": 7},
                                prestige_points=4, difficulty_level=3, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 7, "sapphire": 3},
                                prestige_points=5, difficulty_level=3, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 6, "sapphire": 3, "onyx": 3},
                                prestige_points=4, difficulty_level=3, bonus="sapphire"),
                DevelopmentCard(cost={"diamond": 3, "sapphire": 5, "emerald": 3, "onyx": 3},
                                prestige_points=3, difficulty_level=3, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 7},
                                prestige_points=4, difficulty_level=3, bonus="sapphire"),
                DevelopmentCard(cost={"sapphire": 7},
                                prestige_points=4, difficulty_level=3, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 3, "ruby": 3, "onyx": 6},
                                prestige_points=4, difficulty_level=3, bonus="diamond"),
                DevelopmentCard(cost={"sapphire": 3, "emerald": 3, "ruby": 5, "onyx": 3},
                                prestige_points=3, difficulty_level=3, bonus="diamond"),
                DevelopmentCard(cost={"ruby": 7, "onyx": 3},
                                prestige_points=5, difficulty_level=3, bonus="onyx"),
                DevelopmentCard(cost={"onyx": 7},
                                prestige_points=4, difficulty_level=3, bonus="diamond"),
                DevelopmentCard(cost={"emerald": 7, "ruby": 3},
                                prestige_points=5, difficulty_level=3, bonus="ruby")
            ],
            "**": [
                DevelopmentCard(cost={"onyx": 6},
                                prestige_points=3, difficulty_level=2, bonus="onyx"),
                DevelopmentCard(cost={"sapphire": 2, "emerald": 3, "onyx": 3},
                                prestige_points=1, difficulty_level=2, bonus="sapphire"),
                DevelopmentCard(cost={"diamond": 3, "onyx": 5},
                                prestige_points=2, difficulty_level=2, bonus="ruby"),
                DevelopmentCard(cost={"sapphire": 6},
                                prestige_points=3, difficulty_level=2, bonus="sapphire"),
                DevelopmentCard(cost={"sapphire": 5, "emerald": 3},
                                prestige_points=2, difficulty_level=2, bonus="emerald"),
                DevelopmentCard(cost={"emerald": 1, "ruby": 4, "onyx": 2},
                                prestige_points=2, difficulty_level=2, bonus="diamond"),
                DevelopmentCard(cost={"diamond": 3, "emerald": 3, "onyx": 2},
                                prestige_points=1, difficulty_level=2, bonus="onyx"),
                DevelopmentCard(cost={"ruby": 5, "onyx": 3},
                                prestige_points=2, difficulty_level=2, bonus="diamond"),
                DevelopmentCard(cost={"diamond": 2, "sapphire": 3, "ruby": 3},
                                prestige_points=1, difficulty_level=2, bonus="diamond"),
                DevelopmentCard(cost={"diamond": 5},
                                prestige_points=2, difficulty_level=2, bonus="onyx"),
                DevelopmentCard(cost={"sapphire": 2, "emerald": 2, "ruby": 3},
                                prestige_points=1, difficulty_level=2, bonus="sapphire"),
                DevelopmentCard(cost={"diamond": 6},
                                prestige_points=3, difficulty_level=2, bonus="diamond"),
                DevelopmentCard(cost={"sapphire": 3, "ruby": 2, "onyx": 3},
                                prestige_points=1, difficulty_level=2, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 4, "sapphire": 2, "onyx": 1},
                                prestige_points=2, difficulty_level=2, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 2, "sapphire": 3, "onyx": 2},
                                prestige_points=1, difficulty_level=2, bonus="emerald"),
                DevelopmentCard(cost={"onyx": 5},
                                prestige_points=2, difficulty_level=2, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 2, "ruby": 1, "onyx": 4},
                                prestige_points=2, difficulty_level=2, bonus="sapphire"),
                DevelopmentCard(cost={"sapphire": 5},
                                prestige_points=2, difficulty_level=2, bonus="sapphire"),
                DevelopmentCard(cost={"emerald": 5, "ruby": 3},
                                prestige_points=2, difficulty_level=2, bonus="onyx"),
                DevelopmentCard(cost={"diamond": 3, "emerald": 2, "ruby": 3},
                                prestige_points=1, difficulty_level=2, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 1, "sapphire": 4, "emerald": 2},
                                prestige_points=2, difficulty_level=2, bonus="ruby"),
                DevelopmentCard(cost={"ruby": 5},
                                prestige_points=2, difficulty_level=2, bonus="diamond"),
                DevelopmentCard(cost={"ruby": 6},
                                prestige_points=3, difficulty_level=2, bonus="ruby"),
                DevelopmentCard(cost={"emerald": 3, "ruby": 2, "onyx": 2},
                                prestige_points=1, difficulty_level=2, bonus="diamond"),
                DevelopmentCard(cost={"diamond": 5, "sapphire": 3},
                                prestige_points=2, difficulty_level=2, bonus="sapphire"),
                DevelopmentCard(cost={"emerald": 6},
                                prestige_points=3, difficulty_level=2, bonus="emerald"),
                DevelopmentCard(cost={"emerald": 5},
                                prestige_points=2, difficulty_level=2, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 2, "ruby": 2, "onyx": 3},
                                prestige_points=1, difficulty_level=2, bonus="ruby"),
                DevelopmentCard(cost={"sapphire": 1, "emerald": 4, "ruby": 2},
                                prestige_points=2, difficulty_level=2, bonus="onyx"),
                DevelopmentCard(cost={"diamond": 3, "sapphire": 2, "emerald": 2},
                                prestige_points=1, difficulty_level=2, bonus="onyx")
            ],
            "*": [
                DevelopmentCard(cost={"diamond": 2, "ruby": 2},
                                prestige_points=0, difficulty_level=1, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 1, "sapphire": 1, "emerald": 1, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 4},
                                prestige_points=1, difficulty_level=1, bonus="ruby"),
                DevelopmentCard(cost={"sapphire": 4},
                                prestige_points=1, difficulty_level=1, bonus="onyx"),
                DevelopmentCard(cost={"sapphire": 1, "ruby": 2, "onyx": 2},
                                prestige_points=0, difficulty_level=1, bonus="emerald"),
                DevelopmentCard(cost={"sapphire": 2, "ruby": 2},
                                prestige_points=0, difficulty_level=1, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 1, "onyx": 2},
                                prestige_points=0, difficulty_level=1, bonus="sapphire"),
                DevelopmentCard(cost={"diamond": 1, "emerald": 1, "ruby": 1, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="sapphire"),
                DevelopmentCard(cost={"emerald": 2, "onyx": 2},
                                prestige_points=0, difficulty_level=1, bonus="sapphire"),
                DevelopmentCard(cost={"sapphire": 2, "emerald": 1},
                                prestige_points=0, difficulty_level=1, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 1, "sapphire": 1, "ruby": 1, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 1, "emerald": 2, "ruby": 2},
                                prestige_points=0, difficulty_level=1, bonus="sapphire"),
                DevelopmentCard(cost={"diamond": 1, "sapphire": 2, "emerald": 1, "ruby": 1},
                                prestige_points=0, difficulty_level=1, bonus="onyx"),
                DevelopmentCard(cost={"sapphire": 2, "emerald": 2, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="diamond"),
                DevelopmentCard(cost={"sapphire": 1, "emerald": 3, "ruby": 1},
                                prestige_points=0, difficulty_level=1, bonus="sapphire"),
                DevelopmentCard(cost={"ruby": 4},
                                prestige_points=1, difficulty_level=1, bonus="sapphire"),
                DevelopmentCard(cost={"onyx": 3},
                                prestige_points=0, difficulty_level=1, bonus="sapphire"),
                DevelopmentCard(cost={"emerald": 4},
                                prestige_points=1, difficulty_level=1, bonus="diamond"),
                DevelopmentCard(cost={"sapphire": 3},
                                prestige_points=0, difficulty_level=1, bonus="diamond"),
                DevelopmentCard(cost={"ruby": 2, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="diamond"),
                DevelopmentCard(cost={"sapphire": 1, "emerald": 1, "ruby": 1, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="diamond"),
                DevelopmentCard(cost={"diamond": 2, "sapphire": 2, "ruby": 1},
                                prestige_points=0, difficulty_level=1, bonus="onyx"),
                DevelopmentCard(cost={"emerald": 1, "ruby": 3, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="onyx"),
                DevelopmentCard(cost={"emerald": 2, "ruby": 1},
                                prestige_points=0, difficulty_level=1, bonus="onyx"),
                DevelopmentCard(cost={"diamond": 2, "emerald": 2, "onyx": 2},
                                prestige_points=0, difficulty_level=1, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 3},
                                prestige_points=0, difficulty_level=1, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 2, "sapphire": 1},
                                prestige_points=0, difficulty_level=1, bonus="emerald"),
                DevelopmentCard(cost={"sapphire": 1, "emerald": 2, "ruby": 1, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="diamond"),
                DevelopmentCard(cost={"diamond": 1, "sapphire": 1, "ruby": 1, "onyx": 2},
                                prestige_points=0, difficulty_level=1, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 1, "sapphire": 3, "emerald": 1},
                                prestige_points=0, difficulty_level=1, bonus="emerald"),
                DevelopmentCard(cost={"diamond": 1, "ruby": 1, "onyx": 3},
                                prestige_points=0, difficulty_level=1, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 2, "sapphire": 1, "emerald": 1, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="ruby"),
                DevelopmentCard(cost={"diamond": 1, "emerald": 1, "ruby": 2, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="sapphire"),
                DevelopmentCard(cost={"diamond": 3, "sapphire": 1, "onyx": 1},
                                prestige_points=0, difficulty_level=1, bonus="diamond"),
                DevelopmentCard(cost={"diamond": 1, "sapphire": 1, "emerald": 1, "ruby": 1},
                                prestige_points=0, difficulty_level=1, bonus="onyx"),
                DevelopmentCard(cost={"sapphire": 2, "onyx": 2},
                                prestige_points=0, difficulty_level=1, bonus="diamond"),
                DevelopmentCard(cost={"emerald": 3},
                                prestige_points=0, difficulty_level=1, bonus="onyx"),
                DevelopmentCard(cost={"diamond": 2, "emerald": 2},
                                prestige_points=0, difficulty_level=1, bonus="onyx"),
                DevelopmentCard(cost={"ruby": 3},
                                prestige_points=1, difficulty_level=1, bonus="emerald"),
                DevelopmentCard(cost={"onyx": 4},
                                prestige_points=1, difficulty_level=1, bonus="emerald")
            ]
        }
        self.market = {"***": [], "**": [], "*": [], "nobles": []}

    def setup(self):
        random.shuffle(self.development_card_decks["*"])
        random.shuffle(self.development_card_decks["**"])
        random.shuffle(self.development_card_decks["***"])
        random.shuffle(self.noble_tiles)

        for x in range(5):
            self.market['***'].append(self.development_card_decks["***"].pop())
            self.market['**'].append(self.development_card_decks["**"].pop())
            self.market['*'].append(self.development_card_decks["*"].pop())

        for x in range(self.number_of_players + 1): 
            self.market["nobles"].append(self.noble_tiles.pop())



    def __str__(self):
        game_str = "Card count total: " + \
                   str(len(self.development_card_decks["***"]) + \
                       len(self.development_card_decks["**"]) + \
                       len(self.development_card_decks["*"])) + "\n" \
                   + "Card count '*': " + str(len(self.development_card_decks["*"])) + "\n" \
                   + "Card count '**': " + str(len(self.development_card_decks["**"])) + "\n" \
                   + "Card count '***': " + str(len(self.development_card_decks["***"])) + "\n" \
                   + f"Tokens: emerald = {self.gems['emerald']}; sapphire = {self.gems['sapphire']}; " \
                     f"ruby = {self.gems['ruby']}; diamond = {self.gems['diamond']}; " \
                     f"onyx = {self.gems['onyx']}; gold = {self.gems['gold']}" \
                    + f"\nnoble tiles = {len(self.noble_tiles)}" \
                    + f"\nnumber of players = {self.number_of_players}" \
                    + f"\nRound count = {self.number_of_rounds}" \
                    + f"\nCurrent Market = {self.market_as_string()}"
        return game_str

    def market_as_string(self):
        returned_string = "{"
        for difficulty_level in self.market:
            returned_string += f"\n{difficulty_level}:["
            for card in self.market[difficulty_level]:
                returned_string += f"\n\t{card},"
            returned_string += "\n]"
        return returned_string

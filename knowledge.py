from DevelopmentCard import DevelopmentCard


class Knowledge:

    def __init__(self):
        self.gem_colors = ["emerald", "sapphire", "ruby", "diamond", "onyx", "gold"]
        self.gems = {"emerald": 0, "sapphire": 0, "ruby": 0, "diamond": 0, "onyx": 0, "gold": 0}
        self.nobles = {}
        self.development_cards = {}

    def prestige_point_total(self):
        total = 0

        for card in self.development_cards:
            total += card.prestige_points

        return total

    def __str__(self):
        return f"\n\tGems = {self.gems}\n\tNobles = {self.nobles}\n\tDevelopment Cards = {self.development_cards}"

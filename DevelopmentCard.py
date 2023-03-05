class DevelopmentCard:
    def __init__(self, cost, prestige_points, bonus, difficulty_level):
        self.cost = cost
        self.prestige_points = prestige_points
        self.bonus = bonus
        self.difficulty_level = difficulty_level

    def __str__(self):
        return f"\n\tCost = {self.cost}\n\tPrestige points = {self.prestige_points}" \
               f"\n\tBonus = {self.bonus}\n\tDifficulty Level = {self.difficulty_level}"

class nobleTile:
    def __init__(self, cost, prestige_points):
        self.cost = cost
        self.prestige_points = prestige_points

    def __str__(self):
        return f"\n\tCost = {self.cost}\n\tPrestige Points = {self.prestige_points}"

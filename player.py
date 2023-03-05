from knowledge import Knowledge
from game import Game


class Player:

    def __init__(self, starting: bool):
        self.knowledge = Knowledge()
        self.is_my_turn = starting

    def is_winner(self) -> bool:
        return self.knowledge.prestige_point_total() == 15

    def take_turn(self, game:Game):
        ## take up to 3 gem tokens of different colors from the pool OR
        ## take up 2 gem tokens of the same color from the pool, given that there are at least 4 tokens left of that color OR
        ## take one gold gem token and reserve one development card, given total number of reserved cards held by that player does not exceed 3 OR
        ## Purchase a development card from the market or reserved cards by spending the required gem tokens or/and using the gem bonus of the cards purchased previously by the player

        ## THEN, if player has earned enough development card gems to trigger noble points bonus, take noble tile (one per turn)
        ## gem tokens can not be more than 10
        ## replenish the market

        pass

    def take_3_from_pool(self):
        pass

    def take_2_from_pool(self):
        pass

    def reserve_a_card(self):
        pass

    def purchase_a_card(self):
        pass

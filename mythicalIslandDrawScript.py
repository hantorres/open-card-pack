from mythicalIslandCards import *
from random import choices 
from queue import LifoQueue

class Mythical_Island:
    def __init__(self): # initialize draw stack
        pass 
    
    def pack_type(self):
        pack_types = ['Regular', 'Rare']
        weights = [99.95, 0.05]
        return choices(pack_types, weights=weights, k=1)[0]
    
    def regular(self):
        # Create card draw
        reg_draw = LifoQueue()

        # Card 5 rarity options + weights
        rarity5 = ['crown', 'triple_star', 'double_star', 'star', 'four_diamond', 'three_diamond', 'two_diamond']
        weights5 = [0.16, 0.888, 2, 10.288, 6.664, 20, 60]
        card5_type = choices(rarity5, weights=weights5, k=1)[0]
        card5 = choices(list(rarity_dicts[card5_type].keys()))[0]
        reg_draw.put(f'Card 5: {card5}. Rarity: {card5_type}')

        # Card 4 rarity options + weights
        rarity4 = ['crown', 'triple_star', 'double_star', 'star', 'four_diamond', 'three_diamond', 'two_diamond']
        weights4 = [0.04, 0.222, 0.5, 2.572, 1.666, 5, 90]
        card4_type = choices(rarity4, weights=weights4, k=1)[0]
        card4 = choices(list(rarity_dicts[card4_type].keys()))[0]
        reg_draw.put(f'Card 4: {card4}. Rarity: {card4_type}')

        # Card 1-3 options (they're all the same)
        n = 3 
        while n > 0:
            card = choices(list(diamond.keys()))[0]
            reg_draw.put(f'Card {n}: {card}. Rarity: diamond')
            n -= 1
        return reg_draw

    def reg_draw(self):
        return self.reg_draw.get()

    def rare(self):
        # Create card draw
        rare_draw = LifoQueue()

        # Card rarity options + weights
        rarity = ['crown', 'triple_star', 'double_star', 'star']
        weights = [5.556, 5.556, 55.555, 33.333]
        n = 5
        while n > 0:
            card_type = choices(rarity, weights=weights, k=1)[0]
            card = choices(list(rarity_dicts[card_type].keys()))[0]
            rare_draw.put(f'Card {n}: {card}. Rarity: {card_type}')
            n -= 1
        rare_draw.put("YOU GOT A RARE PACK LET'S FUCKING GO")
        return rare_draw
    
    def rare_draw(self):
        return self.rare_draw.get()
    
    def open_pack(self):
        type = self.pack_type()
        if type == 'Regular':
            return self.regular()
        else: return self.rare()

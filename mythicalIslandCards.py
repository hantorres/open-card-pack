# MYTHICAL ISLAND POKEMON CARDS BASED ON RARITY
# follows format Pokemon : card number
diamond = {
    "Exeggcute": 1,
    "Snivy": 4,
    "Morelull": 7,
    "Ponyta": 10,
    "Larvesta": 13,
    "Salandit": 15,
    "Magikarp": 17,
    "Finneon": 20,
    "Chewtle": 22,
    "Cramorant": 24,
    "Pikachu": 25,
    "Joltik": 28,
    "Dedenne": 30,
    "Elgyem": 34,
    "Flabébé": 36,
    "Floette": 37,
    "Swirlix": 39,
    "Mankey": 41,
    "Geodude": 43,
    "Koffing": 49,
    "Purrloin": 51,
    "Venipede": 53,
    "Pidgey": 57,
    "Pidgeotto": 58,
    "Eevee": 61,
    "Chatot": 62,
    "Old Amber": 63
}
two_diamond = {
    "Exeggutor": 2,
    "Servine": 5,
    "Shiinotic": 8,
    "Dhelmise": 9,
    "Rapidash": 11,
    "Magmar": 12,
    "Salazzle": 16,
    "Lumineon": 21,
    "Drednaw": 23,
    "Electabuzz": 27,
    "Galvantula": 29,
    "Sigilyph": 33,
    "Beheeyem": 35,
    "Florges": 38,
    "Primeape": 42,
    "Graveler": 44,
    "Stonjourner": 48,
    "Weezing": 50,
    "Liepard": 52,
    "Whirlipede": 54,
    "Scolipede": 55,
    "Druddigon": 56,
    "Pokemon Flute": 64,
    "Mythical Slab": 65,
    "Budding Expeditioner": 66,
    "Blue": 67,
    "Leaf": 68
}
three_diamond = {
    "Serperior": 6,
    "Volcarona": 14,
    "Vaporeon": 19,
    "Raichu": 26,
    "Mew": 31,
    "Slurpuff": 40,
    "Golem": 45,
    "Marshadow": 47,
    "Tauros": 60
}
four_diamond = {
    "Celebi EX": 3,
    "Gyarados EX": 18,
    "Mew EX": 32,
    "Aerodactyl EX": 46,
    "Pidgeot EX": 59
}
star = {
    "Exeggutor ★": 69,
    "Serperior ★": 70,
    "Salandit ★": 71,
    "Vaporeon ★": 72,
    "Dedenne ★": 73,
    "Marshadow ★": 74
}
double_star = {
    "Celebi EX ★★": 75,
    "Gyarados EX ★★": 76,
    "Mew EX ★★": 77,
    "Aerodactyl EX ★★": 78,
    "Pidgeot EX ★★": 79,
    "Budding Expeditioner ★★": 80,
    "Blue ★★": 81,
    "Leaf ★★": 82
}
triple_star = {
    "Mew EX ★★★": 83,
    "Aerodactyl EX ★★★": 84,
    "Celebi EX ★★★": 85
}
crown = {
    "Mew EX Crown": 86
}

# mapping of rarity string to dictionary
rarity_dicts = {
    'crown': crown,
    'triple_star': triple_star,
    'double_star': double_star,
    'star': star,
    'four_diamond': four_diamond,
    'three_diamond': three_diamond,
    'two_diamond': two_diamond
}

from pyautogui import position


slots = [
    {"field": position(1730, 885), "button": position(1730, 825)},
    {"field": position(1730, 775), "button": position(1730, 710)},
    {"field": position(1730, 665), "button": position(1730, 600)},
    {"field": position(1730, 550), "button": position(1730, 485)},
    {"field": position(1730, 440), "button": position(1730, 380)},
    {"field": position(1730, 330), "button": position(1730, 265)},
    {"field": position(1730, 220), "button": position(1730, 155)},
]

buttons_positions = {
    "compost": slots[0],
    "stone_to_tree": slots[2],
    "cloth": slots[2],
    "mhq": slots[4],
    "iron": slots[5],
    "corn": slots[3],
    "smoke": slots[0],
    "green_card": slots[2],
    "fish": slots[1],
}

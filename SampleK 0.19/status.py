
# SampleK Engine
# Player Status Module


def get_status_lines(hp, max_hp, score, items, player):

    lines = [
        f"HP: {hp}/{max_hp}",
        f"SCORE: {score}",
        f"ITEMS: {items}",
        f"POS: {player['x']}, {player['y']}"
    ]

    return lines


# SampleK Engine
# HUD Module

BOX_WIDTH = 48
INNER_WIDTH = BOX_WIDTH - 4


def write_line(row, content):
    print(f"\033[{row};1H\033[2K{content}", end="")


def draw_border(row):
    write_line(row, "+" + "-" * (BOX_WIDTH - 2) + "+")


def draw_box_line(row, content):
    content = str(content)[:INNER_WIDTH]
    write_line(row, f"| {content:<{INNER_WIDTH}} |")


def draw(map_height, sound_events, hp, max_hp,
         score, items, x, y):

    # SOUND CONSOLE
    sound_row = map_height + 2

    draw_border(sound_row)
    draw_box_line(sound_row + 1, "SOUND CONSOLE")

    recent_events = list(sound_events[-3:])

    while len(recent_events) < 3:
        recent_events.insert(0, "[SYS] Awaiting events")

    for index, event in enumerate(recent_events):
        draw_box_line(sound_row + 2 + index, event)

    draw_border(sound_row + 5)

    # PLAYER STATISTICS
    stats_row = sound_row + 6

    draw_border(stats_row)
    draw_box_line(stats_row + 1, "PLAYER STATISTICS")

    hearts = "♥ " * hp + "♡ " * max(0, max_hp - hp)

    draw_box_line(stats_row + 2, f"HP: {hearts}")
    draw_box_line(stats_row + 3, f"SCORE: {score:03} | ITEMS: {items:02}")
    draw_box_line(stats_row + 4, f"POSITION: X:{x:02} Y:{y:02}")
    draw_box_line(stats_row + 5, "WASD: mover | Q: sair")

    draw_border(stats_row + 6)

    print("", end="", flush=True)

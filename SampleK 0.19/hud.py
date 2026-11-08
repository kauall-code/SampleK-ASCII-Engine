
# SampleK Engine
# HUD Module

BOX_WIDTH = 48
INNER_WIDTH = BOX_WIDTH - 4


def write_line(row, content):
    print(f"\033[{row};43H\033[0K{content}", end="")


def draw_border(row):
    write_line(row, "+" + "-" * (BOX_WIDTH - 2) + "+")


def draw_box_line(row, content):
    content = str(content)[:INNER_WIDTH]
    write_line(row, f"| {content:<{INNER_WIDTH}} |")


def draw(map_height, sound_events, narrator_events):

    # SOUND CONSOLE
    sound_row = 1

    draw_border(sound_row)
    draw_box_line(sound_row + 1, "SOUND CONSOLE")

    recent_events = list(sound_events[-3:])

    while len(recent_events) < 3:
        recent_events.insert(0, "[SYS] Awaiting events")

    for index, event in enumerate(recent_events):
        draw_box_line(sound_row + 2 + index, event)

    draw_border(sound_row + 5)

    # EVENT NARRATOR
    narrator_row = sound_row + 6

    draw_border(narrator_row)
    draw_box_line(narrator_row + 1, "EVENT NARRATOR")

    # Espaço disponível até o final do mapa
    available_lines = map_height - narrator_row - 2

    recent_messages = list(narrator_events[-available_lines:])

    while len(recent_messages) < available_lines:
        recent_messages.insert(0, "...")

    for index, message in enumerate(recent_messages):
        draw_box_line(narrator_row + 2 + index, message)

    draw_border(map_height)

    print("", end="", flush=True)

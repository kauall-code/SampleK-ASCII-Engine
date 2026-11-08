
# SampleK Engine
# Menu Module

MASCOT = "-[:)]-"
CONTROLS = "CONTROLES: WASD, E, Q"


def create_menu(options):

    return {
        "options": options,
        "cursor": 0
    }


def move_cursor(menu, direction):

    if not menu["options"]:
        return

    menu["cursor"] += direction

    # Impede ultrapassar os limites
    if menu["cursor"] < 0:
        menu["cursor"] = 0

    if menu["cursor"] >= len(menu["options"]):
        menu["cursor"] = len(menu["options"]) - 1


def get_selected(menu):

    if not menu["options"]:
        return None

    return menu["options"][menu["cursor"]]


def draw_window(
    frame,
    title,
    lines,
    width=32,
    height=12,
    cursor=None,
    mascot=True,
    controls=CONTROLS
):

    output = [row.copy() for row in frame]

    world_height = len(output)
    world_width = len(output[0])

    start_x = (world_width - width) // 2
    start_y = (world_height - height) // 2

    bottom = start_y + height - 1
    right = start_x + width - 1

    # Fundo e bordas
    for y in range(start_y, bottom + 1):
        for x in range(start_x, right + 1):

            if y == start_y or y == bottom:
                output[y][x] = "-"
            elif x == start_x or x == right:
                output[y][x] = "|"
            else:
                output[y][x] = " "

    # Cantos
    output[start_y][start_x] = "+"
    output[start_y][right] = "+"
    output[bottom][start_x] = "+"
    output[bottom][right] = "+"

    # Título
    title = title[:width - 4]

    for index, char in enumerate(title):
        output[start_y + 1][start_x + 2 + index] = char

    # Conteúdo
    for index, line in enumerate(lines):

        if index + 4 >= height:
            break

        line = str(line)

        if cursor == index:
            line = "> " + line
        else:
            line = "  " + line

        line = line[:width - 4]

        for char_index, char in enumerate(line):
            output[start_y + 2 + index][start_x + 2 + char_index] = char

    # Rodapé: controles
    if controls:

        controls = controls[:width - 4]
        controls_y = bottom - 1
        controls_x = start_x + 2

        for index, char in enumerate(controls):
            output[controls_y][controls_x + index] = char

    # Perninha
    if mascot:

        mascot_x = right - len(MASCOT) - 1
        mascot_y = bottom - 1

        for index, char in enumerate(MASCOT):
            output[mascot_y][mascot_x + index] = char

    return output

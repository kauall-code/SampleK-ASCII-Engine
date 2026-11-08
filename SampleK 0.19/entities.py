
# SampleK Engine
# Entity Module


def create_entity(x, y, symbol, item_id=None, item_name=None):
    return {
        "x": x,
        "y": y,
        "symbol": symbol,
        "item_id": item_id,
        "item_name": item_name
    }



def entity_at(entity_list, x, y, ignore=None):
    for entity in entity_list:

        if entity is ignore:
            continue

        if entity["x"] == x and entity["y"] == y:
            return entity

    return None


def compose(world_grid, entity_list):

    # Cria uma cópia do mundo
    frame = [row.copy() for row in world_grid]

    # Desenha as entidades sobre o mundo
    for entity in entity_list:

        x = entity["x"]
        y = entity["y"]

        if 0 <= y < len(frame) and 0 <= x < len(frame[y]):

            if frame[y][x] != "#":
                frame[y][x] = entity["symbol"]

    return frame

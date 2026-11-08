
# SampleK Engine
# Entity System Test

import world
import entities

grid = world.load_map()

entity_list = [
    entities.create_entity(2, 2, "@"),
    entities.create_entity(3, 5, "$"),
    entities.create_entity(10, 7, "E")
]

frame = entities.compose(grid, entity_list)

print("=== WORLD + ENTITIES ===")

for row in frame:
    print("".join(row))

print("\n=== ORIGINAL WORLD ===")

for row in grid:
    print("".join(row))

print("\n=== ENTITY TEST ===")

found = entities.entity_at(entity_list, 2, 2)
print(found)


# SampleK Engine
# Version 0.19

import status
import renderer
import world
import entities
import input_handler
import hud
import time
import inventory
import narrator
import menu


def main():

    # Carrega o mundo
    world_grid = world.load_map()

    height = len(world_grid)
    width = len(world_grid[0])

    # Entidades
    player = entities.create_entity(1, 1, "Π")

    coin = entities.create_entity(
        3, 5, "$",
        item_id="coin",
        item_name="Moeda"
    )

    enemy = entities.create_entity(10, 7, "E")

    entity_list = [player, coin, enemy]

    # Sistemas
    bag = inventory.create_inventory()
    event_log = narrator.create_narrator()

    hp = 3
    max_hp = 3
    score = 0

    # Menu principal
    main_menu = menu.create_menu([
        "INVENTARIO",
        "STATUS",
        "CONFIGURACOES",
        "HABILIDADES"
    ])

    menu_state = "closed"
    submenu_title = ""

    sound_events = ["[SYS] SampleK initialized"]

    # Aguarda a tecla inicial ser solta
    while input_handler.get_key() is not None:
        pass

    print("\033[2J\033[H", end="", flush=True)

    while True:

        key = input_handler.get_key()

        if key is not None:

            # =================================
            # JOGO NORMAL
            # =================================

            if menu_state == "closed":

                if key in (b'e', b'E'):

                    menu_state = "main"
                    main_menu["cursor"] = 0

                elif key in (b'q', b'Q'):

                    break

                else:

                    new_x = player["x"]
                    new_y = player["y"]

                    if key in (b'w', b'W'):
                        new_y -= 1

                    elif key in (b's', b'S'):
                        new_y += 1

                    elif key in (b'a', b'A'):
                        new_x -= 1

                    elif key in (b'd', b'D'):
                        new_x += 1

                    if 0 <= new_x < width and 0 <= new_y < height:

                        if world_grid[new_y][new_x] != "#":

                            target = entities.entity_at(
                                entity_list,
                                new_x,
                                new_y,
                                ignore=player
                            )

                            if target is None or target.get("item_id") is not None:

                                player["x"] = new_x
                                player["y"] = new_y

                                if target is not None:

                                    inventory.add_item(
                                        bag,
                                        target["item_id"],
                                        target["item_name"]
                                    )

                                    entity_list.remove(target)

                                    sound_events.append(
                                        "[SFX] Item collected"
                                    )

                                    narrator.add_event(
                                        event_log,
                                        "item_collected"
                                    )

                                else:

                                    sound_events.append(
                                        "[SFX] Footstep"
                                    )

                                sound_events = sound_events[-3:]

            # =================================
            # MENU PRINCIPAL
            # =================================

            elif menu_state == "main":

                if key in (b'w', b'W'):

                    menu.move_cursor(main_menu, -1)

                elif key in (b's', b'S'):

                    menu.move_cursor(main_menu, 1)

                elif key in (b'q', b'Q'):

                    menu_state = "closed"

                elif key in (b'e', b'E'):

                    selected = menu.get_selected(main_menu)

                    if selected == "INVENTARIO":

                        menu_state = "inventory"

                    elif selected == "STATUS":

                        menu_state = "status"

                    elif selected == "CONFIGURACOES":

                        menu_state = "placeholder"
                        submenu_title = "CONFIGURACOES"

                    elif selected == "HABILIDADES":

                        menu_state = "placeholder"
                        submenu_title = "HABILIDADES"

            # =================================
            # TELAS INTERNAS
            # =================================

            else:

                if key in (b'q', b'Q'):

                    menu_state = "main"

        # =================================
        # DESENHO DO MUNDO
        # =================================

        frame = entities.compose(world_grid, entity_list)

        # =================================
        # DESENHO DO MENU
        # =================================

        if menu_state == "main":

            frame = menu.draw_window(
                frame,
                "MENU PRINCIPAL",
                main_menu["options"],
                cursor=main_menu["cursor"]
            )

        elif menu_state == "inventory":

            inventory_lines = ["ITENS"]

            if bag:

                for item in bag:
                    inventory_lines.append(
                        f"- {item['name']}"
                    )

            else:

                inventory_lines.append("- Vazio")

            frame = menu.draw_window(
                frame,
                "INVENTARIO",
                inventory_lines
            )

        elif menu_state == "status":

            item_count = len(bag)

            status_lines = status.get_status_lines(
                hp,
                max_hp,
                score,
                item_count,
                player
            )

            frame = menu.draw_window(
                frame,
                "STATUS",
                status_lines
            )

        elif menu_state == "placeholder":

            frame = menu.draw_window(
                frame,
                submenu_title,
                ["EM DESENVOLVIMENTO"]
            )

        # Renderização
        renderer.render(frame)

        hud.draw(
            height,
            sound_events,
            narrator.get_events(event_log)
        )

        time.sleep(0.05)


if __name__ == "__main__":
    main()


# SampleK Engine
# Render Module

def render(grid):
    for y, row in enumerate(grid):
        print(
            f"\033[{y + 1};1H\033[2K{''.join(row)}",
            end=""
        )

    print("", end="", flush=True)

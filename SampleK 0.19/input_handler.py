
# SampleK Engine
# Input Module

import msvcrt

def get_key():
    if not msvcrt.kbhit():
        return None

    key = msvcrt.getch().lower()

    # Ignora teclas especiais do Windows
    if key in (b'\x00', b'\xe0'):
        msvcrt.getch()
        return None

    return key

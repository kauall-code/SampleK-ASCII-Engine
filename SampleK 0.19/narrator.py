
# SampleK Engine
# Event Narrator Module

def create_narrator():
    return []


def describe_event(event):

    messages = {
        "item_collected": "Você encontrou uma Moeda!",
        "player_moved": "Você caminhou pelo mundo.",
        "enemy_blocked": "Algo está bloqueando seu caminho."
    }

    return messages.get(event, "Algo aconteceu...")


def add_event(narrator, event):

    message = describe_event(event)

    narrator.append(message)

    # Mantém apenas os últimos eventos
    narrator[:] = narrator[-5:]


def get_events(narrator):
    return narrator.copy()

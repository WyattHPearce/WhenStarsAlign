# Standard Imports
# Third-Party Imports
# Local Imports

current_state: str = None

def get_state() -> str:
    return current_state

def set_state(state: str) -> None:
    global current_state
    current_state = state
from enum import IntEnum

class Screen(IntEnum):
    STARTUP_SCREEN = 0
    ARCADE_FLOOR = 1

class GameState:
  def __init__(self):
      self.current_screen = Screen.STARTUP_SCREEN


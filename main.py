import pyray as pr
import gamestate

import startupscreen
import arcadefloor

state = gamestate.GameState()

pr.init_window(1024, 640, "GIB")

ss = startupscreen.StartupScreen(state) # texture initialization needs to be done w/ opengl context
af = arcadefloor.ArcadeFloor(state)
screens = [ss, af]
pr.set_target_fps(60)

state.current_screen = gamestate.Screen.STARTUP_SCREEN

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    screens[int(state.current_screen)].draw_frame()
    pr.end_drawing()
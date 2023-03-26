import pyray as pr
import utils
import gamestate

class StartupScreen:
  def __init__(self, game_state):
      self.current_total_time = 0.0
      self.game_state = game_state
      self.playbuttonimg = pr.load_image("assets/playbutton.png")
      self.playbuttontexture = pr.load_texture_from_image(self.playbuttonimg)
      self.playbuttonbounds = pr.Rectangle(1024/2 - self.playbuttontexture.width / 2, 640/2 + 200 - self.playbuttontexture.height/2, self.playbuttontexture.width, self.playbuttontexture.height)


  def draw_frame(self):
      self.current_total_time += pr.get_frame_time()
      if self.current_total_time > 5.7:
          pr.draw_texture(self.playbuttontexture, int(1024/2 - self.playbuttontexture.width / 2), int(640/2) + 200, pr.RAYWHITE)
          if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT):
            self.game_state.current_screen = gamestate.Screen.ARCADE_FLOOR
      if self.current_total_time > 4.7:
          utils.draw_text_centered("THE GAME!!!!!!!!!!", 1024 / 2 + 220, 640 / 1.8, 22, pr.RED)
      if self.current_total_time > 4.0:
          utils.draw_text_centered("gambling is bad", 1024 / 2, 640 / 3, 80, pr.YELLOW)
      elif self.current_total_time > 2.0:
          utils.draw_text_centered("Hello there, and welcome to...", 1024 / 2, 640 / 2, 24, pr.BLACK)
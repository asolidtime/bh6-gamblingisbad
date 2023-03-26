import pyray as pr

def draw_text_centered(text, x, y, size, color):
    pr.draw_text(text, int(x - pr.measure_text(text, size) / 2), int(y), size, color)

def draw_text_really_centered(text, x, y, size, color):
    pr.draw_text(text, int(x - pr.measure_text(text, size) / 2), int(y - size/2), size, color)
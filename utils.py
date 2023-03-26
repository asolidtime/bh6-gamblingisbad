import pyray as pr

def draw_text_centered(text, x, y, size, color):
    pr.draw_text(text, int(x - pr.measure_text(text, size) / 2), int(y), size, color)

def draw_text_really_centered(text, x, y, size, color):
    pr.draw_text(text, int(x - pr.measure_text(text, size) / 2), int(y - size/2), size, color)
    
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

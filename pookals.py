import turtle as T
import time

# --- Customizable Settings ---
CONFIG = {"bg": "#f3f3f3", "size": 900}

# Color palettes
PALETTE_1 = {
    "orange": "#e97512", "maroon": "#e97512",
    "green": "#1d6e3a", "darkgreen": "#1d6e3a",
    "yellow": "#f6bd20", "gold": "#d4af37",
}
PALETTE_2 = {
    "orange": "#3498DB", "maroon": "#3498DB",
    "green": "#FFC300", "darkgreen": "#FFC300",
    "yellow": "#FF5733", "gold": "#900C3F",
}
PALETTE_3 = {
    "orange": "#00BFA5", "maroon": "#00BFA5",
    "green": "#D4E157", "darkgreen": "#D4E157",
    "yellow": "#FFD54F", "gold": "#FFC107",
}
PALETTE_4 = {
    "orange": "#D32F2F", "maroon": "#D32F2F",
    "green": "#9c27B0", "darkgreen": "#9C27B0",
    "yellow": "#4DD0E1", "gold": "#00ACC1",
}

COLOR_PALETTES = [PALETTE_1, PALETTE_2, PALETTE_3, PALETTE_4]
current_palette = COLOR_PALETTES[0]

# Pattern mode → 0 = round, 1 = lotus, 2 = star
pattern_mode = 0  

pen = T.Turtle(visible=False)
pen.speed(0)

# ---------------- SETUP ---------------- #
def setup():
    T.setup(CONFIG["size"], CONFIG["size"])
    T.bgcolor(CONFIG["bg"])
    T.title("Pookalam – Press A/B/C/D for colors, P for patterns, O/T for surprises, R to reset")
    T.tracer(0, 0)

# ---------------- PARTS ---------------- #
def radial(draw_fn, count, start_angle=0):
    step = 360 / count
    for i in range(count):
        pen.penup(); pen.home(); pen.setheading(start_angle + i*step)
        draw_fn()

# Petal variations
def petal_round():
    r = 180
    pen.forward(r)
    pen.pendown()
    pen.fillcolor(current_palette["orange"])
    pen.pencolor(current_palette["maroon"])
    pen.begin_fill()
    pen.left(60); pen.circle(80, 120)
    pen.left(120); pen.circle(80, 120)
    pen.end_fill()
    pen.penup(); pen.backward(r)

def petal_lotus():
    r = 180
    pen.forward(r)
    pen.pendown()
    pen.fillcolor(current_palette["orange"])
    pen.pencolor(current_palette["maroon"])
    pen.begin_fill()
    for _ in range(2):
        pen.left(60)
        pen.circle(80, 60)
        pen.left(60)
    pen.end_fill()
    pen.penup(); pen.backward(r)

def petal_star():
    r = 180
    pen.forward(r)
    pen.pendown()
    pen.fillcolor(current_palette["orange"])
    pen.pencolor(current_palette["maroon"])
    pen.begin_fill()
    for _ in range(5):
        pen.forward(60)
        pen.right(144)
    pen.end_fill()
    pen.penup(); pen.backward(r)

def petals():
    if pattern_mode == 0: radial(petal_round, 12)
    elif pattern_mode == 1: radial(petal_lotus, 12)
    else: radial(petal_star, 12)

def leaves():
    r = 260
    def leaf():
        pen.forward(r)
        pen.pendown()
        pen.fillcolor(current_palette["green"])
        pen.pencolor(current_palette["darkgreen"])
        pen.begin_fill()
        pen.left(60); pen.circle(100, 120)
        pen.left(120); pen.circle(100, 120)
        pen.end_fill()
        pen.penup(); pen.backward(r)
    radial(leaf, 8)

def inner_petals():
    r = 100
    def small_petal():
        pen.forward(r)
        pen.pendown()
        pen.fillcolor(current_palette["yellow"])
        pen.pencolor(current_palette["maroon"])
        pen.begin_fill()
        pen.left(60); pen.circle(50, 120)
        pen.left(120); pen.circle(50, 120)
        pen.end_fill()
        pen.penup(); pen.backward(r)
    radial(small_petal, 12)

def rim_only():
    pen.penup(); pen.goto(100, -375)
    pen.pendown()
    pen.pencolor(current_palette["gold"])
    pen.pensize(14)
    pen.circle(380)

def happy_onam_text():
    pen.penup(); pen.goto(0, -420)
    pen.pendown()
    pen.color(current_palette["maroon"])
    pen.write("Happy Onam", align="center", font=("Arial", 28, "bold"))

def status_label():
    """Show current palette & pattern at top."""
    names = ["Round", "Lotus", "Star"]
    idx = COLOR_PALETTES.index(current_palette) + 1
    pen.penup(); pen.goto(0, 400)
    pen.color("black")
    pen.write(f"Palette {idx} | Pattern: {names[pattern_mode]}", 
              align="center", font=("Arial", 16, "bold"))

# ---------------- MAIN DRAWING FUNCTION ---------------- #
def draw_pookalam():
    pen.clear()
    inner_petals()
    petals()
    leaves()
    rim_only()
    happy_onam_text()
    status_label()
    T.update()

# ---------------- FESTIVAL SURPRISE ---------------- #
def draw_lotus_icon():
    """Draw a simple lotus-like icon at center (simulating Onam symbol)."""
    pen.penup(); pen.home()
    pen.pendown()
    pen.fillcolor(current_palette["yellow"])
    pen.pencolor(current_palette["maroon"])
    pen.begin_fill()
    for _ in range(12):
        pen.forward(60)
        pen.left(150)
        pen.forward(60)
        pen.left(30)
    pen.end_fill()
    T.update()

def text_animation():
    """Animate text 'Happy Onam 2025 🌸' letter by letter."""
    message = "Happy Onam 2025 🌸"
    pen.penup(); pen.goto(0, 0)
    pen.color(current_palette["maroon"])
    pen.pendown()
    for i in range(len(message)):
        pen.write(message[i], align="center", font=("Arial", 26, "bold"))
        time.sleep(0.2)
        pen.penup(); pen.forward(20); pen.pendown()
    T.update()

# ---------------- INTERACTIVE FUNCTION ---------------- #
def set_palette(index):
    global current_palette
    current_palette = COLOR_PALETTES[index]
    draw_pookalam()

def reset_pookalam():
    global pattern_mode
    pattern_mode = 0
    set_palette(0)

def change_pattern():
    global pattern_mode
    pattern_mode = (pattern_mode + 1) % 3
    draw_pookalam()

# ---------------- PROGRAM EXECUTION ---------------- #
if __name__ == "__main__":
    setup(); draw_pookalam()

    T.listen()
    for key, idx in zip("abcd", range(4)):
        T.onkey(lambda i=idx: set_palette(i), key)
        T.onkey(lambda i=idx: set_palette(i), key.upper())
    T.onkey(reset_pookalam, 'r'); T.onkey(reset_pookalam, 'R')
    T.onkey(change_pattern, 'p'); T.onkey(change_pattern, 'P')
    T.onkey(draw_lotus_icon, 'o'); T.onkey(draw_lotus_icon, 'O')
    T.onkey(text_animation, 't'); T.onkey(text_animation, 'T')

    T.mainloop()  # keep window open

#=============RENDER METHOD INSTEAD OF USING NORMAL PRINT FUNCTION========================
def draw_text(stdscr, y, x, text):
    h, w = stdscr.getmaxyx()
    if y < 0 or y >= h:
        return
    if x < 0 or x >= w:
        return
    text = text[: w - x - 1]       
    stdscr.addstr(y, x, text)

def draw_lines(stdscr, y, x, lines):
    for i in range(len(lines)):
        draw_text(stdscr, y + i, x, lines[i])

def draw_box(stdscr, y, x, h, w):
    draw_text(stdscr, y, x, "+" + "-" * (w - 2) + "+")
    for i in range(1, h - 1):
        draw_text(stdscr, y + i, x, "|")
        draw_text(stdscr, y + i, x + w - 1, "|")
    draw_text(stdscr, y + h - 1, x, "+" + "-" * (w - 2) + "+")
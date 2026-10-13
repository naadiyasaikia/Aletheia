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
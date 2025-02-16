from pygame import *


window_width = 700
window_height = 500
display.set_caption("Лабіринт")
window = display.set_mode((window_width, window_height))

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
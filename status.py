import os
import curses
import time

stdscr = curses.initscr()



slashes = ["/","-","\\","|"]

timing = 0.1
value = 1


while True:
    message = "#"*value
    for i in range(0,3):
        stdscr.erase()
        stdscr.refresh()
        stdscr.addstr("["+slashes[i]+"]"+message+"-"+str(value)+"%")
        stdscr.refresh()
        time.sleep(timing)
    value = value + 1
    if value>100:
        break
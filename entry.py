import curses
import time
print("\nInitializing mierda checker v0.1.34-13-12-2022...")
time.sleep(2)

names = [
    "John",
    "Mao",
    "Voldemar"
]

if __name__ == "__main__":
    stdscr = curses.initscr()
    stdscr.addstr("g")
    stdscr.refresh()
    from main import main
    main(names,"jabroni","not jabroni")

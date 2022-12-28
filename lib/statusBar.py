import curses


class statusBar:
    value = 0
    slashes = ["/","-","\\","|"]
    state = 0
    stdscr = None
    def __init__(self,start,end) -> None:
        self.start = start
        self.end = end
        self.stdscr = curses.initscr()
        pass

    def update(self,value):
        message = "#"*int(value)
        self.stdscr.erase()
        self.stdscr.addstr("["+self.slashes[self.state]+"]"+message+"-"+str(value)+"%")
        self.stdscr.refresh()
        self.state=self.state+1
        if self.state>3:
            self.state=0
        pass
    def kill(self):
        del self

from random import randint
import lib.statusBar
import time
import curses


def main(names: list,first,second):
    statBar = lib.statusBar.statusBar(0,144)
    startTime = time.time()
    val=0
    tval = 0
    maxTiming = 15
    while True:
        timing = time.time() - startTime
        if timing<maxTiming:
            for i in range(0,5):
                if timing>2 and timing<4:
                    tval = 12
                if timing>4 and timing<6:
                    tval = 34
                if timing>6 and timing<10:
                    tval = 69
                if timing>10 and timing<12:
                    tval = 144
                if timing>12 and timing<13:
                    tval = 101

                if val<tval:
                    val=val+1
                elif val>tval:
                    val=val-1

                statBar.update(val)
                time.sleep(0.05)
        if timing>maxTiming:            
            stdscr = statBar.stdscr
            statBar.kill()
            stdscr.addstr("init success, starting AI to perform this task\n")
            stdscr.refresh()
            curses.endwin()
            print("result:",sep="")
            for k in range(0,len(names)): 
                time.sleep(0.5)               
                print(names[k]+" is ",end="")
                time.sleep(0.5)
                if randint(0,1)==1:
                    print(first)
                else:
                    print(second)
                pass

            break
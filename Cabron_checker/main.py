from random import randint
import lib.statusBar
import time
import curses


def main(anim: bool,names: list, first: str, second: str):
    stdscr = curses.initscr()
    stdscr.refresh()

    progressBar = lib.statusBar.statusBar(0,144)
    startTime = time.time()
    currentTiming = startTime
    val=0
    progressBarValue = 0
    maxTiming = 15

    while True:
        if anim:
            currentTiming = time.time() - startTime
            if currentTiming<maxTiming:
                for i in range(0,5):
                    # loading animation
                    if currentTiming>2 and currentTiming<4:
                        progressBarValue = 12
                    if currentTiming>4 and currentTiming<6:
                        progressBarValue = 34
                    if currentTiming>6 and currentTiming<10:
                        progressBarValue = 69
                    if currentTiming>10 and currentTiming<12:
                        progressBarValue = 144
                    if currentTiming>12 and currentTiming<13:
                        progressBarValue = 101

                    if val<progressBarValue:
                        val=val+1
                    elif val>progressBarValue:
                        val=val-1

                    progressBar.update(val)
                    time.sleep(0.05)
        if currentTiming>maxTiming or not anim:            
            stdscr = progressBar.stdscr
            progressBar.kill()
            # ?
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

            time.sleep(1)
            break
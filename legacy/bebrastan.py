import requests
from multiprocessing import Process
def spam():
    i = 1
    while True:
        print(i)
        i=i+1
        requests.get('https://camo.githubusercontent.com/25eac3b6a48df9b23361192995aa6b8600d00ac8d75030171d59974ce3beb47c/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d652f696e736f6c6974756d2f636f756e742e737667')
def main():
    for i in range(1,100):
        p = Process(target=spam)
        p.start()
    while True:
        print("-")
main()
#!/usr/local/bin/python3

import wxWorks as WX
  
def send():
    WX.sendMessage("Hello World!", True)

if __name__ == '__main__':
    send()
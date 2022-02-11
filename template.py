#!/usr/bin/env python3
import os
from pwn import *

BIN = "[CHALL_NAME]"
HOST = "chall.remote.ctf"
PORT = 42666
USER = "USER"
PASS = "PASS"
LOCALBIN = os.getcwd() + "/" + BIN

def exploit(r):
    print("[+] IMPLEMENT ME")

def starter():
    r = ""
    if (len(sys.argv) == 2):
        if sys.argv[1] == "remote":
            r = remote(HOST,PORT)
        elif sys.argv[1] == "remote-ssh":
            s = ssh(host=HOST, user=USER, password=PASS,port=PORT)
            r = s.process(BIN)
        else: # no debug
            r = process(LOCALBIN)
    else:
        context.terminal = ["tmux", "splitw", "-h"]
        r = process(LOCALBIN)
        gdb.attach(r, """
        break main
        continue
        """)
    return r

if __name__ == "__main__":
    r = starter()
    exploit(r)

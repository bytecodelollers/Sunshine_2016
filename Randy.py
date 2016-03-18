sh = remote("4.31.182.242", 9002)
#sh = process("/root/Desktop/ctf/sunshine/randy_noflag")
print sh.recvuntil("DebugInfo: ", timeout=1)
data = sh.recvline(timeout=1)
print "Mydata = " + data
sh.recv(timeout=1)
#print data[41:45]
#data = data[41:45]
#data = "qlrf"
rand = []
for x in data[0:4]:
    cpy = x.encode('hex')
    value = int(cpy, 16)
    calc = value - 65
    print "{} - 65 = {}".format(value, calc)
    rand.append(chr(calc))

print rand
print ' '.join(x.encode('hex') for x in rand)
rand = ''.join(rand)
sh.sendline(rand[::-1])
print sh.recv()
sh.close()

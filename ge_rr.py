
def bitlen(n):
    i=0
    while (1<<i) <n:
        i = i+1
    return i

f= open("rsa_pub.txt")
out = open("rr.txt","w")
n =  f.readline()  
N = int(n[4:],base=16)
R = 1<<bitlen(N)
RR = R*R%N

out.writelines('RR = %0x'%RR)
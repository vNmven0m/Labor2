import re
def binär(z):
    #binär in 8erBlöcken
    z = int(z, 16)
    z = bin(z)
    egal, z = str(z).split("b", 1)
    while len(z) % 8 != 0:
        z = "0" + z
    z = re.findall("........",z)
    return z
def addition(messageblock,keyarray):
    m = messageblock
    k = keyarray
    k = k[0]
    res = []

    mlist = [char for char in m]
    # print(d1,"\n",dlist1)

    klist = [char for char in k]
    # print(d2, "\n", dlist2)
    result = [int(mlist[x]) + int(klist[x]) for x in range(len(mlist))]
    for n, i in enumerate(result):
        if i == 2:
            result[n] = 0
    r = "".join(str(result))
    result = ''.join(c for c in r if c.isnumeric())
    res.append(result)
    return result
def zahl(a,i):
    #CTR mode Counter
    a = int(a, 2)
    b = a*i
    b = bin(b)
    egal, b = str(b).split("b", 1)
    add = 0
    while len(b) % 8 != 0:
        b = "0" + b
        add = add + 1
    return b, add
def ECB(m,k):

    res = [addition(m[i],[k[0][::-1]]) for i in range(len(m))]
    return res
def CBC(m,k,z):
    res = []
    d1 = addition(addition(m[0],z),[k[0][::-1]])
    res.append(d1)
    for i in range(1,len(m)):
        d = addition(addition(m[i],[res[i-1]]),[k[0][::-1]])

        res.append(d)
    return res
def CTR(m,k,v,c):
    r=[]
    for i in range(len(m)):
        z = addition(v[0],zahl(c[0],i+1))
        d = addition(addition(z,[k[0][::-1]]),[m[i]])
        r.append(d)
    return r

#in1 = input("Nachricht: ")
in1 = "a7b8c9d6e504"
#in2 = input("Schlüssel: ")
in2 = "a5"
#in3 = input("Initalisierungsvektor: ")
mode = input("ECB(1);CBC(2);CTR(3):")
mode = int(mode)
#nice
m = binär(in1)
k = binär(in2)
print("Message in 0b:",m,)
print("Key in 0b",k)
if mode == 1:
    #ECB
    result = ECB(m,k)
else:
    # in3 = input("Initalisierungsvektor: ")
    in3 = "23"
    v = binär(in3)
    print("Initalisierungsvektor in 0b", v)
    if mode == 2:
        #CBC
        result = CBC(m,k,v)
    else:
        if mode == 3:
            #CTR
            # in4 = input("ctr: ")
            in4 = "3"
            c = binär(in4)
            print("ctr in 0b", c)
            result = CTR(m,k,v,c)

        else:
            input("Gültigen Wert für mode angeben:(1;2;3)")
            exit()
print("Ergebis in 0b:",result)
r = "".join(str(result))
res = ''.join(c for c in r if c.isnumeric())
res=int(res,2)
res=hex(res)
print("Ergebnis:",res)
input("Press Enter to exit")

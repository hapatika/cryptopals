def h2b(H):
    b=''
    for i in H:
        bt=''
        i=int(i,base=16)
        
        while i>=1:
            bt = str(int(i%2)) + bt
            i/=2
        bt='0'*(4-len(bt))+bt
        b+=bt
        
    return b

def xor(a,b):
    c=''
    for i in range(len(a)):
        if a[i] == b[i]:
            c+='0'
        else:
            c+='1'
    #print(c)
    return c

def bax2hex(c):
    l1=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    w=''
    for i in range(0,len(c),4):
        p=int(c[i:i+4], base=2)
        w+=l1[p]
    print(w)
    return w


def xorhex(a,b):
    bax2hex(xor(h2b(a),h2b(b)))

xorhex('1c0111001f010100061a024b53535009181c','686974207468652062756c6c277320657965')
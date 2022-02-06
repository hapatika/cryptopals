def h2b(H):
    l1=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    b=''
    for i in H:
        s1 = bin(l1.index(i))[2:]
        while len(s1)%4 != 0:
            s1 = '0'+s1
        b += s1
    return b

def bin_chunk(num):
    # takes 6 digit binary number and returns base64 equivalent
    num = int(num,base=2)
    if(num < 26):
        return chr(num+ord('A'))
    num -= 26
    if(num < 26):
        return chr(num+ord('a'))
    num -= 26
    if(num < 10):
        return chr(num+ord('0'))
    num -= 10
    if(num == 0):
        return '+'
    return '/'

def b_to_64(H):
    #H = '0'*(6-(len(H)-1)%6)+1);
    while len(H)%6 != 0:
        H = '0'+H
    H_64 = ''
    i = 0
    while i < len(H):
        H_64 += bin_chunk(H[i:i+6])
        i = i+6
    return H_64

def hex_to_64(H):


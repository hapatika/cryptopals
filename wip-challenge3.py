import challegne1

def xor(a,b):
    c=''
    for i in range(len(a)):
        if a[i] == b[i]:
            c+='0'
        else:
            c+='1'
    return c

def xorz(bino):
    #bino is h2b(inp)
    lisp = []
    c=''
    for i in range(0,len(bino),4):
        for j in range(16):
            j='0'*(4-len(bin(j)[2:]))+bin(j)[2:]
            c+=xor(bino[i:i+4], bin(j))
            j=int(j, base =2)
        lisp.append(c)
    return lisp

#call challenge 1 function to convert to ASCII idr how to save as a module or whatever

def scoring(eng):
    # method 1 : char freq (very annoying that they gave this as a hint because it is trivial everyone's first thought
    # probably). i can't think of how to score by char freq while accounting for sampling bias but here's a shot in the dark anyway
    # arr = [letters in english in descending order of frequency]
    # vec = [letters of decoded cipher in desc order of freq]
    # sum over all a : |vec.index(a) - arr.index(a)|/largest difference (this is so...not it lmao)
    # and then order by min(sum) over all 16 keys
    # if '+' or '/' or numeric values show up in xoring using any key k disregard k
    # 
    # average length of words and standard deviation (i.e. oh wait not all words are capitalised...sentences? terrible idea.)
    # 

    ##### ok so since len(b64) = 2/3 * len(b16)
    # for any len(bino) > 16 it is more effective to just xor the 6-bit grouping with b64 characters 
    pass

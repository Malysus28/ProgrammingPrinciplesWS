def happy (s):
    out = False

    if len(s) == 1:
        out = False

    if len(s) >1:
        for i in range (len(s)):
            if s[0] == 'g' and s[1] == 'g': #check if the first two char is g
                out = True
                break
            if s[-1] == 'g' and s[-2] == 'g': #check if the last two car is g
                out = True
                break
            if 0 < i < len (s) -1 and s [i] == 'g' and (s [i-1]=='g' or s [i+1]=='g'):
                out = True
                break
    return out


s= input ("String:")
print (happy(s))

#pass Break Continue

#break terminates the loop sequence, it should be inside the loop

# c = charecters for reference

s = "blah,blah,blah"
n = 0
for c in s:
    if c == ',':
        break
    else:
        n+=1
    print (n)
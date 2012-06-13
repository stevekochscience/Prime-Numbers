p = []
f = open("p3000.txt")

for line in f:
    p.append(int(line))

cc = 0
lc = 0
    
for i in range(2,200):
    if i in p:
        print repr(i).rjust(3),
    else:
        print "   ",
        
    cc += 1
    if cc == p[lc]:
        lc += 1
        cc = 0
        print
    else:
        pass
        
    

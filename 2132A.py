t = int(input())
for _ in range(t):
    l_a =  int(input())
    a = str(input())
    l_b= int(input())
    b = str(input())
    c=str(input())
    c=list(c)
    a=list(a)
    b=list(b)
    for i in range(0,l_b):
        if c[i]=="V":
            a.insert(0,b[i])
        else:
            a.append(b[i])
    ans="".join(a)
    print(ans)
    
    # solved this problem on 18/12/25
    # just check if c[i]  is v or d. if it is v then appendb[i] to beggining else to append to end
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
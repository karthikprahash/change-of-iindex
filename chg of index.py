# change-of-iindex
i=int(input())
p=list(map(int,input().split()))
l=p[0]
if i==len(p):
    for x in range(1,len(p)):
        if p[x]>l:
            l=p[x]
        else:
            print(x-1)
            break
        
    
    
    
    
    
    

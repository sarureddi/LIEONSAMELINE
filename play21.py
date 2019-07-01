x11,y11=list(map(int,input().split()))
x22,y22=list(map(int,input().split()))
x33,y33=list(map(int,input().split()))
if (x11==x22==x33 or y11==y22==y33 or(x11==y11 and x22==y22 and x33==y33)):
    print ("yes") 
else: 
    print ("no")

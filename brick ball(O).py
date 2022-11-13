a=int(input("Enter size of the NxN matrix :"))
for i in range(a):
    if(i==0 ): 
        for j in range(a):
            print("W",end="   ")
    elif(i==a-1):
        for j in range(a):
            if(j==0 or j==a-1):
                print("W",end="   ")
            elif(j==(a//2)):
                print("O",end="   ")
            else:
                print("G",end="   ")
    else:
        for j in range(a):
            if(j==0 or j==a-1):
                print("W",end="   ")
            else:
                print(" ",end="   ")
    print()
b="y"
e=[]
while(b=="y" or b=="Y"):
    l=list((input("Enter the brick's position and the brick type :").split(" ")))
    b=input("Do you want to continue(Y or N)?")
    for i in range(len(l)):
        if l[i].isdigit():
            l[i]=int(l[i])
    e.append(l)
c=int(input("Enter ball Count :"))
for i in range(a):
    if(i==0 ):
        for j in range(a):
            print("W",end="   ")
    elif(i==a-1):
        for j in range(a):
            if(j==0 or j==a-1):
                print("W",end="   ")
            elif(j==(a//2)):
                print("O",end="   ")
            else:
                print("G",end="   ")
    else:
        for j in range(a):
            if(j==0 or j==a-1):
                print("W",end="   ")
            else:
                d=0
                for k in e:
                    if i==k[0] and j==k[1]:
                        if(len(str(k[2]))<2):
                            print(k[2],end="   ")
                            d=1
                        else:
                            print(k[2],end="  ")
                            d=1
                if(d==0):
                    print("",end="    ")
    print()
print("Ball Count :",c)
f=len(e)
w=a//2
p=[]
p.append(w)
bb=0
while(c>0 and f>0):
    cc=0
    h=input("Enter the direction in which the ball need to traverse :")
    m=e[0][0]
    for i in e:
        if(i[0]>m and i[2]!=" " ):
            m=i[0]
    
    hh=[]
    if(h=="ST"):
        y=w
    elif(h=="LD"):
        y=w-1
    elif(h=="RD"):
        y=w+1
    for i in e:
        if(i[1]==y and i[2]!=" "):
            hh.append(i[0])
    
    
    if(h=="ST" and len(hh)>=1):
        for i in range(a):
            for j in range(a):
                for k in e:
                    if(i==k[0] and j==k[1]):
                        if(j==w and cc==0 and i==max(hh)):
                            d=1
                            cc=1
                            if(k[2]=="DS"):
                                www=k[0]
                                wwww=k[1]
                                for v in e:
                                    if(v[0]==www or v[0]==(www-1) or v[0]==(www+1)):
                                        if(v[1]==wwww or v[1]==(wwww-1) or v[1]==(wwww+1)):
                                            v[2]=" "
                                            f=f-1
                            elif(k[2]=="DE"):
                                www=k[0]
                                for v in e:
                                    if(v[0]==www):
                                        v[2]=" "
                                        f=f-1
                            elif(str(k[2]).isdigit()):
                                if((k[2]-1)==0):
                                    k[2]=" "
                                    f=f-1
                                else:
                                    k[2]=k[2]-1
                            elif(str(k[2])=="B"):
                                k[2]=" "
                                f=f-1
                                bb=bb+1
                                if(bb%2==0):
                                    p.append(w-1)
                                else:
                                    p.append(w+1)
        
        if(w not in p):
            c=c-1
                                    
        for i in range(a):
            if(i==0 ):
                for j in range(a):
                    print("W",end="   ")
            elif(i==a-1):
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="   ")
                    elif(j==(w)):
                        print("O",end="   ")
                    elif((j in p) and len(p)>1):
                        print("-",end="  ")
                    else:
                        print("G",end="   ")
            else:
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="   ")
                    else:
                        d=0
                        for k in e:
                            if i==k[0] and j==k[1]:
                                if(len(str(k[2]))<2):
                                    print(k[2],end="   ")
                                    d=1
                                else:
                                    print(k[2],end="  ")
                                    d=1
                        if(d==0):
                            print("",end="    ")
            print()
                   
        """for i in range(a):
            if(i==0 ):
                for j in range(a):
                    print("W",end="  ")
            elif(i==a-1):
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="  ")
                    elif(j==(w)):
                        print("O",end="  ")
                    elif((j in p) and len(p)>1):
                        print("-",end="  ")
                    else:
                        print("G",end="  ")
            else:
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="  ")
                    else:
                        d=0
                        for k in e:
                            if i==k[0] and j==k[1]:
                                print(k[2],end="  ")
                                d=1
                        if(d==0):
                            print("",end="   ")
            print()"""
        w=w
    elif(h=="LD" and len(hh)>=1):
        
        for i in range(a):
            for j in range(a):
                for k in e:
                    if(i==k[0] and j==k[1]):
                        if(j==(w-1) and cc==0 and i==max(hh)):
                            d=1
                            cc=1
                            if(k[2]=="DS"):
                                www=k[0]
                                wwww=k[1]
                                for v in e:
                                    if(v[0]==www or v[0]==(www-1) or v[0]==(www+1)):
                                        if(v[1]==wwww or v[1]==(wwww-1) or v[1]==(wwww+1)):
                                            v[2]=" "
                                            f=f-1
                            elif(k[2]=="DE"):
                                www=k[0]
                                for v in e:
                                    if(v[0]==www):
                                        v[2]=" "
                                        f=f-1
                                
                                        
                            elif(str(k[2]).isdigit()):
                                if((k[2]-1)==0):
                                    k[2]=" "
                                    f=f-1
                                else:
                                    k[2]=k[2]-1
                            elif(str(k[2])=="B"):
                                k[2]=" "
                                f=f-1
                                bb=bb+1
                                if(bb%2==0):
                                    p.append(w-1)
                                else:
                                    p.append(w+1)
        
        if(w-1 not in p):
            c=c-1
        for i in range(len(p)):
            p[i]=p[i]-1
        for i in range(a):
            if(i==0 ):
                for j in range(a):
                    print("W",end="   ")
            elif(i==a-1):
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="   ")
                    elif(j==((w)-1)):
                        print("O",end="   ")
                    elif((j in p) and len(p)>1):
                        print("-",end="  ")
                    else:
                        print("G",end="   ")
            else:
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="   ")
                    else:
                        d=0
                        for k in e:
                            if i==k[0] and j==k[1]:
                                if(len(str(k[2]))<2):
                                    print(k[2],end="   ")
                                    d=1
                                else:
                                    print(k[2],end="  ")
                                    d=1
                        if(d==0):
                            print("",end="    ")
            print()

            
                            
        """for i in range(a):
            if(i==0 ):
                for j in range(a):
                    print("W",end="  ")
            elif(i==a-1):
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="  ")
                    elif(j==(w-1)):
                        print("O",end="  ")
                    elif((j in p) and len(p)>1):
                        print("-",end=" ")
                    else:
                        print("G",end="  ")
            else:
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="  ")
                    else:
                        d=0
                        for k in e:
                            if i==k[0] and j==k[1]:
                                print(k[2],end="  ")
                                d=1
                        if(d==0):
                            print("",end="   ")
            print()"""
        w=w-1
        
    elif(h=="RD" and len(hh)>=1):
  
        for i in range(a):
            for j in range(a):
                for k in e:
                    if(i==k[0] and j==k[1]):
                        if(j==(w+1) and cc==0 and i==max(hh)):
                            d=1
                            cc=1
                            if(k[2]=="DS"):
                                www=k[0]
                                wwww=k[1]
                                for v in e:
                                    if(v[0]==www or v[0]==(www-1) or v[0]==(www+1)):
                                        if(v[1]==wwww or v[1]==(wwww-1) or v[1]==(wwww+1)):
                                            v[2]=" "
                                            f=f-1
                            elif(k[2]=="DE"):
                                www=k[0]
                                for v in e:
                                    if(v[0]==www):
                                        v[2]=" "
                                        f=f-1
                             
                                        
                            elif(str(k[2]).isdigit()):
                                if((k[2]-1)==0):
                                    k[2]=" "
                                    f=f-1
                                else:
                                    k[2]=k[2]-1
                            elif(str(k[2])=="B"):
                                k[2]=" "
                                f=f-1
                                bb=bb+1
                                if(bb%2==0):
                                    p.append(w-1)
                                else:
                                    p.append(w+1)
        
        if(w+1 not in p):
            c=c-1
        for i in range(len(p)):
            p[i]=p[i]+1
        for i in range(a):
            if(i==0 ):
                for j in range(a):
                    print("W",end="   ")
            elif(i==a-1):
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="   ")
                    elif(j==((w)+1)):
                        print("O",end="   ")
                    elif((j in p) and len(p)>1):
                        print("-",end="  ")
                    else:
                        print("G",end="   ")
            else:
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="   ")
                    else:
                        d=0
                        for k in e:
                            if i==k[0] and j==k[1]:
                                if(len(str(k[2]))<2):
                                    print(k[2],end="   ")
                                    d=1
                                else:
                                    print(k[2],end="  ")
                                    d=1
                        if(d==0):
                            print("",end="    ")
            print()

        
        
        """for i in range(a):
            if(i==0 ):
                for j in range(a):
                    print("W",end="  ")
            elif(i==a-1):
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="  ")
                    elif(j==(w+1)):
                        print("O",end="  ")
                    elif((j in p) and len(p)>1):
                        print("-",end=" ")
                    else:
                        print("G",end="  ")
            else:
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="  ")
                    else:
                        d=0
                        for k in e:
                            if i==k[0] and j==k[1]:
                                print(k[2],end="  ")
                                d=1
                        if(d==0):
                            print("",end="   ")
            print()"""
        w=w+1
        
    if(len(hh)<1):
        for i in range(a):
            if(i==0 ):
                for j in range(a):
                    print("W",end="   ")
            elif(i==a-1):
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="   ")
                    elif(j==(y)):
                        print("O",end="   ")
                    else:
                        print("G",end="   ")
            else:
                for j in range(a):
                    if(j==0 or j==a-1):
                        print("W",end="   ")
                    else:
                        d=0
                        for k in e:
                            if i==k[0] and j==k[1]:
                                if(len(str(k[2]))<2):
                                    print(k[2],end="   ")
                                    d=1
                                else:
                                    print(k[2],end="  ")
                                    d=1
                        if(d==0):
                            print("",end="    ")
            print()
            w=y
            if(h=="ST"):
                for i in range(len(p)):
                    p[i]=p[i]
            elif(h=="LD"):
                for i in range(len(p)):
                    p[i]=p[i]-1
            elif(h=="RD"):
                for i in range(len(p)):
                    p[i]=p[i]+1
            
    if w not in p:
        c=c-1
        if(len(p)>1):
            if(w<p[0] and w<p[1]):
                p[1]=p[0]
                p[0]=w
        else:
            p[0]=w
    if(f>0):
        print("Ball Count :",c)
if(f<=0):
    print()
    print("You win HURRAY..!!")
if(c==0 and f>0):
    print()
    print("You Lost")

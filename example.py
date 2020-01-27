n=input()
c=0
for i in range(len(n)):
    if(n[i].isalpha()==0 and n[i].isdigit()==0):
        c=c+1
s=''
if(c%2!=0):
    for i in range(len(n)):
        if(n[i].isdigit()):
            if(int(n[i])%2!=0):
                s=s+n[i]
                n.replace('n[i]','*',1)
            break
    for i in range(len(n)):
        if(n[i].digit()):
            if(int(n[i])%2==0):
                s=s+n[i]
                n.replace('n[i]','*',1)
            continue
        if(n[i].digit()):
            s=s+n[i]
print(s)

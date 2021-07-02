def minion_game(st):
    strr={}
    for i in st:
        strr[i]=strr.get(i,0)+1
    kevin=[]
    stuart=[]
    ks=0
    ss=0
    for i in range(0,len(st)):
        if st[i]=='a'or st[i]=='e'or st[i]=='i'or st[i]=='o' or st[i]=='u':
            kevin.append(s[i])
            x=s[i]
            ks=strr[x]+ks 
            if st in kevin :
                print("kevin",ks)
                break           
        else :
            stuart.append(st[i])
            x=st[i]
            ss=strr[x]+ss
            if st in stuart:
                print("stuart",ss)
                break
def ReassignIDs(Lvl):
    file = open('level_{}.dat'.format(Lvl) , 'r')
    StrFile = file.read()

    StringOut=''
    
    for row in StrFile.split('\n'):
        frst=True
        for el in row.split(' '):
            if(not frst):
                StringOut+=' '
            else:
                frst=False
            if(int(el)==3):
                StringOut+='8'
            elif(int(el)==2):
                StringOut+='12'
            else:
                StringOut+=el
        StringOut+='\n'
    file = open('levelR_{}.dat'.format(Lvl) , 'w')
    file.write(StringOut)
    
    
ReassignIDs(1)

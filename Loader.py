from PIL import Image

def GetSprites():
    Source = Image.open('Wolfenstein3DWalls.png')
    
    Walls = []

    for i in range(19):
        for j in range(6):
            box=(0+64*j,0+64*i,64+64*j,64+64*i)
            Walls.append(Source.crop(box))
    return Walls

class map():
    def __init__(self,n):
        file = open('level_{}.dat'.format(n) , 'r')
        StrFile = file.read()
        self.ids=[]
        i=0
        for row in StrFile.split('\n'):
            self.ids.append([])
            for el in row.split(' '):
                self.ids[i].append(int(el))
            i+=1

from PIL import Image

class map():
    def __init__(self,n):
        file = open('level_{}.dat'.format(n) , 'r')
        StrFile = file.read()
        self.ids=[]
        i=0
        for row in StrFile.split('\n'):
            self.ids.append([])
            for el in reversed(row.split(' ')):
                try:
                    self.ids[i].append(int(el))
                except:
                    pass
            i+=1

def GetSlicedSprites(w,h):
    render = Image.new('RGBA', (64, 64))

    Source = Image.open('Wolfenstein3DWalls.png')
    
    Walls = []

    WallsSliced = []
    
    for i in range(18):
        for j in range(6):
            box=(0+64*j,0+64*i,64+64*j,64+64*i)
            Walls.append(Source.crop(box))
    
    WallsSliced.append([])
    i=1
    for Wall in Walls:
        WallsSliced.append([])
        for j in range(int(64)):
            WallsSliced[i].append(Image.new('RGBA', (1, 64)))
            WallsSliced[i][j].paste(Wall.crop((j,0,j+1,64)))
            WallsSliced[i][j]=WallsSliced[i][j].resize((1,h), resample=Image.NEAREST)
        i+=1
    return WallsSliced

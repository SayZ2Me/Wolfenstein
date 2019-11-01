import math
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
class ray():
    def __init__(self,direction):
        self.direction = direction
    
class player():
    def __init__(self,x,y,angle,FOW,RaysQuantity):

        angle = angle * math.pi / 180
        
        self.position = point(x,y)
        self.rays = []
        self.Forward =  ray(angle)
        
        FOW = FOW * math.pi / 180
        RayAngle = FOW / (RaysQuantity-1)
        angle -= FOW/2
        
        for i in range(RaysQuantity):
            self.rays.append(ray(angle))
            angle += RayAngle
    
    def move(self,direction,Level):
        data=[]
        if(direction > 0):
            data = ray_cast(self.position.x,self.position.y,self.Forward,Level)
        else:
            self.Forward.direction+=math.pi
            self.Forward.direction%=math.pi*2
            data = ray_cast(self.position.x,self.position.y,self.Forward,Level)
            self.Forward.direction-=math.pi
            self.Forward.direction%=math.pi*2
        if(data[3]>1):
            self.position.x += 0.1 * math.cos(self.Forward.direction)*direction
            self.position.y += 0.1 * math.sin(self.Forward.direction)*direction
            
    def rotate(self,angle):
        angle = angle * math.pi / 180
        
        self.Forward.direction += angle
        self.Forward.direction %= math.pi *2
        if(self.Forward.direction<0):
            self.Forward.direction=2*math.pi-self.Forward.direction
        
        for ray in self.rays:
            ray.direction += angle
            ray.direction %= math.pi*2

def ray_cast(x,y,ray,Level):
    
    angle = ray.direction
    data=[]

    dx=0
    dy=0

    FvC=point(0,0)
    FhC=point(0,0)
    
    IncVx=0
    IncVy=0
    IncHx=0
    IncHy=0

    
    if(angle >= 0 and angle < math.pi/2):
        dx=round(x) + 0.5 - x
        dy=round(y) + 0.5 - y

        FvC=point(dx + x,y + dx * math.tan(angle))
        FhC=point(x + dy * math.tan(math.pi / 2-angle),y + dy)

        IncVx=1
        IncVy= 1 * math.tan(angle)
            
        IncHx= 1 * math.tan(math.pi / 2-angle)
        IncHy=1
        
        dx=0.5
        dy=0.5

    if(angle >= math.pi/2 and angle < math.pi):
        dx=abs(round(x) - 0.5 - x)
        dy=round(y) + 0.5 - y

        FvC=point(x - dx,y + dx / math.tan(angle-math.pi/2+0.0000001))
        FhC=point(x - dy / math.tan(math.pi-angle+0.0000001),y + dy)

        IncVx=-1
        IncVy=1 / math.tan(angle-math.pi/2+0.000001)
            
        IncHx=-(1 / math.tan(math.pi-angle+0.000001))
        IncHy=1
        
        dx=-0.5
        dy=0.5

    if(angle >= math.pi and angle < math.pi*3/2):
        dx=abs(round(x) - 0.5 - x)
        dy=abs(round(y) - 0.5 - y)

        FvC=point(x - dx,y - dx * math.tan(angle-math.pi))
        FhC=point(x - dy * math.tan(math.pi*3/2-angle),y - dy)

        IncVx=-1
        IncVy=-(1 * math.tan(angle-math.pi))
            
        IncHx=-(1 * math.tan(math.pi*3/2-angle))
        IncHy=-1
        
        dx=-0.5
        dy=-0.5
    
    if(angle >= math.pi*3/2 and angle < 2*math.pi):
        dx=round(x) + 0.5 - x
        dy=abs(round(y) - 0.5 - y)

        FvC=point(x + dx,y - dx * math.tan(math.pi * 2 - angle))
        FhC=point(x + dy * math.tan(angle - math.pi*3/2),y - dy)

        IncVx=1
        IncVy=-(1 * math.tan(math.pi * 2 - angle))
            
        IncHx=1 * math.tan(angle - math.pi*3/2)
        IncHy=-1
        
        dx=0.5
        dy=-0.5

    while True:
        
        vd=math.sqrt((FvC.x - x) * (FvC.x - x) + (FvC.y - y) * (FvC.y - y))
                
        hd=math.sqrt((FhC.x - x) * (FhC.x - x) + (FhC.y - y) * (FhC.y - y))
                  
        if vd < hd:
            if(Level.ids[round(FvC.x+dx)][round(FvC.y)]>0):
                data.append(1)
                data.append(FvC.y)
                if(Level.ids[round(FvC.x-dx)][round(FvC.y)]==-1):
                    data.append(51)
                else:
                    data.append(Level.ids[round(FvC.x+dx)][round(FvC.y)])
                data.append(vd)
                return data
            else:
                FvC.x+=IncVx
                FvC.y+=IncVy
        else:
            if(Level.ids[round(FhC.x)][round(FhC.y+dy)]>0):
                data.append(0)
                data.append(FhC.x)
                if(Level.ids[round(FhC.x)][round(FhC.y)]==-1):
                    data.append(51)
                else:
                    data.append(Level.ids[round(FhC.x)][round(FhC.y+dy)])
                data.append(hd)
                return data
            else:
                FhC.x+=IncHx
                FhC.y+=IncHy

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
        
        self.position = point(x,y)
        self.rays = []
        self.Forward =  ray(angle)
        
        FOW = FOW * math.pi / 180
        RayAngle = FOW / (RaysQuantity-1)
        angle = angle * math.pi / 180 - FOW/2
        
        for i in range(RaysQuantity):
            self.rays.append(ray(angle))
            angle += RayAngle
    
    def move(self,direction,Level):
        data=[]
        if(direction>0):
            data = ray_cast(self.position.x,self.position.y,self.Forward,Level)
        else:
            self.Forward.direction+=math.pi
            self.Forward.direction%=math.pi*2
            data = ray_cast(self.position.x,self.position.y,self.Forward,Level)
            self.Forward.direction-=math.pi
            self.Forward.direction%=math.pi*2
        if(data[4]>0.5):
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
            if(ray.direction<0):
                rya.direction=2*math.pi-ray.direction

def ray_cast(x,y,ray,Level):
    
    angle = ray.direction
    data=[]
    
    if(angle >= 0 and angle <= math.pi/2):
        dx=round(x) + 0.5 - x
        dy=round(y) + 0.5 - y

        FvC=point(dx + x,y + dx * math.tan(angle))
        FhC=point(x + dy * math.tan(math.pi / 2-angle),y + dy)

        while True:
            vd=math.sqrt(math.pow((FvC.x - x),2) + math.pow((FvC.y - y),2))
                
            hd=math.sqrt(math.pow((FhC.x - x),2) + math.pow((FhC.y - y),2))
            
            if(vd) < (hd):
                if(Level.ids[round(FvC.x+0.5)][round(FvC.y)]!=0):
                    data.append(0)
                    data.append(FvC.x)
                    data.append(FvC.y)
                    data.append(Level.ids[round(FvC.x)][round(FvC.y)])
                    data.append(vd)
                    return data
                else:
                    FvC.x+=1
                    FvC.y+=1 * math.tan(angle)
            else:
                if(Level.ids[round(FhC.x)][round(FhC.y+0.5)]!=0):
                    data.append(1)
                    data.append(FhC.x)
                    data.append(FhC.y)
                    data.append(Level.ids[round(FhC.x)][round(FhC.y)])
                    data.append(hd)
                    return data
                else:
                    FhC.x+=1 * math.tan(math.pi / 2-angle)
                    FhC.y+=1

    if(angle > math.pi/2 and angle <= math.pi):
        dx=abs(round(x) - 0.5 - x)
        dy=round(y) + 0.5 - y

        FvC=point(x - dx,y + dx / math.tan(angle-math.pi/2))
        FhC=point(x - dy / math.tan(math.pi-angle),y + dy)

        while True:
            vd=math.sqrt(math.pow((FvC.x - x),2) + math.pow((FvC.y - y),2))
                
            hd=math.sqrt(math.pow((FhC.x - x),2) + math.pow((FhC.y - y),2))
 
            if(vd) < (hd):
                if(Level.ids[round(FvC.x-0.5)][round(FvC.y)]!=0):
                    data.append(0)
                    data.append(FvC.x)
                    data.append(FvC.y)
                    data.append(Level.ids[round(FvC.x)][round(FvC.y)])
                    data.append(vd)
                    return data
                else:
                    FvC.x-=1
                    FvC.y+=1 / math.tan(angle-math.pi/2)
            else:
                if(Level.ids[round(FhC.x)][round(FhC.y+0.5)]!=0):
                    data.append(1)
                    data.append(FhC.x)
                    data.append(FhC.y)
                    data.append(Level.ids[round(FhC.x)][round(FhC.y)])
                    data.append(hd)
                    return data
                else:
                    FhC.x-=1 / math.tan(math.pi-angle)
                    FhC.y+=1


    if(angle > math.pi and angle <= math.pi*3/2):
        dx=abs(round(x) - 0.5 - x)
        dy=abs(round(y) - 0.5 - y)

        FvC=point(x - dx,y - dx * math.tan(angle-math.pi))
        FhC=point(x - dy * math.tan(math.pi*3/2-angle),y - dy)

        while True:
            vd=math.sqrt(math.pow((FvC.x - x),2) + math.pow((FvC.y - y),2))
                
            hd=math.sqrt(math.pow((FhC.x - x),2) + math.pow((FhC.y - y),2))
                   
            if(vd) < (hd):
                if(Level.ids[round(FvC.x-0.5)][round(FvC.y)]!=0):
                    data.append(0)
                    data.append(FvC.x)
                    data.append(FvC.y)
                    data.append(Level.ids[round(FvC.x)][round(FvC.y)])
                    data.append(vd)
                    return data
                else:
                    FvC.x-=1
                    FvC.y-=1 * math.tan(angle-math.pi)
            else:
                if(Level.ids[round(FhC.x)][round(FhC.y-0.5)]!=0):
                    data.append(1)
                    data.append(FhC.x)
                    data.append(FhC.y)
                    data.append(Level.ids[round(FhC.x)][round(FhC.y)])
                    data.append(hd)
                    return data
                else:
                    FhC.x-=1 * math.tan(math.pi*3/2-angle)
                    FhC.y-=1
    
    if(angle > math.pi*3/2 and angle <= 2*math.pi):
        dx=round(x) + 0.5 - x
        dy=abs(round(y) - 0.5 - y)

        FvC=point(x + dx,y - dx * math.tan(math.pi * 2 - angle))
        FhC=point(x + dy * math.tan(angle - math.pi*3/2),y - dy)

        while True:
            vd=math.sqrt(math.pow((FvC.x - x),2) + math.pow((FvC.y - y),2))
                
            hd=math.sqrt(math.pow((FhC.x - x),2) + math.pow((FhC.y - y),2))
                  
            if(vd) < (hd):
                if(Level.ids[round(FvC.x+0.5)][round(FvC.y)]!=0):
                    data.append(0)
                    data.append(FvC.x)
                    data.append(FvC.y)
                    data.append(Level.ids[round(FvC.x)][round(FvC.y)])
                    data.append(vd)
                    return data
                else:
                    FvC.x+=1
                    FvC.y-=1 * math.tan(math.pi * 2 - angle)
            else:
                if(Level.ids[round(FhC.x)][round(FhC.y-0.5)]!=0):
                    data.append(1)
                    data.append(FhC.x)
                    data.append(FhC.y)
                    data.append(Level.ids[round(FhC.x)][round(FhC.y)])
                    data.append(hd)
                    return data
                else:
                    FhC.x+=1 * math.tan(angle - math.pi*3/2)
                    FhC.y-=1

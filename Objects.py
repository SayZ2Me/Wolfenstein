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
    
    def move(self,direction):
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
    
    if(angle >= 0 and angle <= math.pi/2):
        dx=round(x) + 0.5 - x
        dy=round(y) + 0.5 - y

        FvC=point(dx + x,y + dx * math.tan(angle))
        FhC=point(x + dy * math.tan(math.pi / 2-angle),y + dy)

    if(angle > math.pi/2 and angle <= math.pi):
        dx=abs(round(x) - 0.5 - x)
        dy=round(y) + 0.5 - y

        FvC=point(x - dx,y + dx / math.tan(angle-math.pi/2))
        FhC=point(x - dy / math.tan(math.pi-angle),y + dy)

    if(angle > math.pi and angle <= math.pi*3/2):
        dx=abs(round(x) - 0.5 - x)
        dy=abs(round(y) - 0.5 - y)

        FvC=point(x - dx,y - dx * math.tan(angle-math.pi))
        FhC=point(x - dy * math.tan(math.pi*3/2-angle),y - dy)
    
    if(angle > math.pi*3/2 and angle <= 2*math.pi):
        dx=round(x) + 0.5 - x
        dy=abs(round(y) - 0.5 - y)

        FvC=point(x + dx,y - dx * math.tan(math.pi * 2 - angle))
        FhC=point(x + dy * math.tan(angle - math.pi*3/2),y - dy)

    data=[]
    data.append(FvC.x)
    data.append(FvC.y)
    data.append(FhC.x)
    data.append(FhC.y)
    return data

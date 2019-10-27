from tkinter import *
from PIL import Image
import Loader,Objects,math,time

closed = False

ScrnSize = Objects.point(1280,800)

PlRaysQuant = 640

PlFOW = 60

Key = ''

UiScale = 200

def DrawCoordGrid(canvas):
    canvas.create_line(0,0,ScrnSize.x * UiScale,0,fill="blue",width=10)
    canvas.create_line(0,0,0,ScrnSize.y * UiScale,fill="red",width=10)

def create_circle(canvas,x,y,r):
    canvas.create_oval((x-r) * UiScale,(y-r) * UiScale,(x+r) * UiScale,(y+r) * UiScale,fill="black", outline="white", width=1)

def DrawPlayer(canvas,Player,Level):
    create_circle(canvas,Player.position.x,Player.position.y,0.1)
    for ray in Player.rays:
        data = Objects.ray_cast(Player.position.x,Player.position.y,ray,Level)
        #canvas.create_line(Player.position.x * UiScale,Player.position.y * UiScale,data[0] * UiScale,data[1] * UiScale,fill='red', width=1)
        #canvas.create_line(Player.position.x * UiScale,Player.position.y * UiScale,data[2] * UiScale,data[3] * UiScale,fill='blue', width=1)
    
def DrawMap(canvas,Level):
    i,j=0,0
    for row in Level.ids:
        for el in row:
            if(el != 0):
                canvas.create_rectangle((j-0.5) * UiScale,(i-0.5) * UiScale,(j+0.5) * UiScale,(i+0.5) * UiScale,fill='black',outline='white')
            j+=1
        j=0
        i+=1
        
def OnDestroy():
    global closed
    closed = True
    root.quit()
    root.destroy()

def key(event):
    global Key
    Key=event.keysym
    
def keyRel(event):
    global Key
    Key=''

root = Tk()
root.geometry("{}x{}".format(ScrnSize.x,ScrnSize.y))
root.protocol("WM_DELETE_WINDOW",OnDestroy)
root.title("Wolfenstein3D")
root.resizable(0, 0)
root.bind_all('<KeyPress>',key)
root.bind_all('<KeyRelease>',keyRel)
window = Canvas(root,width = ScrnSize.x,height = ScrnSize.y,bg='grey')
window.pack()

Player = Objects.player(1,1,0,PlFOW,PlRaysQuant)

Player.rotate(0.1)

Level = Loader.map(1)

for row in Level.ids:
    print(row)

WallSprites = Loader.GetSprites()

while not closed:
    t = time.time()
    if(Key != ''):
        if(Key == 'Right'):
            Player.rotate(5)
        if(Key == 'Left'):
            Player.rotate(-5)
        if(Key == 'Up'):
            Player.move(1)
        if(Key == 'Down'):
            Player.move(-1)
    
    window.delete("all")
        
    DrawMap(window,Level)
    
    DrawCoordGrid(window)
    
    DrawPlayer(window,Player,Level)
    
    root.update()
    print(time.time()-t)

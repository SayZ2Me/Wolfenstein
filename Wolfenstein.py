from tkinter import *
from PIL import Image,ImageTk
import Loader,Objects,math,time

closed = False

ScrnSize = Objects.point(1280,720)

ColWidth = 4

PlRaysQuant = int(ScrnSize.x/ColWidth)

PlFOW = 50

Key = ''

UiScale = 10

def DrawFrame(canvas,Player,Level):
    render = Image.new('RGBA', (ScrnSize.x, ScrnSize.y))
    global WallSprites
    i=0
    for ray in Player.rays:
        
        data = Objects.ray_cast(Player.position.x,Player.position.y,ray,Level)
        
        var = data[1]%1
        
        ImgBuf = WallSprites[data[2]*2 - data[0]][round(63*var-32)]
        
        ImgBuf = ImgBuf.resize((ColWidth,int(ScrnSize.y/data[3]*2)), resample=Image.NEAREST)
        
        render.paste(ImgBuf, (i*ColWidth,int(ScrnSize.y/2-ScrnSize.y/data[3])))

        i+=1
    
    img = ImageTk.PhotoImage(render)
    
    return img
        
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

Player = Objects.player(49,33,0,PlFOW,PlRaysQuant)

Player.rotate(-90)

Level = Loader.map(1)

WallSprites = Loader.GetSlicedSprites(ColWidth,ScrnSize.y)

while not closed:
    t = time.time()
    if(Key != ''):
        if(Key == 'Right'):
            Player.rotate(6)
        if(Key == 'Left'):
            Player.rotate(-6)
        if(Key == 'Up'):
            Player.move(3,Level)
        if(Key == 'Down'):
            Player.move(-3,Level)
    
    window.delete("all")

    Frame = DrawFrame(window,Player,Level)
    window.create_image(0, 0, anchor=NW, image=Frame)
    root.update()
    root.title("Wolfenstein3D FPS "+str(round(1/(time.time() - t),2)))
    while(time.time() - t < 0.033):
        pass

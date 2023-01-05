from tkinter import *
from time import sleep
from PIL import ImageTk, Image
from random import randint
from playsound import playsound
### list ảnh
img = [0,0,0]
y = -20
x = randint(10,680)
### tạo cửa sổ game
game = Tk();
game.title("Catch Apple")
canvas = Canvas(master=game, width=700, height=525, background="white")
canvas.pack()
#### đưa hình ảnh vào cửa sổ game
img[0] = ImageTk.PhotoImage(Image.open("/Users/haihai/Downloads/catch_apple/backgr.png"))
img[1] = ImageTk.PhotoImage(Image.open("/Users/haihai/Downloads/catch_apple/bowl.png"))
img[2] = ImageTk.PhotoImage(Image.open("/Users/haihai/Downloads/catch_apple/apple.png"))
### xác định vị trí của hình
backgr = canvas.create_image(0,0,anchor=NW, image=img[0])
bowl = canvas.create_image(0,420,anchor=NW, image=img[1])
apple = canvas.create_image(x,y,anchor=NW, image=img[2])
canvas.update()
### xây dựng tính điểm
score = 0
text_score = canvas.create_text(620,30,text="SCORE: "+ str(score), fill="red",font=("Times", 20))
### xây dựng hàm apple quả thứ 1
def AppleFall():
    global apple, score
    canvas.move(apple, 0,25)
    if canvas.coords(apple)[1]> 550:
        canvas.delete(apple)
        y=-20
        x=randint(10,680)
        apple = canvas.create_image(x,y,anchor=NW, image=img[2])
    if (canvas.coords(apple)[0] >= canvas.coords(bowl)[0] and canvas.coords(apple)[0] + 50 <= canvas.coords(bowl)[0]+120) and (canvas.coords(apple)[1]+ 50 >= canvas.coords(bowl)[1] and canvas.coords(apple)[1]+50 <= canvas.coords(bowl)[1] + 37.5):
        playsound("/Users/haihai/Downloads/catch_apple/vacham.wav")
        canvas.delete(apple)
        y=-20
        x=randint(10,680)
        apple = canvas.create_image(x,y,anchor=NW, image=img[2])
        score= score + 1
        canvas.itemconfig(text_score,text="SCORE: "+ str(score))
    canvas.update()

### xây dựng hàm apple quả thứ 2
y2 = randint(-10,500)
x2 = randint(10,680)
apple2 = canvas.create_image(x2,y2,anchor=NW, image=img[2])

def AppleFall2():
    global apple2, score
    canvas.move(apple2, 0,25)
    if canvas.coords(apple2)[1]> 550:
        canvas.delete(apple2)
        y2=-20
        x2=randint(10,680)
        apple2 = canvas.create_image(x,y,anchor=NW, image=img[2])
    if (canvas.coords(apple2)[0] >= canvas.coords(bowl)[0] and canvas.coords(apple2)[0] + 50 <= canvas.coords(bowl)[0]+120) and (canvas.coords(apple2)[1]+ 50 >= canvas.coords(bowl)[1] and canvas.coords(apple2)[1]+50 <= canvas.coords(bowl)[1] + 37.5):
        playsound("/Users/haihai/Downloads/catch_apple/vacham.wav")
        canvas.delete(apple2)
        y2=-20
        x2=randint(10,680)
        apple2 = canvas.create_image(x,y,anchor=NW, image=img[2])
        score= score + 1
        canvas.itemconfig(text_score,text="SCORE: "+ str(score))
    canvas.update()

def right():
    global bowl
    if canvas.coords(bowl)[0]<650:
        canvas.move(bowl, 50,0)
    canvas.update
def left():
    global bowl
    if canvas.coords(bowl)[0]>-10:
        canvas.move(bowl, -50,0)
    canvas.update
def keyPess(event):
    if event.keysym == "Right":
        right()
    if event.keysym == "Left":
        left()
canvas.bind_all("<KeyPress>", keyPess)
gameOver = False
while not gameOver:
    AppleFall()
    AppleFall2()
    sleep(0.05)

game.mainloop()



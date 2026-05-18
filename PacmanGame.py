from tkinter import *
import random as r 
class Pacman:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = 30
        self.speed = 5
        self.direction = "None"
        self.body = canvas.create_text(x + 15,y + 15,text="💀",
                                       font=("Arial", 20,"bold"),fill="#fff500")


    def can_move(self, new_x, new_y):
        row_top = new_y // cell_size
        row_bottom = (new_y + self.size - 1) // cell_size
        col_left = new_x // cell_size
        col_right = (new_x + self.size - 1) // cell_size

        if maze[row_top][col_left] == 0 and \
           maze[row_top][col_right] == 0 and \
           maze[row_bottom][col_left] == 0 and \
           maze[row_bottom][col_right] == 0:
            return True

        return False

    def move(self):
        global mode
        if self.direction == "Right":
            new_x = self.x + self.speed

            if self.can_move(new_x, self.y):
                self.canvas.move(self.body, self.speed, 0)
                self.x = new_x

            else:
                
                if mode == "touch":
                    game_over()
                    return
                
        elif self.direction == "Left":
            new_x = self.x - self.speed

            if self.can_move(new_x, self.y):
                self.canvas.move(self.body, -self.speed, 0)
                self.x = new_x

            else:

                if mode == "touch":
                    game_over()
                    return

        elif self.direction == "Up":
            new_y = self.y - self.speed

            if self.can_move(self.x, new_y):
                self.canvas.move(self.body, 0, -self.speed)
                self.y = new_y

            else:
            
                if mode == "touch":
                    game_over()
                    return


        elif self.direction == "Down":
            new_y = self.y + self.speed

            if self.can_move(self.x, new_y):
                self.canvas.move(self.body, 0, self.speed)
                self.y = new_y

            else:
                
                if mode == "touch":
                    game_over()
                    return

#+----------starting part----------+
def play_game():
    global btn1,btn2,btn3,cnv,cnv1,cnv2, game_running,frame1,frame2
    cnv = Canvas(root,width = 1000, height = 600,
                 highlightbackground="#e0935b", background = "#e0935b")
    cnv.place(x=0,y=0)
    cnv1 = Canvas(root, width = 380, height = 550,highlightthickness = 2,
                  highlightbackground="#ff3131",background = "#ff8336")
    cnv1.place(x=310,y=25)
    cnv2 = Canvas(root,width = 330, height = 490,
                  highlightbackground="#ff751f", background = "#ff751f")
    cnv2.place(x=335, y=55)
    cnv2.create_text(165,50,text = "start play",font = ("Arial",45),fill = "#ffcd6b")
    cnv2.create_text(70,190,text = "play",font = ("Arial",23), fill = "#b7190e")
    cnv2.create_text(260,190,text = "game",font = ("Arial",23),fill = "#b7190e")
    cnv2.create_text(165,232, text = "mode",font = ("Arial",23), fill = "#b7190e")
    frame1 = Frame(root,width = 144,height = 54,background = "#ffa021")
    frame1.place(x=428,y=318)
    btn1 = Button(root,text = "time",font = ("Arial",16),foreground = "#c41717",activeforeground="#075a83",
                background = "#ffa021",command = lambda : set_mode("time"),activebackground = "#fff500")
    btn1.place(x=430,y=320, width = 140, height = 50)
    frame2 = Frame(root,width = 144,height = 54,background = "#ffa021")
    frame2.place(x=428,y=378)
    btn2 = Button(root,text = "touch",font = ("Arial",16),foreground = "#c41717",activeforeground="#075a83",
                background = "#ffa021",command = lambda : set_mode("touch"),activebackground = "#fff500")
    btn2.place(x=430,y=380, width = 140, height = 50)
    btn3 = Button(root,text = "play",font = ("Arial",16),foreground = "#c41717",activeforeground="#075a83",
                command = play ,background = "#ffa021",activebackground = "#fff500")
    btn3.place(x=430,y=440, width = 140, height = 50)

# the ending part//game_over()
def game_over():
    global text, game_running ,btn4,btn5 ,cnv3,cnv4
    game_running = False
    cnv3 = Canvas(root,width = 640, height = 400, background = "#ff914d",
                highlightbackground = "#ff914d")
    cnv3.place(x=180,y=100)
    cnv4 = Canvas(root,width = 560, height = 350, background = "#ff751f",
                highlightbackground = "#ff751f")
    cnv4.place(x=220,y=125)
    cnv4.create_text(280,100,text ="Game Over",font = ("Arial",56),fill = "#ffcd6b")
    cnv4.create_text(280,175,text ="score : "+ str(score)
                     ,font = ("Arial",32),fill = "#b7190e")
    btn4 = Button(root,text = "Menue",font = ("Arial",16),command = menue,activeforeground="#075a83",
                background = "#ffa021",foreground = "#c41717",activebackground = "#fff500")
    btn4.place(x=310,y=350,width = 140, height = 50)
    btn5 = Button(root,text = "restart",font = ("Arial",16),activebackground = "#fff500",
                command = restart,background = "#ffa021",foreground = "#c41717")
    btn5.place(x=530,y=350,width = 140, height = 50)

#+--------maze------------------+
def show_maze (maze):
    global mazes
    global rdots
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            if maze[row][col] == 1:
                mazes = canvas.create_rectangle(x1, y1, x2, y2, fill="#780020")

            else :
                rdots.append((x1, y1))
# +-----------dots----------+
def show_dot():
    global dots
    x, y = r.choice(rdots)
    dot = canvas.create_oval( x + 10,y + 10, x + 40, y + 40, fill="#4ffffa")
    dots.append(dot)

def spawn_dot():
    if len(dots) < 2 and rdots:
        show_dot()

#+--------movement-----------+
def move_player(event):

    if event.keysym == "Right" or event.keysym == "d" :
        player.direction = "Right"

    elif event.keysym == "Left" or event.keysym == "a" :
        player.direction = "Left"

    elif event.keysym == "Up" or event.keysym == "w" :
        player.direction = "Up"

    elif event.keysym == "Down" or event.keysym == "s" :
        player.direction = "Down"

#+----------collision-----------+
def check_collision():
    global score, score_text,Time,time,mode,a
    x, y = canvas.coords(player.body)
    player_coords = [
        x - 15,
        y - 15,
        x + 15,
        y + 15
    ]

    overlapping = canvas.find_overlapping(
        player_coords[0],
        player_coords[1],
        player_coords[2],
        player_coords[3]
    )

    for dot in dots[:]:
        if dot in overlapping:
            canvas.delete(dot)
            dots.remove(dot)
            score += 1
            canvas.itemconfig(score_text,text="Score: " + str(score))
    if mode == "time":
        time = time +1/20
        canvas.itemconfig(Time,text="time = " +str(int(time)))
        if int(time) == 120:
            game_over()
    else :
        canvas.delete(Time)
    spawn_dot()
#--------functions----------+
def menue():
    global player, score, dots, rdots
    global game_running, score_text, time

    game_running = False

    canvas.delete("all")

    if 'cnv3' in globals():
        cnv3.destroy()

    if 'cnv4' in globals():
        cnv4.destroy()

    if 'btn4' in globals():
        btn4.destroy()

    if 'btn5' in globals():
        btn5.destroy()

    score = 0
    time = 0

    dots.clear()
    rdots.clear()

    play_game()

def set_mode (value):
    global mode,frame1,frame2 
    mode = value
    if mode == "time":
        frame1.config(background = "#c41717")
        frame2.config(background = "#ffa021")
    else :
        frame1.config(background = "#ffa021")
        frame2.config(background = "#c41717")


def play():
    global player,  game_running,score_text,btn3,cnv,frame1,frame2
    game_running = True
    cnv.delete("all")
    cnv1.delete("all")
    cnv2.delete("all")
    cnv.destroy()
    cnv1.destroy()
    cnv2.destroy()
    frame1.destroy()
    btn1.destroy()
    frame2.destroy()
    btn2.destroy()
    btn3.destroy()
    restart()

def restart():
    global player, score, dots, rdots,x
    global game_running, score_text, time

    game_running = False

    canvas.delete("all")

    if 'cnv3' in globals():
        cnv3.destroy()

    if 'cnv4' in globals():
        cnv4.destroy()

    if 'btn4' in globals():
        btn4.destroy()

    if 'btn5' in globals():
        btn5.destroy()

    score = 0
    time = 0

    dots.clear()
    rdots.clear()
    show_maze(maze)
    player = Pacman(canvas, 60, 60)
    score_text = canvas.create_text(100, 20,text="Score: 0",
                                    fill="#fcff7a",font=("Arial", 20,"bold"))
    if mode == "time":
        Time = canvas.create_text(600,20,text = "time = 0",
                                  font = ("Arial",20,"bold"),fill = "#fcff7a" )

    show_dot()
    game_running = True
    game_loop()

def stop():
    root.quit()   

def game_loop():
    if game_running:
        player.move()
        check_collision()
        root.after(50, game_loop)
        
#+-------------------main part---------------------------+
#       +----data initilization------+
score = 0
game_running = False
dots = []
rdots = []
cell_size = 50

maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,1,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]
width = 400
height = 400
mode = "touch"
time = 0
#   +------------basic UI --------------+
root = Tk()
root.geometry("1000x600")
root.configure(background="black")

bg1 = Canvas (root, width = 1000 , height = 600,
               background = "#ffb47e",highlightbackground = "#ffb47e")
bg1.place(x = 0, y = 0)
bg2 = Canvas(root, width = 900 ,height= 540 ,
             background = "#e0935b",highlightbackground = "#ff3131")
bg2.place(x=50,y =30)
canvas = Canvas(root , width = 750, height = 450,
             background  = "#d27937",highlightbackground = "#d27937")
canvas.place(x=125,y=75)

score_text = canvas.create_text(100, 20,text="Score: 0",
                                fill="#fcff7a",font=("Arial", 20,"bold"))

Time = canvas.create_text(600,20,text = "time = 0",font = ("Arial",20,"bold"),fill = "#fcff7a" )

#     +------------function calling-------------+
player = Pacman(canvas, 60, 60)
root.bind("<KeyPress>", move_player)
root.bind("<BackSpace>", lambda e: stop())
root.bind("<Return>", lambda e: restart())
show_maze(maze)
show_dot()
play_game()

root.mainloop()

from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab


# Definir clase y constructor del programa
class Draw():
    def __init__(self,root):

# Configuración de la ventana
        self.root =root
        self.root.title("Gech BOX Studio (Beta) v1.0.0")
        self.root.iconbitmap("logo.ico")
        self.root.geometry("1100x600")
        self.root.resizable(0,0)
        self.root.config(bg="gray23")

# Menu
        menu = Menu(root)
        File = Menu(menu) 
        Help = Menu(menu)
        menu.add_cascade(label= 'File', menu = File)
        menu.add_cascade(label= 'Help', menu = Help)


# Vars   
        self.pointer= "black"
        self.erase="white"

    
        text=Text(root)

        self.gechv = Label(self.root,bg='gray15',height=900,width=1000)
        self.gechv.place(x=100,y=0)

        
# Elegir color del panel
        self.pick_color = LabelFrame(self.root,font =('arial',15),bd=0,relief=RIDGE,bg="gray23")
        self.pick_color.place(x=23,y=40,width=90,height=185)

        colors = ['black','gray17','red', 'yellow','green','blue','white','gray','orange','gold','dark green','royal blue']
        i=j=0
        for color in colors:
            Button(self.pick_color,bg=color,bd=0,relief=RIDGE,width=3,command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j=1

# Borrador y propiedades
        self.eraser_btn= Button(self.root,text="Eraser",bg='gray30',fg="White",command=self.eraser,width=9,height=1,relief=RIDGE)
        self.eraser_btn.place(x=15,y=190)

# Botón de reinicio
        self.clear_screen= Button(self.root,text="Clear",bg='gray30',fg="White",command= lambda : self.background.delete('all'),width=9,height=1,relief=RIDGE)
        self.clear_screen.place(x=15,y=220)

# Save Button for saving the image in local computer
        self.save_btn= Button(self.root,text="ScreenShot",bg='gray30',fg="White",command=self.save_drawing,width=9,height=1,relief=RIDGE)
        self.save_btn.place(x=15,y=250)

# Background Button for choosing color of the Canvas
        self.bg_btn= Button(self.root,text="Background",bg='gray30',fg="White",command=self.canvas_color,width=9,height=1,relief=RIDGE)
        self.bg_btn.place(x=15,y=280)


#Creating a Scale for pointer and eraser size
        self.pointer_frame= LabelFrame(self.root,bd=0,bg="gray23",font=('arial',15,'bold'),relief=RIDGE)
        self.pointer_frame.place(x=20,y=320,height=200,width=70)

        self.pointer_size =Scale(self.pointer_frame,orient=VERTICAL,from_ =88 , to =0, length=200)
        self.pointer_size.set(1)
        self.pointer_size.grid(row=0,column=2,padx=15)


#Defining a background color for the Canvas 
        self.background = Canvas(self.root,bg='white',relief=GROOVE,height=550,width=960)
        self.background.config(cursor="circle")
        self.background.place(x=100,y=40)

#Bind the background Canvas with mouse click
        self.background.bind("<B1-Motion>",self.paint) 



# Functions are defined here

# Paint Function for Drawing the lines on Canvas
    def paint(self,event):       
        x1,y1 = (event.x-2), (event.y-2)  
        x2,y2 = (event.x+2), (event.y+2)  

        self.background.create_oval(x1,y1,x2,y2,fill=self.pointer,outline=self.pointer,width=self.pointer_size.get())

# Function for choosing the color of pointer  
    def select_color(self,col):
        self.pointer = col

# Function for defining the eraser
    def eraser(self):
        self.pointer= self.erase

# Function for choosing the background color of the Canvas    
    def canvas_color(self):
        color=colorchooser.askcolor()
        self.background.configure(background=color[1])
        self.erase= color[1]

# Function for saving the image file in Local Computer
    def save_drawing(self):
        try:
            # self.background update()
            file_ss =filedialog.asksaveasfilename(defaultextension='jpg')
            #print(file_ss)
            x=self.root.winfo_rootx() + self.background.winfo_x()
            #print(x, self.background.winfo_x())
            y=self.root.winfo_rooty() + self.background.winfo_y()
            #print(y)

            x1= x + self.background.winfo_width() 
            #print(x1)
            y1= y + self.background.winfo_height()
            #print(y1)
            ImageGrab.grab().crop((x , y, x1, y1)).save(file_ss)
            messagebox.showinfo('Screenshot Successfully Saved as' + str(file_ss))
            msgalert = root(text="Hola")
            msgalert.pack()

        except:
            print("Error in saving the screenshot")


if __name__ =="__main__":
    root = Tk()
    p= Draw(root)
    root.mainloop()
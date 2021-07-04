""" #!/usr/bin/python3 """

# importing modules 
from tkinter import *
from tkinter.filedialog import *
from stegano import exifHeader as stg
from tkinter import messagebox
from PIL import Image,ImageTk

# Encode function
def encode():
    main.destroy()
    enc=Tk()
    enc.geometry('500x400+300+150')
    enc.iconbitmap('c:/Users/91934/Downloads/hacker.ico')
    enc.title("Encoding scheme")
    enc.resizable(False,False)

# background image
    bg=ImageTk.PhotoImage(file='c:/Users/91934/Downloads/colors.png')
    my_label=Label(enc,image=bg)
    my_label.place(x=0,y=0,relheight=1,relwidth=1)

# lables and Entry boxes
    label1=Label(text="   SECRET MESSAGE   ",font = ("Helvetica 16 bold italic",10),fg="white",bg="black")
    label1.place(relx=0.1,rely=0.3,width=150,height=40)
    entry=Entry()
    entry.place(relx=0.5,rely=0.3,width=180,height=40)
    label2=Label(text="     FILE NAME     ",font = ("Helvetica 16 bold italic",10),fg="white",bg="black")
    label2.place(relx=0.1,rely=0.5,width=150,height=40)
    entrysave=Entry()
    entrysave.place(relx=0.5,rely=0.5,width=180,height=40)

# Functions
    def openfile():
        global fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg files",".jpg"),("all files","*.*")))
    
    def encodee():
        response=messagebox.askyesno("pop up","Do you want to encode the message")
        if response==1:
            stg.hide(fileopen,entrysave.get()+'.jpg',entry.get())
            messagebox.showinfo("pop up","successfully encoded")
        else:
            messagebox.showwarning("pop up","unsuccessfull")

# Buttons
    buttonselect=Button(text='Select file',command=openfile)
    buttonselect.place(relx=0.3,rely=0.7,height=40,width=80)
    buttonencode=Button(text='Encode',command=encodee)
    buttonencode.place(relx=0.5,rely=0.7,height=40,width=80)


# Decode function
def decode():
    main.destroy()
    enc=Tk()
    enc.geometry('500x400+300+150')
    enc.iconbitmap('c:/Users/91934/Downloads/hacker.ico')
    enc.title("Decoding scheme")
    enc.resizable(False,False)

# Functions
    def openfile():
        global fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg files",".jpg"),("all files","*.*")))

    def decodee():
        response=messagebox.askyesno("pop up","Do you want to decode the message")
        if response==1:
            message=stg.reveal(fileopen)
            messagebox.showinfo("pop up","successfully decoded")
        else:
            messagebox.showwarning("pop up","unsuccessfull")
# decoded message
        label4=Label(text=message, font = ("Helvetica 16 bold italic",10),fg="white",bg="black")
        label4.place(relx=0.3,rely=0.2)

# Buttons
    buttonselect=Button(text='Select file',command=openfile,borderwidth=2)
    buttonselect.place(relx=0.1,rely=0.2,height=40,width=80)
    buttondecode=Button(text='Decode',command=decodee,borderwidth=2)
    buttondecode.place(relx=0.1,rely=0.6,height=40,width=80)

# Label
    label5=Label(text="After choosing the file press to Decode the Image", font = ("Helvetica 16 bold italic",10),fg="white",bg="black")
    label5.place(relx=0.3,rely=0.6)


# Main window
main=Tk()
main.geometry('500x400+300+150')
main.title("Graphical stego tool")
main.iconbitmap('c:/Users/91934/Downloads/hacker.ico')
main.resizable(False,False)

# background image
bg=ImageTk.PhotoImage(file='c:/Users/91934/Downloads/social media.png')
my_label=Label(main,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1)

# Encode button
image=Image.open('c:/Users/91934/Pictures/encodeed.png')
image=image.resize((90, 60), Image. ANTIALIAS)
enc_btn=ImageTk.PhotoImage(image)

# Hover effect
def on_enter(e):
   encodeb.config(background='OrangeRed3', foreground= "white")
def on_leave(e):
   encodeb.config(background= 'SystemButtonFace', foreground= 'black')

encodeb=Button(image=enc_btn,command=encode,borderwidth=1,bg="black")
encodeb.place(relx=0.4,rely=0.5)

encodeb.bind('<Enter>', on_enter)
encodeb.bind('<Leave>', on_leave)

# Decode button
imageD=Image.open('c:/Users/91934/Pictures/DECODEED.png')
imageD=imageD.resize((90,60), Image. ANTIALIAS)
dec_btn=ImageTk.PhotoImage(imageD)

def on_enter(e):
   decodeb.config(background='OrangeRed3', foreground= "white")

def on_leave(e):
   decodeb.config(background= 'SystemButtonFace', foreground= 'black')

decodeb=Button(image=dec_btn,command=decode,borderwidth=1,bg="black")
decodeb.place(rely=0.7,relx=0.4)

decodeb.bind('<Enter>', on_enter)
decodeb.bind('<Leave>', on_leave)

# Top label
lab=Label(main, text="     HIDE and REVEAL using STEGO !!    ",font = "Helvetica 16 bold italic",fg="white",bg="black")
lab.place(relx=0.1,rely=0.3)

# END
main.mainloop()

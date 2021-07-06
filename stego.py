#!/usr/bin/python3

# importing modules
from tkinter import *
from tkinter.filedialog import *
from PIL import Image,ImageTk
from stegano import exifHeader as stg
from tkinter import messagebox

# root window
root=Tk()
canvas=Canvas(root, width=600,height=550)
canvas.grid(columnspan=3,rowspan=3)
root.resizable(False,False)

# Background image
logo=Image.open('Images/gaming.jpg')
logo=logo.resize((600, 550), Image. ANTIALIAS)
logo=ImageTk.PhotoImage(logo)
my_label=Label(root,image=logo)
my_label.place(x=0,y=0,relheight=1,relwidth=1)

# encode window
def encode():
    root.destroy()
    enc=Tk()
    canvas=Canvas(enc, width=600,height=550)
    canvas.grid(columnspan=3,rowspan=3)
    enc.resizable(False,False)

    # background image
    logo=Image.open('Images/panther.jpg')
    logo=logo.resize((600, 550), Image. ANTIALIAS)
    logo=ImageTk.PhotoImage(logo)
    my_label=Label(enc,image=logo)
    my_label.place(x=0,y=0,relheight=1,relwidth=1)

    # lables and Entry boxes
    label1=Label(text="   SECRET MESSAGE   ",font = ("Raleway",13),fg="white",bg="black")
    label1.place(relx=0.1,rely=0.3,width=150,height=40)
    entry=Entry()
    entry.place(relx=0.5,rely=0.3,width=180,height=40)
    label2=Label(text="     FILE NAME     ",font = ("Raleway",13),fg="white",bg="black")
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
    txt1=StringVar()
    enc_btn=Button(enc, textvariable=txt1,height=2,width=12,font="Raleway",bg="#20bebe",fg="white",command=openfile)
    txt1.set("Select file")
    enc_btn.grid(row=2,column=0)

    def ext():
        enc.destroy()

    txt2=StringVar()
    ext_btn=Button(enc, textvariable=txt2,height=2,width=12,font="Raleway",bg="#20bebe",fg="white",command=ext)
    txt2.set("Exit")
    ext_btn.grid(row=2,column=1)

    txt3=StringVar()
    dec_btn=Button(enc, textvariable=txt3,height=2,width=12,font="Raleway",bg="#20bebe",fg="white",command=encodee)
    txt3.set("Encode")
    dec_btn.grid(row=2,column=2)

    lab=Label(enc, text="   Please select the file and then ENCODE !!",font = "Helvetica 16 bold italic",fg="white",bg="black")
    lab.place(relx=0.1,rely=0.1)

    enc.mainloop()

# decode window
def decode():
    root.destroy()
    enc=Tk()
    canvas=Canvas(enc, width=600,height=550)
    canvas.grid(columnspan=3,rowspan=3)
    enc.resizable(False,False)

    # Background image
    logo=Image.open('Images/panther.jpg')
    logo=logo.resize((600, 550), Image. ANTIALIAS)
    logo=ImageTk.PhotoImage(logo)
    my_label=Label(enc,image=logo)
    my_label.place(x=0,y=0,relheight=1,relwidth=1)

    def openfile():
        global fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=(("jpeg files",".jpg"),("all files","*.*")))

    def decodee():
        response=messagebox.askyesno("pop up","Do you want to decode the message")
        if response==1:
            msg=stg.reveal(fileopen)
            messagebox.showinfo("pop up","successfully decoded")
        else:
            messagebox.showwarning("pop up","unsuccessfull")
            
# decoded message
        text_box=Text(enc, height=8,width=25,padx=15,pady=15)
        text_box.insert(1.0,msg)
        text_box.tag_config("center",justify="center")
        text_box.tag_add("center",1.0,"end")
        text_box.grid(row=1,column=1)


    # Buttons
    txt1=StringVar()
    enc_btn=Button(enc, textvariable=txt1,height=2,width=12,font="Raleway",bg="#20bebe",fg="white",command=openfile)
    txt1.set("Select file")
    enc_btn.grid(row=2,column=0)

    def ext():
        enc.destroy()

    txt2=StringVar()
    ext_btn=Button(enc, textvariable=txt2,height=2,width=12,font="Raleway",bg="#20bebe",fg="white",command=ext)
    txt2.set("Exit")
    ext_btn.grid(row=2,column=1)

    txt3=StringVar()
    dec_btn=Button(enc, textvariable=txt3,height=2,width=12,font="Raleway",bg="#20bebe",fg="white",command=decodee)
    txt3.set("Decode")
    dec_btn.grid(row=2,column=2)

    lab=Label(enc, text="   Please select the file and then DECODE !!",font = "Helvetica 16 bold italic",fg="white",bg="black")
    lab.place(relx=0.1,rely=0.1)

    enc.mainloop()

# Buttons
txt1=StringVar()
enc_btn=Button(root, textvariable=txt1,height=2,width=12,font="Raleway",bg="#20bebe",fg="white",command=encode)
txt1.set("Encode")
enc_btn.grid(row=2,column=0)

def ext():
    root.destroy()

txt2=StringVar()
ext_btn=Button(root, textvariable=txt2,height=2,width=12,font="Raleway",bg="#2ec4b6",fg="white",command=ext)
txt2.set("Exit")
ext_btn.grid(row=2,column=1)

txt3=StringVar()
dec_btn=Button(root, textvariable=txt3,height=2,width=12,font="Raleway",bg="#20bebe",fg="white",command=decode)
txt3.set("Decode")
dec_btn.grid(row=2,column=2)

# Labels
lab1=Label(root, text=" ___/\____________________/\_____    ",font = "Helvetica 16 bold italic",fg="white",bg="black")
lab1.place(relx=0.2,rely=0.1)

lab=Label(root, text="  HIDE and REVEAL using STEGO !!    ",font = "Helvetica 16 bold italic",fg="white",bg="black")
lab.place(relx=0.2,rely=0.2)

root.mainloop()

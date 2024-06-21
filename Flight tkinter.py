from tkinter import *
import tkinter as tk
from tkcalendar import DateEntry
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk


root=tk.Tk()
root.title('Flight Booking')
root.attributes('-fullscreen',True)
root.configure(bg='#daeaeb')



connection = mysql.connector.connect(
host='localhost',
user='root', 
password='mith@1122',
database="PieTkinter")

fn = StringVar()
ln = StringVar()
la = IntVar()
lm = StringVar()
tr = StringVar()

def insertData():

    fns = fn.get()
    lns = ln.get()
    las = la.get()
    lms = lm.get()

    c = connection.cursor()
    insert_query = "INSERT INTO PieTb(first_name, last_name, age, mob) VALUES (%s,%s,%s,%s)"
    vals = (fns,lns,las,lms)

    c.execute(insert_query,vals)
    connection.commit()
    print("Data inserted Successfuly")

    if(fns=="" or lns=="" or las=="" or lms==""):
        messagebox.showerror("Error","Please Enter all the values")



image=Image.open('flig.jpg')
img=image.resize((1370, 770))
my_img=ImageTk.PhotoImage(img)
label=Label(root, bd=0,image=my_img)
label.place(x= 0,y= 0)



lb1 = tk.Label(root,text="",bg='#2e9ba3',width=1000,height=20)
lb1.place(x= 0,y=0)

lb0 = tk.Label(root,text="Domestic Flight Booking",fg="white",font=("bold",40),bg="#2e9ba3")
lb0.place(x = 380,y = 30)

lb2 = tk.Label(root,text="",bg='white',height=35,width=150)
lb2.place(x = 150,y = 150)

c1 = tk.Checkbutton(root,text="One Way",fg="#2e9ba3",bg="white",font=("Comic Sans MS",10))
c1.place(x = 165,y = 165)

c2 = tk.Checkbutton(root,text="Round Trip",fg="#2e9ba3",bg= "white",border=5,font=("Comic Sans MS",10))
c2.place(x = 265,y = 165)

c3 = tk.Checkbutton(root,text="Multi city",fg="#2e9ba3",bg= "white",border=5,font=("Comic Sans MS",10))
c3.place(x = 370,y = 165)

lb3 = tk.Label(root,text="From",fg='#2e9ba3',bg="white",font=("bold",40))
lb3.place(x = 200,y= 250)

options = ["Nagpur","Ahmadnagar","Nasik","Amravati","Bhandara"]
click = StringVar()
click.set("Nagpur")

drop = OptionMenu(root,click,*options)
drop.place(x = 200,y = 350)

lb4 = tk.Label(root,text="To",fg='#2e9ba3',bg="white",font=("bold",40))
lb4.place(x = 450,y= 250)

options2 = ["Nagpur","Ahmadnagar","Nasik","Amravati","Bhandara"]
click2 = StringVar()
click2.set("Nasik")

drop2 = OptionMenu(root,click2,*options)
drop2.place(x = 460,y = 350)

lb5 = tk.Label(root,text="Departure",fg='#2e9ba3',bg="white",font=("bold",40))
lb5.place(x = 650,y= 250)  

cal = DateEntry(root, width=10, year=2024, month=5, day=28, background='#2e9ba3', foreground='black', borderwidth=20)
cal.place(x=660,y=350,width=180,height=30) 

lb6 = tk.Label(root,text="Travel",fg='#2e9ba3',bg="white",font=("bold",40))
lb6.place(x = 970,y= 250) 

options3 = ["Economy","Business","Primium Economy","First Class"]
click3 = StringVar()
click3.set("Economy")

drop3 = OptionMenu(root,click3,*options3)
drop3.place(x = 970,y = 350)

label_firstname = tk.Label(root, text="First Name:",fg='#2e9ba3', font=('bold',15), bg="white")
label_firstname.place(x = 200,y = 480)
entry_firstname = tk.Entry(root, font=('bold',15),background='white',fg="black",borderwidth=3,textvariable=fn)
entry_firstname.place(x = 330,y = 480)

label_lastname = tk.Label(root, text="Last Name:",fg='#2e9ba3', font=('bold',15), bg="white")
label_lastname.place(x = 200,y = 600)
entry_lastname = tk.Entry(root, font=('bold',15),background='white',fg="black",borderwidth=3,textvariable=ln)
entry_lastname.place(x = 330,y = 600)

label_age = tk.Label(root, text="Age:",fg='#2e9ba3', font=('bold',15), bg="white")
label_age.place(x = 600,y = 480)
entry_age = tk.Entry(root, font=('bold',15),background='white',fg="black",borderwidth=3,textvariable=la)
entry_age.place(x = 730,y = 480)

label_mob = tk.Label(root, text="Mobile No:",fg='#2e9ba3', font=('bold',15), bg="white")
label_mob.place(x = 600,y = 600)
entry_mob = tk.Entry(root, font=('bold',15),background='white',fg="black",borderwidth=3,textvariable=lm)
entry_mob.place(x = 730,y = 600)

b1 = tk.Button(root,text="Book",bg="#2e9ba3",fg="white",font=("bold",20),height=1,width=8,command=insertData)
b1.place(x = 1015,y = 525)

root.mainloop()



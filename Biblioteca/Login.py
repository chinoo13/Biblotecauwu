from tkinter import *
import tkinter

from Admin import *
from Estudiante import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("Bib.db")
c=conn.cursor()
main = Tk()
main.title('Ingresar')
main.geometry('1200x500')
main.resizable(False, False)
main.configure(background='#731414')
imagenL=PhotoImage(file="123.png")
lblImagen=Label(main,image=imagenL)
lblImagen.place(x=0,y=0)

def register(user,passwd,name,last_name):
    login=user.get()
    mdp=passwd.get()
    nom=name.get()
    prenom=last_name.get()
    cnt=0
    if login =='' or mdp =='' or nom=='' or prenom=='':
        messagebox.showerror("Error"," Porfavor llena todos los campos")
        return
    else:
        c.execute("""INSERT INTO User (login,mdp,nom,prenom,cnt,banned) VALUES(?,?,?,?,?,?)""",(login,mdp,nom,prenom,cnt,0))
        conn.commit()
        user.delete(0, END)
        passwd.delete(0, END)
        name.delete(0, END)
        last_name.delete(0, END)
        messagebox.showinfo("Éxito","Has sido registrado exitosamente !")
       

def clear(event):
    if username_box == main.focus_get() and username_box.get() == 'Nombre Usuario':
        username_box.delete(0, END)
    elif password_box == password_box.focus_get() and password_box.get() == '     ':
        password_box.delete(0, END)
 
def repopulate_defaults(event):
 
    if username_box != main.focus_get() and username_box.get() == '':
        username_box.insert(0, 'Nombre Usuario')
    elif password_box != main.focus_get() and password_box.get() == '':
        password_box.insert(0, '     ')

def login(*event):
 
    username = username_box.get()
    passwd = password_box.get()
    c.execute("""SELECT login,mdp,banned FROM User where login=? and mdp=?""",(username,passwd))
    wa=c.fetchone()
    if(username == "admin" and passwd == "admin"):  
        main.destroy()
        admin()
    elif wa:
        if wa[2]==1:
            messagebox.showerror("Error", "Usuario con Morosidad")    
        else:
            main.destroy()
            student(username,passwd)
    else:
        messagebox.showerror("Error","Contraseña o Usuario incorrectos")

rows = 0
while rows < 10:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1


Reg = Label(main,text="Registrar Estudiante",font=('arial 12'),bg="#bd829e",fg="black")
Reg.grid(row=1, column=1, sticky='NESW')

user = Label(main,text="Nombre Usuario",font=('arial 10'),bg="#bd829e",fg="black")
user.grid(row=2,column=0,sticky='NESW')
user_box = Entry(main)
user_box.grid(row=2,column=1,sticky='NESW')

passwd = Label(main,text="Contraseña",font=('arial 10'),bg="#bd829e",fg="black")
passwd.grid(row=3,column=0,sticky='NESW')
passwd_box = Entry(main,show="*")
passwd_box.grid(row=3,column=1,sticky='NESW')

name = Label(main,text="Nombre Estudiante",font=('arial 10'),bg="#bd829e",fg="black")
name.grid(row=4,column=0,sticky='NESW')
name_box = Entry(main)
name_box.grid(row=4,column=1,sticky='NESW')

last_name = Label(main,text="Rut",font=('arial 10'),bg="#bd829e",fg="black")
last_name.grid(row=5,column=0,sticky='NESW')
last_name_box = Entry(main)
last_name_box.grid(row=5,column=1,sticky='NESW')

btn_register = Button(main,text="Registrarse",command = lambda:register(user_box,passwd_box,name_box,last_name_box),bg="#F4C4BB")
btn_register.grid(row=7,column=1,sticky='NESW')
 
Log = Label(main,text="Iniciar sesión",font=('arial 12'),bg="#bd829e",fg="black")
Log.grid(row=1, column=8, sticky='NESW')
username_box = Entry(main)
username_box.insert(0, 'Nombre Usuario')
username_box.bind("<FocusIn>", clear)
username_box.bind('<FocusOut>', repopulate_defaults)
username_box.grid(row=2, column=8, sticky='NESW')
 
 
password_box = Entry(main, show='*')
password_box.insert(0, '     ')
password_box.bind("<FocusIn>", clear)
password_box.bind('<FocusOut>', repopulate_defaults)
password_box.bind('<Return>', login)
password_box.grid(row=3, column=8, sticky='NESW')
 

login_btn = Button(main, text='Ingresar', command=login,bg="#F4C4BB")
login_btn.bind('<Return>', login)
login_btn.grid(row=5, column=8, sticky='NESW')
 
 
main.mainloop()

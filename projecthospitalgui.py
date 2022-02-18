import tkinter
from tkinter import *

import pymysql
root=Tk()
root.geometry("1920x1080")
root.title("HOSPITAL MANAGEMENT BY IMRAN RAEENI")


def submit():
   
    con=pymysql.connect(host="localhost",user="root",password="",database="fina")
    cur=con.cursor()
    cur.execute("insert into final (name,mob,date,address) values(%s,%s,%s,%s)",(namept.get(),mobpt.get(),datept.get(),addpt.get()))
    con.commit()
    con.close()
    










f1=Frame(root,width=1920,height=100,bg="powderblue")
f1.pack(side=TOP)

name=Label(f1,text="HOSTIPAL MANAGEMENT ",font=("DejaVu Sans Mono",30),bg="powderblue")
name.place(x=500,y=20)




f2=Frame(root,width=950,height=500,bg="snow")
f2.place(y=100)



namelab=Label(f2,text="Name",font=("bold",20),bg="snow")
namelab.place(x=30,y=100)

moblab=Label(f2,text="MOBILE",font=("bold",20),bg="snow")
moblab.place(x=30,y=180)

datelab=Label(f2,text="DATE(y/m/d)",font=("bold",15),bg="snow")
datelab.place(x=30,y=260)

addlab=Label(f2,text="ADDRESS",font=("bold",20),bg="snow")
addlab.place(x=30,y=340)

appointmenttxt=Label(f2,text="Appointment ",font=("monaco",30))
appointmenttxt.place(x=280,y=20)

namept=Entry(f2,font=("arial",30))

namept.place(x=190,y=100)

mobpt=Entry(f2,font=("arial",30))

mobpt.place(x=190,y=180)

datept=Entry(f2,font=("arial",30))

datept.place(x=190,y=260)

addpt=Entry(f2,font=("arial",30))

addpt.place(x=190,y=340)


bookbtn=Button(f2,text="Book Appointment",font=("arial",25),fg="green",command=submit)
bookbtn.place(x=260,y=420)



f3=Frame(root,width=800,height=500,bg="snow")
f3.place(x=951,y=100)

logintxt=Label(f3,text="Log in ",font=("monaco",30))
logintxt.place(x=220,y=20)

gmailpt=Entry(f3,font=("arial",20))

gmailpt.place(x=130,y=130)

passpt=Entry(f3,font=("arial",20))

passpt.place(x=130,y=220)

loginbtn=Button(f3,text="Sign in",font=("arial",20),fg="green")
loginbtn.place(x=130,y=320)

forgetbtn=Button(f3,text="Forgett",font=("arial",20),fg="green")
forgetbtn.place(x=350,y=320)

f4=Frame(root,width=950,height=200,bg="lightblue")
f4.place(y=600)
ambnbtn=Button(f4,text="Ambulance",font=("arial",35),fg="green")
ambnbtn.place(x=50,y=70)
callnowbtn=Button(f4,text="Call Now",font=("arial",35),fg="green")
callnowbtn.place(x=500,y=70)





f5=Frame(root,width=800,height=200,bg="lightblue")
f5.place(x=951,y=600)


reviewtxt=Label(f5,text="Comment",fg="red",font=("monaco",35))
reviewtxt.place(x=20,y=10)
review=Text(f5,height=7,width=50)
review.place(x=20,y=75)

rvwbtn=Button(f5,text="submit",font=("arial",20),fg="green",command=submit)
rvwbtn.place(x=450,y=115)







root.mainloop()
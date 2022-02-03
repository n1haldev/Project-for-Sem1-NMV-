from tkinter import *
from tkinter.messagebox import showinfo,askyesno
from tkinter.simpledialog import askstring
import mailing as em
import TTT

def registration(a,b,c,d):
    f=open("UserDataBase.txt")
    content=(f.read().splitlines())
    fw=open("UserDataBase.txt","a")
    for m in content:
        if c!=d:
            showinfo("Incorrect Input","Password and Confirm Password is different!")
            break
        elif a in m:
            showinfo("Alert!","An account using the provided email already exists\n\tYou can try logging in!")
            break
        else:
            response=askyesno("Real Quick!","Would you like to enable 2FA and make your account more secure?")
            if response=="Yes":
                s="\n"+b+","+a+","+c+",2FA"
                fw.write(s)
                TTT.Gameon()
            else:
                s="\n"+b+","+a+","+c+",2FA"
                fw.write(s)
                TTT.Gameon()
def Login(a,b):
    f=open("UserDataBase.txt","r")
    content=(f.read()).splitlines()
    for m in content:
        if a in m:
            if b in m:
                
                if "2FA" in m:
                    authentication=em.two_FA(a,m[0:m.find(",")])
                    code=askstring("2FA confirmation","Please enter the 6-digit 2FA code that was mailed to you")
                    if code==authentication:
                        TTT.Gameon()

   
RorL=Tk()
RorL.title("Welcome to Tic Tac Toe game")
RorL.geometry("1500x1000")

rml=Label(RorL,text="Enter your email address:")
rnl=Label(RorL,text="Enter your name:")
rpl=Label(RorL,text="Enter your Password")
rcpl=Label(RorL,text="Confirm your Password")
rpe=Entry(RorL,width=30,show="*")
rcpe=Entry(RorL,width=30,show="*")
rme=Entry(RorL,width=30)
rne=Entry(RorL,width=30)
rml.place(x=400,y=200)
rme.place(x=400,y=225)
rnl.place(x=400,y=250)
rne.place(x=400,y=275)
rpl.place(x=400,y=300)
rpe.place(x=400,y=325)
rcpl.place(x=400,y=350)
rcpe.place(x=400,y=375)

lml=Label(RorL,text="Enter your email address:")
lml.place(x=750,y=200)
lme=Entry(RorL,width=30)
lme.place(x=750,y=225)
lpl=Label(RorL,text="Enter your Password")
lpl.place(x=750,y=250)
lpe=Entry(RorL,width=30,show="*")
lpe.place(x=750,y=275)

rb=Label(RorL,text="Register",width=30,height=5,bg="red")
lb=Label(RorL,text="Login",width=30,height=5,bg="red")                                      
register=Button(RorL,text="Register",width=10,height=2,bg="green",command=lambda:registration(rme.get(),rne.get(),rpe.get(),rcpe.get())) #mail#name#pass#confirmpass
login=Button(RorL,text="Login",width=10,height=2,bg="green",command=lambda:Login(lme.get(),lpe.get()))

register.place(x=400,y=400)
login.place(x=750,y=300)
rb.place(x=400,y=100)
lb.place(x=750,y=100)
RorL.mainloop()

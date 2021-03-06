from tkinter import *
from CenterLib import makecenter
from math import *
def clrAction():
    stringInOut.set("")
def inAction1():
    stringInOut.set(stringInOut.get()+"1")
def inAction2():
    stringInOut.set(stringInOut.get()+"2")
def inAction3():
    stringInOut.set(stringInOut.get()+"3")
def inAction4():
    stringInOut.set(stringInOut.get()+"4")
def inAction5():
    stringInOut.set(stringInOut.get()+"5")
def inAction6():
    stringInOut.set(stringInOut.get()+"6")
def inAction7():
    stringInOut.set(stringInOut.get()+"7")
def inAction8():
    stringInOut.set(stringInOut.get()+"8")
def inAction9():
    stringInOut.set(stringInOut.get()+"9")
def inAction0():
    stringInOut.set(stringInOut.get()+"0")
def inActionTru():
    stringInOut.set(stringInOut.get()+"-")
def inActionCham():
    stringInOut.set(stringInOut.get()+".")
def inActionCong():
    stringInOut.set(stringInOut.get()+"+")
def inActionNhan():
    stringInOut.set(stringInOut.get()+"*")
def inActionChia():
    stringInOut.set(stringInOut.get()+"/")
def inActionCan():
    stringInOut.set(stringInOut.get()+"sqrt")
def inActionNgoacMo():
    stringInOut.set(stringInOut.get()+"(")
def inActionNgoacDong():
    stringInOut.set(stringInOut.get()+")")
def inActionMu():
    stringInOut.set(stringInOut.get()+"pow")
def inActionAC():
    oldStr = stringInOut.get()
    if(oldStr[-1]=="t"): # for sqrt
        newStr = oldStr[:-4]
    elif (oldStr[-1]=="r"): # for Math error
        newStr = oldStr[:-10]
    else:
        newStr = oldStr[:-1] #Remove final character from string
    stringInOut.set(newStr)
def giaiAction():
    kq=""
    try:
        kq=eval(stringInOut.get(),{'sqrt': sqrt, 'pow': pow})
    except:
        kq="Math error"
    stringInOut.set(kq)
root=Tk()

stringInOut=StringVar("")

root.title("Caculator")
root.minsize(height=320,width=180)
root.resizable(height=False,width=False)
Entry(root,width=29,textvariable=stringInOut).grid(row=0)


frameButton1=Frame(root)
Button(frameButton1,text="1",font=("tahoma",16),width=4,command=inAction1).pack(side=LEFT)
Button(frameButton1,text="2",font=("tahoma",16),width=4,command=inAction2).pack(side=LEFT)
Button(frameButton1,text="3",font=("tahoma",16),width=4,command=inAction3).pack(side=LEFT)
frameButton1.grid(row=1,columnspan=3)

frameButton2=Frame(root)
Button(frameButton2,text="4",font=("tahoma",16),width=4,command=inAction4).pack(side=LEFT)
Button(frameButton2,text="5",font=("tahoma",16),width=4,command=inAction5).pack(side=LEFT)
Button(frameButton2,text="6",font=("tahoma",16),width=4,command=inAction6).pack(side=LEFT)
frameButton2.grid(row=2,columnspan=3)

frameButton3=Frame(root)
Button(frameButton3,text="7",font=("tahoma",16),width=4,command=inAction7).pack(side=LEFT)
Button(frameButton3,text="8",font=("tahoma",16),width=4,command=inAction8).pack(side=LEFT)
Button(frameButton3,text="9",font=("tahoma",16),width=4,command=inAction9).pack(side=LEFT)
frameButton3.grid(row=3,columnspan=3)

frameButton4=Frame(root)
Button(frameButton4,text="sqrt",font=("tahoma",16),width=4,command=inActionCan).pack(side=LEFT)
Button(frameButton4,text="0",font=("tahoma",16),width=4,command=inAction0).pack(side=LEFT)
Button(frameButton4,text=".",font=("tahoma",16),width=4,command=inActionCham).pack(side=LEFT)
frameButton4.grid(row=4,columnspan=3)


frameButton5=Frame(root)
Button(frameButton5,text="(",font=("tahoma",16),width=4,command=inActionNgoacMo).pack(side=LEFT)
Button(frameButton5,text=")",font=("tahoma",16),width=4,command=inActionNgoacDong).pack(side=LEFT)
Button(frameButton5,text="AC",font=("tahoma",16),width=4,command=inActionAC).pack(side=LEFT)
frameButton5.grid(row=5,columnspan=3)

frameButton6=Frame(root)
Button(frameButton6,text="+",font=("tahoma",16),width=2,command=inActionCong).pack(side=LEFT)
Button(frameButton6,text="-",font=("tahoma",16),width=2,command=inActionTru).pack(side=LEFT)
Button(frameButton6,text="*",font=("tahoma",16),width=2,command=inActionNhan).pack(side=LEFT)
Button(frameButton6,text="/",font=("tahoma",16),width=2,command=inActionChia).pack(side=LEFT)
Button(frameButton6,text="=",font=("tahoma",16),width=2,padx=3, command=giaiAction).pack(side=LEFT)
frameButton6.grid(row=6,columnspan=3)

button=Button(root,text="clr",font=("tahoma",16),width=12, command=clrAction).grid(row=7)

makecenter(root)
root.mainloop()

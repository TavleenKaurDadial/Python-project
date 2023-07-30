

from recharge import *
from DTH import *
from travel import *
from gas import *
from tkinter import *
import webbrowser as wb
from PIL import ImageTk,Image



root=Tk()
root.title("Paytm Tavleen")


bg_old1=Image.open('images/bg.png')
bg_resized=bg_old1.resize((12000,400))
bg=ImageTk.PhotoImage(bg_resized)
bg_label=Label(root,image=bg)
bg_label.place(x=0,y=100)
def signin():
    wb.open("https://accounts.paytm.com/register#!/signup")


oldhead=Image.open('images/header.png')
resizedhead=oldhead.resize((350,50))
header=ImageTk.PhotoImage(resizedhead)

label_head=Label(root,image=header)
label_head.place(x=20,y=15)



img_old5=Image.open('images/signIn.png')
img_resized5=img_old5.resize((250,50))
img_sign=ImageTk.PhotoImage(img_resized5)

label_sign=Label(image=img_sign)
b1=Button(root,image=img_sign,command=signin,borderwidth=0)
b1.place(x=1080,y=20)




img_old1=Image.open('images/phone.png')
img_resized=img_old1.resize((150,150))
img_recharge=ImageTk.PhotoImage(img_resized)

label_re=Label(image=img_recharge)
b1=Button(root,image=img_recharge,command=New_Window,borderwidth=0)
b1.place(x=50,y=150)
l1=Label(root,text="Prepaid/Postpaid",foreground="navy blue",background="light blue",
         font=("Bahnschrift SemiLight SemiConde",20))
l1.place(x=40,y=320)



img_old2=Image.open('images/Satantenna.png')
img_resized2=img_old2.resize((150,150))
img_dth=ImageTk.PhotoImage(img_resized2)

label_dth=Label(image=img_dth)
b2=Button(root,image=img_dth,command=New_DTH,borderwidth=0)
b2.place(x=300,y=150)
l2=Label(root,text="DTH",foreground="navy blue",background="light blue",
         font=("Bahnschrift SemiLight SemiConde",20))
l2.place(x=350,y=320)



img_old3=Image.open('images/metro.png')
img_resized3=img_old3.resize((150,150))
img_metro=ImageTk.PhotoImage(img_resized3)

label_metro=Label(image=img_metro)
b3=Button(root,image=img_metro,command=New_Travel,borderwidth=0)
b3.place(x=550,y=150)
l3=Label(root,text="Metro",foreground="navy blue",background="light blue",
         font=("Bahnschrift SemiLight SemiConde",20))
l3.place(x=600,y=320)



img_old4=Image.open('images/gas.png')
img_resized4=img_old4.resize((150,150))
img_gas=ImageTk.PhotoImage(img_resized4)

label_gas=Label(image=img_gas)
b2=Button(root,image=img_gas,command=New_Gas,borderwidth=0)
b2.place(x=800,y=150)
l2=Label(root,text="Pay Gas Bill",foreground="navy blue",background="light blue",
         font=("Bahnschrift SemiLight SemiConde",20))
l2.place(x=810,y=320)







root.mainloop()

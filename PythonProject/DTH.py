
from tkinter import *
import qrcode as qr
from PIL import ImageTk,Image

def New_DTH():
    Window =Toplevel()
    Window.title("DTH")
    global img_dth1,img_dth2
    l1=Label(Window,text="Recharge DTH or TV",foreground="black",font=("Calibri",25))
    l1.place(x=50,y=0)
    

    l2=Label(Window,text="DTH Operator",foreground='blue',
             font=("Calibri",15))
    l2.place(x=30,y=90)
    e2=Entry(Window,font=("Calibri",15),width=30)
    e2.place(x=30,y=120)

    l3=Label(Window,text="Registered Mobile No",foreground='blue',
             font=("Calibri",15))
    l3.place(x=30,y=180)
    e3=Entry(Window,font=("Calibri",15),width=30)
    e3.place(x=30,y=210)

    l4=Label(Window,text="Amount",foreground='blue',
             font=("Calibri",15))
    l4.place(x=30,y=260)
    e4=Entry(Window,font=("Calibri",15),width=30)
    e4.place(x=30,y=300)

    l5=Label(Window,text="",font=("Calibri",15))
    l5.place(x=50,y=350)

    def storeGasDet():
        
        op=e2.get()
        num=e3.get()
        amount=e4.get()
        if(e2.get()=="" and e3.get()=="" and e4.get()=="" ):
            l5["text"]="Please enter the above details"
        elif(e2.get()=="" or e3.get()=="" or e4.get()=="" ):
            l5["text"]="Please enter the above details"
        else:
            Window2=Toplevel()
            Window2.title("QR Code")
            l7=Label(Window2,text="Scan the QR Code",font=("Calibri",20))
            l7.place(x=30,y=50)
            global img_qr
            
            img=qr.make("Payment Successful!")
            img.save("qr.png")

            img_qr=ImageTk.PhotoImage(Image.open("qr.png"))
            lqr=Label(Window2,image=img_qr)
            lqr.place(x=30,y=100)

            f=open("PaytmData.txt","+a")
            f.writelines(["\n Dth Operator: ",op,"\n Mobile No:",num,"\n Amount: ",amount,"\n _______________________________________________________________________________________________"])
            f.close()
        
    
    b1=Button(Window,text="Proceed to Pay",foreground="blue",background="light blue",
                    font=("Calibri",20),command=storeGasDet)
    b1.place(x=70,y=390)
    l6=Label(Window,text="Select DTH Operator",font=("Calibri",25))
    l6.place(x=30,y=490)


    
    def storeDTH(txt):
        e2.delete(0,END)
        e2.insert(0,txt)
    
    img_old1=Image.open('images/dth1.png')
    img_resized1=img_old1.resize((150,100))
    img_dth1=ImageTk.PhotoImage(img_resized1)

    img_old2=Image.open('images/dth2.png')
    img_resized2=img_old2.resize((150,100))
    img_dth2=ImageTk.PhotoImage(img_resized2)


    b2=Button(Window,command=lambda:storeDTH("Airtel Digital TV Recharge"),image=img_dth1,borderwidth=0)
    b2.place(x=40,y=550)

    b3=Button(Window,command=lambda:storeDTH("Tata Play Recharge"),image=img_dth2,borderwidth=0)
    b3.place(x=300,y=550)


    
   
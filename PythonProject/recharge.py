
from tkinter import *
from PIL import ImageTk,Image
import qrcode as qr
def New_Window():
    Window =Toplevel()
    Window.title("Mobile Recharge")
    global img_recharge1,img_recharge2
    l1=Label(Window,text="Recharge or Pay Mobile Bill",foreground="black",font=("Calibri",25))
    l1.place(x=50,y=0)
    
    r=StringVar()
    r.set("Prepaid")
    r1=Radiobutton(Window,text="Prepaid",foreground="blue",font=("Calibri",20),variable=r,value="Prepaid")
    r1.place(x=30,y=40)
    r2=Radiobutton(Window,text="Postpaid",foreground="blue",font=("Calibri",20),variable=r,value="Postpaid")
    r2.place(x=200,y=40)




    l2=Label(Window,text="Operator",foreground='blue',
             font=("Calibri",15))
    l2.place(x=30,y=90)
    e2=Entry(Window,font=("Calibri",15),width=30)
    e2.place(x=30,y=120)

    l3=Label(Window,text="Mobile Number",foreground='blue',
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



    def storeRechargeDet():
        
        mode=r.get()
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
            f.writelines(["\n Mode: ",mode,"\n Operator: ",op,"\n Mobile No:",num,"\n Amount: ",amount,"\n _______________________________________________________________________________________________"])
            f.close()
        
    
    b1=Button(Window,text="Proceed to Pay",foreground="blue",background="light blue",
                    font=("Calibri",20),command=storeRechargeDet)
    b1.place(x=70,y=390)
    l6=Label(Window,text="Select An Operator",font=("Calibri",25))
    l6.place(x=30,y=490)


    
    def storeRecharge(txt):
        e2.delete(0,END)
        e2.insert(0,txt)
    
    img_old1=Image.open('images/recharge1.png')
    img_resized1=img_old1.resize((150,100))
    img_recharge1=ImageTk.PhotoImage(img_resized1)

    img_old2=Image.open('images/recharge2.png')
    img_resized2=img_old2.resize((150,100))
    img_recharge2=ImageTk.PhotoImage(img_resized2)


    b2=Button(Window,command=lambda:storeRecharge("Airtel Recharge"),image=img_recharge1,borderwidth=0)
    b2.place(x=40,y=550)

    b3=Button(Window,command=lambda:storeRecharge("Jio Recharge"),image=img_recharge2,borderwidth=0)
    b3.place(x=300,y=550)

    
    
    
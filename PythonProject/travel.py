
from tkinter import *
import qrcode as qr
from PIL import ImageTk,Image
def New_Travel():
    global img_mum,img_hyd
    Window =Toplevel()
    Window.title("Metro")
    

    l1=Label(Window,text="Metro",foreground="black",font=("Calibri",25))
    l1.place(x=50,y=0)
    

    l2=Label(Window,text="Metro",foreground='blue',
             font=("Calibri",15))
    l2.place(x=30,y=80)
    e2=Entry(Window,text="",font=("Calibri",15),width=30)
    e2.place(x=30,y=110)

    l3=Label(Window,text="Card Number",foreground='blue',
             font=("Calibri",15))
    l3.place(x=30,y=170)
    e3=Entry(Window,font=("Calibri",15),width=30)
    e3.place(x=30,y=200)

    l4=Label(Window,text="Amount",foreground='blue',
             font=("Calibri",15))
    l4.place(x=30,y=260)
    e4=Entry(Window,font=("Calibri",15),width=30)
    e4.place(x=30,y=290)

    l5=Label(Window,text="",font=("Calibri",15))
    l5.place(x=50,y=340)

    def storeMetroDet():
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
            
            img=qr.make("Payment Successful!",)
            img.save("qr.png")

            img_qr=ImageTk.PhotoImage(Image.open("qr.png"))
            lqr=Label(Window2,image=img_qr)
            lqr.place(x=30,y=100)
            f=open("PaytmData.txt","+a")
            f.writelines(["\n Metro: ",op,"\n Card number:",num,"\n Amount: ",amount,"\n _______________________________________________________________________________________________"])
            f.close()
        
    b1=Button(Window,text="Proceed to Pay",foreground="blue",background="light blue",
                    font=("Calibri",20),command=storeMetroDet)
    b1.place(x=70,y=390)

    l6=Label(Window,text="Select Metro",font=("Calibri",25))
    l6.place(x=30,y=490)

    
        

    def storeMetro(txt):
        e2.delete(0,END)
        e2.insert(0,txt)
    
    mumbai=Image.open('images/mum_metro.png')
    mum_resized=mumbai.resize((200,100))
    img_mum=ImageTk.PhotoImage( mum_resized)

    hyd=Image.open('images/hyd_metro.png')
    hyd_resized=hyd.resize((150,100))
    img_hyd=ImageTk.PhotoImage( hyd_resized)


    mumbutton=Button(Window,command=lambda:storeMetro("Maha Mumbai Metro"),image=img_mum,borderwidth=0)
    mumbutton.place(x=40,y=550)

    hydbutton=Button(Window,command=lambda:storeMetro("Hyderabad Metro"),image=img_hyd,borderwidth=0)
    hydbutton.place(x=300,y=550)

    
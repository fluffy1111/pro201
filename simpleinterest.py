from tkinter import *
window=Tk()

window.title("GUI")
window.geometry("380x400")
window.configure(bg='lightcyan')

result_frame = LabelFrame(window,text="Result", bg = "grey", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20, y=300)

Showlabel=Label(result_frame,text="Your result will be displayed here", bg="grey", font=("Calibri", 12), width=55)
Showlabel.place(x=20,y=20)
Showlabel.pack()

userinfo=Entry(window, text="", bd=2, width=22)
userinfo.place(x=20,y=20)
userinfo.pack()

message=Label(result_frame, text="Intrest an is."+str(p)+" at rste of interest "+str(r)+"is for "+str(t)" years is ks."+str(interest), bg = "grey", font=("Calibri", 12), width=55)
message.place(x=20,y=20)
message.pack()

def calculate_interest():
    p= float(principle.get())
    r= float(rate.get())
    t= float(time.get())
    i= float(p*r*t)/100
    interest= round(1, 2)

Showlabel.destroy()
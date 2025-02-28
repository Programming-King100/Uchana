from tkinter import *
import tkinter.font as font
root = Tk()
root.geometry("500x300")
root.title("Uchana weather Magic")


CandF=Label(root,text="Celsius -> Fahrenheit",font=font.Font(size=20),fg="Purple")
CandF.grid(row=4,column=4,columnspan=9)

def convert():
    temp_celcius=jaeb.get()
    if temp_celcius.replace('.','').isdigit():
        temp_fah=(float(temp_celcius)*9/5)+32
        mT.config(text=''+str(temp_fah)+'°F')
   
Alachbutton=Button(root,text="Translate",command=convert)
Alachbutton.grid(row=7,column=4,columnspan=9)

tctf=Label(root,text="Translate Celsius to Fahrenheit:")
tctf.grid(row=5,column=4,)

jaeb = Entry(root,width=30)
jaeb.grid(row=5,column=5)

jael = Label(root,text="Temperature in Fahrenheit")
jael.grid(row=6,column=4)

mT = Label(root,text="")
mT.grid(row=6,column=5)
root.mainloop()






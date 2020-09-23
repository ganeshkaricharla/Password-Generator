from tkinter import *
import pwdgenerator ,pwdvalidation

def generatenow():
    size=int(Entry_Name.get())
    password=pwdgenerator.generatePasswordws(size)
    Entry_Password.delete(0,100)
    Entry_Password.insert(0,password)
    report=pwdvalidation.validation(password)
    Label_Uppercase=Label(root,text="Uppercase Check                ::",justify=LEFT)
    Label_Lowercase=Label(root,text="Lowercase Check                ::",justify=LEFT)
    Label_digit=Label(root,    text="Digit Check                    ::",justify=LEFT)
    Label_SpclChar=Label(root, text="Special Character Check        ::",justify=LEFT)
    Label_Length=Label(root,   text="Length Check                   ::",justify=LEFT)
    Label_Recomnd=Label(root,  text="Recommended                    ::",justify=LEFT)

    Label_Uppercaser=Label(root,text=report[0],justify=LEFT)
    Label_Lowercaser=Label(root,text=report[1],justify=LEFT)
    Label_digitr=Label(root,    text=report[2],justify=LEFT)
    Label_SpclCharr=Label(root, text=report[3],justify=LEFT)
    Label_Lengthr=Label(root,   text=report[4],justify=LEFT)
    Label_Recomndr=Label(root,  text=report[5],justify=LEFT)

    

    Label_Uppercase.grid(row=7,column=0)
    Label_Lowercase.grid(row=8,column=0)
    Label_digit.grid(row=9,column=0)
    Label_SpclChar.grid(row=10,column=0)
    Label_Length.grid(row=11,column=0)
    Label_Recomnd.grid(row=12,column=0)

    Label_Uppercaser.grid(row=7,column=1)
    Label_Lowercaser.grid(row=8,column=1)
    Label_digitr.grid(row=9,column=1)
    Label_SpclCharr.grid(row=10,column=1)
    Label_Lengthr.grid(row=11,column=1)
    Label_Recomndr.grid(row=12,column=1)



root=Tk()
root.geometry("700x600")
#create the components
Label_Head=Label(root,text="Password Generator and Validator",font="none 30 bold",fg="white",bg="#ad3654",padx=25,pady=20)
Label_subHead=Label(root,text="Check your Password Strength and Make a New",font="none 10 italic",fg="#ad3654",bg="#8cde90",padx=210)
Label_Name=Label(root,text="Enter The Length  ",font="none 30 bold",fg="white",bg="#21b59a",padx=185,pady=20)
Entry_Name=Entry(root,font="none 30 bold",fg="#c5bcd1",bg="white",width=32)
Button_Generate=Button(root,text="Generate Password",font="none 20 bold",fg="black",bg="#EDDF21",padx=215,command=generatenow)
Entry_Password=Entry(root,font="none 30 bold",fg="#c5bcd1",bg="white",width=32)
Label_Author=Label(root,text="Made by Ganesh",font="none 15 bold")

#show the components
Label_Head.grid(row=0,column=0,columnspan=2)
Label_subHead.grid(row=1,column=0,columnspan=2)
Label_Name.grid(row=2,column=0,columnspan=2)
Entry_Name.grid(row=3,column=0,columnspan=2)
Button_Generate.grid(row=4,column=0,columnspan=2)
Entry_Password.grid(row=5,column=0,columnspan=2)
Label_Author.grid(row=13,column=0,columnspan=2)
root.mainloop()
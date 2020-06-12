''' Random Password Generator '''

from tkinter import *
import string  #To use functions string methods
import time    #To delay the result after button being pressed
import random  #To generate random passwords from a string

def copy(event):
    data=event.widget.cget('text')
    root.clipboard_clear()  #clears clipboard
    root.clipboard_append(data) #Append New Value To Clip Board

def enter(event):
    global showresult
    showresult.config(bg='black',fg='red')

def leave(event):
    global showresult
    showresult.config(bg='black',fg='gold')

def generate():
    global f4,showresult #Used these global variables

    f4.destroy()
    
    if opted_value.get()=='Alphabetical Only':
        finalstr=string.ascii_lowercase+string.ascii_uppercase
        length=slider.get()
        pswd=''
        final=pswd.join(random.choices(finalstr,k=length))
        
        f4=Frame(root,padx=5,pady=2)
        pswdgen=Label(f4,text='Password Generated',font='comicsansms 12 bold')
        pswdgen.pack()
        time.sleep(1)
        pswd=Label(f4,text='Password:',font='comicssansms 12 bold')
        pswd.pack(side=LEFT)
        showresult=Label(f4,text=final,bg='black',fg='gold',font='lucida 12 bold',padx=5)
        showresult.pack()
        showresult.bind('<Button-1>',copy)
        showresult.bind('<Enter>',enter)
        showresult.bind('<Leave>',leave)
        f4.pack()

    elif opted_value.get()=='Alphanumerical':
        alphanumpswd=string.ascii_lowercase+string.ascii_uppercase+string.digits
        length=slider.get()
        pswd=''
        final=pswd.join(random.choices(alphanumpswd,k=length))

        f4=Frame(root,padx=5,pady=2)
        pswdgen=Label(f4,text='Password Generated',font='comicsansms 12 bold')
        pswdgen.pack()
        time.sleep(1)
        pswd=Label(f4,text='Password:',font='comicssansms 12 bold')
        pswd.pack(side=LEFT)
        showresult=Label(f4,text=final,bg='black',fg='gold',font='lucida 12 bold',padx=5)
        showresult.pack()
        showresult.bind('<Button-1>',copy)
        showresult.bind('<Enter>',enter)
        showresult.bind('<Leave>',leave)
        f4.pack()

    else:
        specialpswd=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
        length=slider.get()
        pswd=''
        final=pswd.join(random.choices(specialpswd,k=length))

        f4=Frame(root,padx=5,pady=2)
        pswdgen=Label(f4,text='Password Generated',font='comicsansms 12 bold')
        pswdgen.pack()
        time.sleep(1)
        pswd=Label(f4,text='Password:',font='comicssansms 12 bold')
        pswd.pack(side=LEFT)
        showresult=Label(f4,text=final,bg='black',fg='gold',font='lucida 12 bold',padx=5)
        showresult.pack()
        showresult.bind('<Button-1>',copy)
        showresult.bind('<Enter>',enter)
        showresult.bind('<Leave>',leave)
        f4.pack()
        

''' Main Program '''

root=Tk()
root.title('Password Generator')
root.geometry('500x510')
root.wm_iconbitmap('Images/icon.ico')
root.config(bg='#019031')   #To give the bg color to GUI window

#Heading
head=Label(text='Random Password Generator',font='Helvetica 17 bold',bg='white',fg='black',padx=10,pady=10,relief=SUNKEN)
head.pack(pady=10)

#To choose the type of password:
opted_value=StringVar()
opted_value.set('Alphabetical Only')

f1=Frame(root,padx=15,pady=18)
l1=Label(f1,text='Choose the type of password:',font='lucida 13 bold')
l1.pack(anchor='w',pady=10)
pswdtype_name=['Alphabetical Only','Alphanumerical','Alphanumerical + Special_Characters']
pswdvalue=['Alphabetical Only','Alphanumerical','Alphanumerical + Special_Characters']
for i in range(3):
    radio_btn=Radiobutton(f1,text=pswdtype_name[i],variable=opted_value,value=pswdvalue[i],font='consolas 10')
    radio_btn.pack(anchor='w')
f1.pack(fill=X,padx=25,pady=5)


#To select the length of password:
f2=Frame(root,pady=10)
l2=Label(f2,text='Choose the size of password:',font='Arial 13 bold')
l2.pack()
slider=Scale(f2,from_=1,to=24,orient=HORIZONTAL,length=300,relief=RIDGE,troughcolor='black',width=20,fg='black',bg='coral')
slider.pack(padx=35,pady=10)
f2.pack(fill=X,pady=10,padx=25)

#Button to generate password
f3=Frame(root)
submitbtn=Button(f3,text='Generate',font='lucida 13 bold',command=generate) 
submitbtn.pack()
f3.pack(pady=15)

#Declared some variables so that we can use or destroy them in different functions:
f4=Frame()
showresult=Label()

root.mainloop()

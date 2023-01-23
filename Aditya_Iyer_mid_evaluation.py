from tkinter import *
from tkinter.filedialog import asksaveasfile
root=Tk()
style=["Helvetica","Times","Jokerman"]
size=[12,14,16,18,20,24,26]

def mybold():
    
    mytext.config(font='Times 15 bold')

    
    
    
    
    
def myitalics():
    
    
    mytext.config(font='italic')
    
    
    
def myunder():
    mytext.config(font='Times 15 underline')
    

def mysave():
    content=mytext.get('1.0','end-1c')
    files=[('Text document','*.txt')]
    f=asksaveasfile(initialfile="adi.txt",defaultextension=".txt",filetypes=files)
    f.write(content)
    f.close()
           
                    
    
    
    
def mychange():
    text=select.get()
    sz=s.get()
    mytext.config(font=(text,int(sz)))

    
mytext=Text(root,width=60,height=30,padx=5,pady=5)
mytext.grid(row=1,column=0,columnspan=8000)
bold=Button(root,text='BOLD',command=mybold)
italics=Button(root,text='ITALICS',command=myitalics)
under=Button(root,text='UNDERLINE',command=myunder)
save=Button(root,text='SAVE',command=mysave)
bold.grid(row=0,column=0)
italics.grid(row=0,column=1)
under.grid(row=0,column=2)
save.grid(row=0,column=3)
select=StringVar()
select.set("FONT STYLE")

font_drop=OptionMenu(root,select,*style)
font_drop.grid(row=0,column=4)
change=Button(root,text='Change font',command=mychange)
change.grid(row=0,column=5)
s=StringVar()
s.set('Size')
size_drop=OptionMenu(root,s,*size)
size_drop.grid(row=0,column=6)





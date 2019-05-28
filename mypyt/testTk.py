from tkinter import *
root = Tk()

def hell():
    print('hello')

bt1=Button(root,text='click me',width=30,height=5,bg='white',fg='black',
           command=hell)

bt1.pack()
root.mainloop()


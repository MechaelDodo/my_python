import tkinter #as tk

class myMain(tkinter.Frame):
    def __init__(self,root):
        super().__init__(root)  #передаем root в базовый класс Frame
        self.init_myMaint()

    def init_myMaint(self):
        myToolbar=tkinter.Frame(bg='#00BFFF',bd=4)
        myToolbar.pack(side=tkinter.TOP, fill=tkinter.X)    #закрепляет в верхней части окна и растягивает по горизонтали

        #self.add_img=tkinter.PhotoImage(file='E:/W0KWxB7YhDI.jpg')
        myButton_openChild=tkinter.Button(myToolbar, text='Добавить позицию',
                                          command=self.open_myChild(), bg='#00FFFF',
                                          bd=2, compound = tkinter.TOP)#, image = self.add_img)
        myButton_openChild.pack(side = tkinter.LEFT)
        

    def open_myChild(self):
        myChild()       ###
        

class myChild(tkinter.Toplevel):
    def __init__(self):
        super().__init__()      ###root
        self.init_myChild()

    def init_myChild(self):
        self.title('Добавить доходы\расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        
        self.grab_set()     #перехватывает все события, происходящие в приложении 
        self.focus_set()    #захватывает и удерживает фокус
        



if __name__ == '__main__':        #если скрипт выполняется как основная программа, то он запустится,если импортируется, то нет
    myRoot = tkinter.Tk()
    myApp = myMain(myRoot)
    myApp.pack()
    myRoot.title('My Main Page')
    myRoot.geometry('650x450+500+200')
    myRoot.resizable(False, False)
    myRoot.mainloop()
        
    

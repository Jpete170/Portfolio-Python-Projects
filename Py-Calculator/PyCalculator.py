from tkinter import *

#Calculator Frame
def Calculator(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)

    return storeObj

#Creating a Button
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)

    return storeObj


#The App Itself
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Python Calculator")

        #Display Widget
        display = StringVar() 
        Entry(self, relief=RIDGE, textvariable=display, justify='right', bd=30, bg='powder blue').pack(side=TOP, expand=YES, fill=BOTH)

        #Clear Button
        for clearButton in (['C']):
            erase = Calculator(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda storeObj=display, q=ichar: storeObj.set(''))
        
        #Adding Numbers and Symbols
        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = Calculator(self, TOP)
            for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda storeObj=display, q=iEquals: storeObj.set(storeObj.get() + q))

        #Equal Button
        EqualButton = Calculator(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
                                                            
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
            
                                    (storeObj.get() + s))
    #Calculator Function
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")

#Start the GUI
if __name__ == '__main__':
    app().mainloop()
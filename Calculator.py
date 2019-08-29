from tkinter import *

class Calculator(Frame): #Here Create the class and call the Frame to use all methods in this Frame
    def __init__(self):#self means if I'm create object from class then use self to make name this objects
        Frame.__init__(self, bg = 'Purple')#Here just make the background color like Purple
        self.option_add('*font', 'arial 25 bold' )#font size & * to apply in everything
        self.pack(expand = YES , fill = BOTH)#To make expand of Frame and BOTH means for x&y
        self.master.title('Calculator')#To make the tkinter name Like Calculator

        display = StringVar()#It's From String type and allowed the user to write on screen
        obj = Entry(self, relief = RIDGE , textvariable = display, justify = 'right',
                      bd = 20, bg = 'Light Gray', width = 20)
        """Create varibale obj and take the Entry method to create the screen and show up self class
        justify="right" to start the writing from right to left, bd= 20 make the border size,background is blue and width=20"""
        obj.pack(side = TOP, expand=YES, fill=BOTH)#to set location

#C
        clearbutton = Button(self, text = 'C' ,bg ='Purple' , bd = 2,
                           command = lambda clear = display: clear.set(" "))#Object clearbutton from class Button
        clearbutton.pack(side = TOP, expand = YES , fill = BOTH)

#1234567890+-*/.
        for exp in("987/", "456*", "123-", "0.+"):
            frame = Frame(self, bd = 2 , bg = 'Purple')#background
            frame.pack(side = TOP, expand = YES, fill = BOTH)
            for char in exp :
                butt = Button(frame, text = char, bg = 'Thistle',
                              command = lambda stored = display, ch = char: stored.set(stored.get()+ ch))#in every self it's the parent of frame
                butt.pack(side = LEFT , expand = YES, fill = BOTH)

#=
        equal = Button(self, text = '=' , bd = 2, bg= 'Thistle' ,
                       command = lambda a = display: evaluate(a))
        equal.pack(side = TOP, expand = YES , fill = BOTH)

def evaluate(stored):
    try:
        stored.set(eval(stored.get()))
    except:
        stored.set('ERROR')

Calculator().mainloop() #Still running until click x to close the window

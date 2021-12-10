from tkinter import *                   # It is a standard Python interface to the Tk GUI toolkit shipped with Python.
from tkinter.messagebox import *        # 'messagebox' is used to show the error to the user if any is occuring.
import math as m                        # It is used to perform mathematical calculations.

# Defining font details.

font_type=('verdana', 15 , 'bold')

# Defining the clear function to delete single expresion from the text field.

def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 1]
    textField.delete(0, END)
    textField.insert(0, ex)

# Defining the all clear function to delete the entire expresion from the text field.

def all_clear():
    textField.delete(0,END)

# Function to click the equal button.

def click_btn_function(event):
    digit = event.widget
    text = digit['text']
    
    if text == '=':
        try:
            expression=textField.get()
            answer=eval(expression)
            textField.delete(0,END)
            textField.insert(0,answer)
        except Exception as error:
            print("Error....",error)
            showerror("Error....",error)
        return
    
    textField.insert(END,text)

# Creating a window.

window=Tk()

# Giving a tittle to the window.

window.title('Suvro-Calculator')

# Defining heading for the calculator.

heading = Label(window, text='Suvro-Calculator', font=font_type,)
heading.pack()

# Defining text field for the calculator.

textField = Entry(window, font = font_type, justify = CENTER)
textField.pack(side = TOP, pady =10, fill = X, padx =10,)

# Defining the frame for the buttons of the calculator.

buttonFrame = Frame(window)
buttonFrame.pack(side = TOP)

digit = 1

# Loop for creating and binding the buttons(1-9).

for i in range (0,3):
    for j in range(0,3):
        button = Button(buttonFrame, text= str(digit), font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, activebackground = 'green', activeforeground = 'white')
        button.grid(row=i,column=j)
        digit = digit+1
        button.bind('<Button-1>',click_btn_function)

# Creating and binding the zero button. / (<Button-1> - Refers to the left click of the mouse).
      
zeroButton =  Button(buttonFrame, text= '0', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
zeroButton.grid(row=3, column=0)
zeroButton.bind('<Button-1>',click_btn_function)

# Creating and binding the point button.

pointButton =  Button(buttonFrame, text= '.', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
pointButton.grid(row=3, column=1)
pointButton.bind('<Button-1>',click_btn_function)

# Creating and binding the equal button.

equalButton =  Button(buttonFrame, text= '=', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5,
activebackground = 'orange', activeforeground = 'white')
equalButton.grid(row=3, column=2)
equalButton.bind('<Button-1>',click_btn_function)

# Creating and binding the plus button.

plusButton =  Button(buttonFrame, text= '+', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
plusButton.grid(row=0, column=3)
plusButton.bind('<Button-1>',click_btn_function)

# Creating and binding the minus button.

minusButton =  Button(buttonFrame, text= '-', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
minusButton.grid(row=1, column=3)
minusButton.bind('<Button-1>',click_btn_function)

# Creating and binding the multiply button.

multiplyButton =  Button(buttonFrame, text= '*', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
multiplyButton.grid(row=2, column=3)
multiplyButton.bind('<Button-1>',click_btn_function)

# Creating and binding the divide button.

divideButton =  Button(buttonFrame, text= '/', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
divideButton.grid(row=3, column=3)
divideButton.bind('<Button-1>',click_btn_function)

# Creating and binding the clear button.

clearButton =  Button(buttonFrame, text= '<--', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white' , command = clear)
clearButton.grid(row=4, column=0)

# Creating and binding the all clear button.

allclearButton =  Button(buttonFrame, text= 'AC', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white', command = all_clear)
allclearButton.grid(row=4, column=1)

# Take response from enter button function.

def enterClick(event):
    e = Event()
    e.widget = equalButton
    click_btn_function(e)

textField.bind('<Return>', enterClick)

# Defining the scientific frame for the buttons of the calculator.

scientificFrame = Frame(window)

# Creating the square root (√) button.

squarerootButton = Button(scientificFrame, text= '√', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
squarerootButton.grid(row=0, column=0)

# Creating the power (^) button.

powerButton = Button(scientificFrame, text= '^', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
powerButton.grid(row=0, column=1)

# Creating the factorial (!) button.

factorialButton = Button(scientificFrame, text= 'x!', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
factorialButton.grid(row=0, column=2)

# Creating the radian button.

radianButton = Button(scientificFrame, text= 'toRad', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
radianButton.grid(row=0, column=3)

# Creating the degree button.

degreeButton = Button(scientificFrame, text= 'toDeg', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
degreeButton.grid(row=0, column=4)

# Creating the sinθ button.

sinButton = Button(scientificFrame, text= 'sinθ', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
sinButton.grid(row=1, column=0)

# Creating the cosθ button.

cosButton = Button(scientificFrame, text= 'cosθ', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
cosButton.grid(row=1, column=1)

# Creating the tanθ button.

tanButton = Button(scientificFrame, text= 'tanθ', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
tanButton.grid(row=1, column=2)

# Creating the GCD button.

gcdButton =  Button(buttonFrame, text= 'GCD', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
gcdButton.grid(row=5, column=0)

# Creating the () button.

firstbracketButton =  Button(buttonFrame, text= '()', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
firstbracketButton.grid(row=5, column=1)
firstbracketButton.bind('<Button-1>',click_btn_function)

# Creating the {} button.

secondbracketButton =  Button(buttonFrame, text= '{}', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
secondbracketButton.grid(row=5, column=2)
secondbracketButton.bind('<Button-1>',click_btn_function)

# Creating the [] button.

thirdbracketButton =  Button(buttonFrame, text= '[]', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
thirdbracketButton.grid(row=5, column=3)
thirdbracketButton.bind('<Button-1>',click_btn_function)

# Creating the remainder button.

remainderButton =  Button(buttonFrame, text= 'Remainder', font = font_type, width= 12, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
remainderButton.grid(row=4, column=2, columnspan = 2)

# Creating the log 2 button.

log2Button =  Button(scientificFrame, text= 'log2', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
log2Button.grid(row=1, column=3)

# Creating the log 10 button.

log10Button =  Button(scientificFrame, text= 'log10', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
log10Button.grid(row=1, column=4)

# Creating the tau button.

tauButton =  Button(scientificFrame, text= 'Tau', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
tauButton.grid(row=2, column=0)

# Creating the Pi button.

piButton =  Button(scientificFrame, text= 'Pi', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
piButton.grid(row=2, column=1)

# Creating the Euler's number button.

eButton =  Button(scientificFrame, text= 'e', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
eButton.grid(row=2, column=2)

# Creating the sin h button.

sinhButton =  Button(scientificFrame, text= 'sin h', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
sinhButton.grid(row=2, column=3)

# Creating the tan h button.

tanhButton =  Button(scientificFrame, text= 'tan h', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
tanhButton.grid(row=2, column=4)

# Creating the cos h button.

coshButton =  Button(scientificFrame, text= 'cos h', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
coshButton.grid(row=3, column=0)

# Creating the |X| button.

modulasButton =  Button(scientificFrame, text= '|X|', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
modulasButton.grid(row=3, column=1)

# Creating the Arc Tan button.

atanButton =  Button(scientificFrame, text= 'ArcTan', font = font_type, width= 5, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
atanButton.grid(row=3, column=2)

# Creating the Copy Sign button.

copysignButton =  Button(scientificFrame, text= 'Copy Sign', font = font_type, width= 12, pady = 5, padx = 5, relief = 'sunken', border = 5, 
activebackground = 'orange', activeforeground = 'white')
copysignButton.grid(row=3, column=3, columnspan = 2)

# Defining normal Calculator as global variable.
             
normalcalculator = True

# Defining calculate_sc function to perform various operations.

def calculate_sc(event):
    btn = event.widget
    text = btn['text']
    ex = textField.get()
    answer = ''
    
    if text == 'toDeg':
        answer = str(m.degrees(float(ex)))
                                                
    elif text == 'toRad':
        answer = str(m.radians(float(ex)))

    elif text == 'x!':
        answer = str(m.factorial(int(ex)))
        
    elif text == 'sinθ':
        answer = str(m.sin(m.radians(int(ex))))
        
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
        
    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))
        
    elif text == '√':
        answer = m.sqrt(int(ex))
        
    elif text == '^':
        base, pow = ex.split(',')
        answer = m.pow(int(base), int(pow))
        
    elif text == 'GCD':
        a, b = ex.split(',')
        answer = m.gcd(int(a), int(b))
       
    elif text == 'log2':
        answer = m.log2(int(ex))
        
    elif text == 'log10':
        answer = m.log10(int(ex))
        
    elif text == 'Tau':
        answer = m.tau
        
    elif text == 'Pi':
        answer = m.pi
        
    elif text == 'e':
        answer = m.e
        
    elif text == 'Remainder':
        a, b = ex.split(',')
        answer = m.remainder(int(a), int(b))
        
    elif text == 'sin h':
        answer = m.sinh(int(ex))
        
    elif text == 'tan h':
        answer = m.tanh(int(ex))
        
    elif text == 'cos h':
        answer = m.cosh(int(ex))
        
    elif text == '|X|':
        answer = m.fabs(int(ex))
        
    elif text == 'Floor':
        answer = m.floor(int(ex))
        
    elif text == 'ArcTan':
        answer = m.atan(int(float(ex)))
        
    elif text == 'Copy Sign':
        a, b = ex.split(',')
        answer = m.copysign(int(a), int(b))
        
    textField.delete(0, END)
    textField.insert(0, answer)

# Defining sc_click function to switch between scientific calculator and normal calculator.

def sc_click():
    
    global normalcalculator
    
    if normalcalculator:
        buttonFrame.pack_forget()
        scientificFrame.pack(side=TOP, pady=20)
        buttonFrame.pack(side=TOP)
        window.geometry('600x700')
        normalcalculator = False
    else:
        scientificFrame.pack_forget()
        window.geometry('600x600')
        normalcalculator = True

# Binding all the important buttons of scientific calculator with calculate_sc functions.
       
squarerootButton.bind("<Button-1>", calculate_sc)
powerButton.bind("<Button-1>", calculate_sc)
factorialButton.bind("<Button-1>", calculate_sc)
radianButton.bind("<Button-1>", calculate_sc)
degreeButton.bind("<Button-1>", calculate_sc)
sinButton.bind("<Button-1>", calculate_sc)
cosButton.bind("<Button-1>", calculate_sc)
tanButton.bind("<Button-1>", calculate_sc)
gcdButton.bind('<Button-1>',calculate_sc)
log2Button.bind('<Button-1>',calculate_sc)
log10Button.bind('<Button-1>',calculate_sc)
tauButton.bind('<Button-1>',calculate_sc)
piButton.bind('<Button-1>',calculate_sc)
eButton.bind('<Button-1>',calculate_sc)
remainderButton.bind('<Button-1>',calculate_sc)
sinhButton.bind('<Button-1>',calculate_sc)
tanhButton.bind('<Button-1>',calculate_sc)
coshButton.bind('<Button-1>',calculate_sc)
modulasButton.bind('<Button-1>',calculate_sc)
atanButton.bind('<Button-1>',calculate_sc)
copysignButton.bind('<Button-1>',calculate_sc)

# Defining the font type for the menu option.

fontMenu = ('verdana', 10)

# Defining the menu bar.

menubar = Menu(window, font = fontMenu)

# Defining the mode option.

mode = Menu(menubar, font = fontMenu, tearoff = 0)

# Adding the check button option.

mode.add_checkbutton(label="Scientific Calculator", command = sc_click)

menubar.add_cascade(label="Mode", menu=mode)

window.config(menu=menubar)

window.mainloop()
from tkinter import *
import tkinter.messagebox
import math
import parser

sc = Tk()
sc.title("Scientific Calculator")
sc.iconbitmap(sc,r"C:\Users\Md. Arafat Hossan\PY\calc.ico")
sc.config(bg="#4a485d")
sc.resizable(width=False, height=False)
sc.geometry("303x485+0+0")
calc = Frame(sc,bg="#4a485d",bd=10)
calc.grid()
#============================================================Function Part==========================================
#____________________________Function for Number pad an Display____________________________________________
class Calculator():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value = True
        self.check_sum= False
        self.op=""
        self.result=False

    def numberEnter(self,num):
        self.result=False
        firstNum= textDisplay.get()
        secondNum=str(num)
        if self.input_value:
            self.current=secondNum
            self.input_value=False           #Number Entry from numberpad
        else:
            if secondNum=='.':
                if secondNum in firstNum:
                    return
            self.current=firstNum+secondNum
        self.display(self.current)


    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(textDisplay.get())         #Displaying Result
    def display(self,value):
        textDisplay.delete(0,END)
        textDisplay.insert(0, value)


    def valid_function(self):
        if self.op == "add":
            self.total +=self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "div":
            self.total /= self.current  #Basic operations
        if self.op == "mod":
            self.total %= self.current
        if self.op == "ncr":
            self.total = math.factorial(self.total)/(math.factorial(self.current)*(math.factorial(self.total-self.current)))
        if self.op == "npr":
            self.total = math.factorial(self.total)/(math.factorial(self.total-self.current))
        if self.op == "inverse":
            self.total = 1/(pow(self.total,self.current))
        if self.op == "power":
            self.total = pow(self.total,self.current)
        if self.op == "exp":
            self.total = pow(self.total,self.current)
        self.input_value = True
        self.check_sum = False
        self.display(self.total)


    def operation(self,op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum = True
        self.op=op
        self.result = False

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def del_one(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

    def del_all(self):
        self.del_one()

        store = self.total
        self.total=0

    def squareroot(self):
        self.result=False
        self.current= math.sqrt(float(textDisplay.get()))
        self.display(self.current)

    def square(self):
        self.result=False
        self.current= math.pow(float(textDisplay.get()),2)
        self.display(self.current)

    def log_b_2(self):
        self.result=False
        self.current= math.log2(float(textDisplay.get()))
        self.display(self.current)

    def log_b_10(self):
        self.result=False
        self.current= math.log10(float(textDisplay.get()))
        self.display(self.current)

    def ln(self):
        self.result=False
        self.current= math.log1p(float(textDisplay.get()))
        self.display(self.current)

    def factorial(self):
        self.result=False
        self.current= math.factorial(float(textDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result=False
        self.current=math.cos(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result=False
        self.current=math.tan(math.radians(float(textDisplay.get())))
        self.display(self.current)

    def retrive_input(self):
        self.current=textDisplay.get()
#============================================Design Part====================================================

#_________________________________________Header 1st row______________________________________________________
header= Label(calc, text="CISCO     ", font=('cooper black',16,'bold'),bg="#4a485d", fg="#9ca2b0").grid(row=0,column=0, columnspan=2, pady=6)
header1= Label(calc, text="SCIENTIFIC CALCULATOR", font=('calibri',7,'bold','italic'),bg="#4a485d", fg="#9ca2b0").grid(row=0,column=2, columnspan=2, pady=6)
header11= Label(calc, text="fx-95Ms", font=('calibri',10,'bold','italic'),bg="#4a485d", fg="#9ca2b0").grid(row=0,column=4, columnspan=1, pady=6)


#_________________________________________Header 2st row______________________________________________________
header12= Label(calc, text="A.R.A.F.A.T", font=('wide latin',10,'bold'),bg="#4a485d", fg="#b26a80").grid(row=1,column=0, columnspan=5, )

#_________________________________________Display 3rd row______________________________________________________

added_value=Calculator()
textDisplay= Entry(calc, font=('arial',25, 'bold'), bg="#d5e3e4", bd=15, width=14,justify=RIGHT)
textDisplay.grid(row=2, column=0, columnspan=5, pady=10)
textDisplay.insert(0,"0")

#__________________________________________Numberpad_______________________________________________________

numpad="789456123"
i=0
btn=[]
for j in range(7,10):
    for k in range(3):
        btn.append(Button(calc,width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff", text=numpad[i]))
        btn[i].grid(row=j,column=k,pady=3)
        btn[i]["command"]=lambda x=numpad[i]: added_value.numberEnter(x)
        i+=1

#___________________________________4th Row________________________________

shiftBtn = Button(calc,text="SHIFT",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#c3c3cd",fg="#d8942a").grid(row=3,column=0,pady=3)

SqRootBtn = Button(calc,text="√",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#3c3b43",fg="#d8942a", command=added_value.squareroot).grid(row=3,column=1,pady=3)

SquarBtn = Button(calc,text="x²",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#3c3b43",fg="#d8942a" ,command=added_value.square).grid(row=3,column=2,pady=3)

factorialBtn = Button(calc,text="x!",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#3c3b43",fg="#d8942a", command= added_value.factorial).grid(row=3,column=3,pady=3)

offBtn = Button(calc,text="OFF",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#c3c3cd",fg="#d8942a", command=sc.destroy).grid(row=3,column=4,pady=3)

#___________________________________5th Row________________________________

eBtn = Button(calc,text="e",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff", command = added_value.e ).grid(row=4,column=0,pady=3)

perBtn = Button(calc,text="%",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=lambda: added_value.operation("mod")).grid(row=4,column=1,pady=3)

sinBtn = Button(calc,text="sin",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff", command=added_value.sin).grid(row=4,column=2,pady=3)

cosBtn = Button(calc,text="cos",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff", command=added_value.cos).grid(row=4,column=3,pady=3)

tanBtn = Button(calc,text="tan",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff", command=added_value.tan).grid(row=4,column=4,pady=3)

#___________________________________6th Row________________________________

PiBtn = Button(calc,text="π",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff", command = added_value.pi ).grid(row=5,column=0,pady=3)

left_bracketBtn = Button(calc,text="(",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=lambda: added_value.numberEnter("(")).grid(row=5,column=1,pady=3)

right_bracketBtn = Button(calc,text=")",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=lambda: added_value.numberEnter(")")).grid(row=5,column=2,pady=3)

log_base_2Btn = Button(calc,text="log2",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=added_value.log_b_2).grid(row=5,column=3,pady=3)

log_base_10Btn = Button(calc,text="log10",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=added_value.log_b_10).grid(row=5,column=4,pady=3)

#___________________________________7th Row________________________________

nprBtn = Button(calc,text="nPr",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=lambda: added_value.operation("npr")).grid(row=6,column=0,pady=3)

x_inversBtn = Button(calc,text="x^-1",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=lambda: added_value.operation("inverse")).grid(row=6,column=1,pady=3)

pwrBtn = Button(calc,text="^",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=lambda: added_value.operation("power")).grid(row=6,column=2,pady=3)

nCrBtn = Button(calc,text="nCr",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=lambda: added_value.operation("ncr")).grid(row=6,column=3,pady=3)

lnBtn = Button(calc,text="ln",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#3c3b43",fg="#ffffff",command=added_value.ln).grid(row=6,column=4,pady=3)

#_________________________8th Row_________________________________________________

DelBtn = Button(calc,text="DEL",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#b07281",fg="#ffffff", command= added_value.del_one).grid(row=7,column=3,pady=3)

AClrBtn = Button(calc,text="AC",width=4, height=1,font=('arial',10, 'bold'),bd=4, bg="#b07281",fg="#ffffff", command= added_value.del_all).grid(row=7,column=4,pady=3)

#_____________________________________9th Row_________________________________________

MultBtn = Button(calc,text="✕",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff",command=lambda: added_value.operation("multi")).grid(row=8,column=3,pady=3)

DivBtn = Button(calc,text="÷",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff",command=lambda: added_value.operation("div")).grid(row=8,column=4,pady=3)

#_____________________________________10th Row_________________________________________

addBtn = Button(calc,text="+",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff",command=lambda: added_value.operation("add")).grid(row=9,column=3,pady=3)

subBtn = Button(calc,text="-",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff",command=lambda: added_value.operation("sub")).grid(row=9,column=4,pady=3)

#___________________________________11th Row________________________________

ZeroroBtn = Button(calc,text="0",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff",command=lambda: added_value.numberEnter(0)).grid(row=10,column=0,pady=3)

DotBtn = Button(calc,text=".",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff",command=lambda: added_value.numberEnter(".")).grid(row=10,column=1,pady=3)

ExpBtn = Button(calc,text="EXP",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff",command=lambda: added_value.operation("exp")).grid(row=10,column=2,pady=3)

AnsBtn = Button(calc,text="ANS",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff",command = added_value.sum_of_total).grid(row=10,column=3,pady=3)

EquBtn = Button(calc,text="=",width=4, height=1,font=('arial',10, 'bold'),bd=4,bg="#9797a3",fg="#ffffff", command = added_value.sum_of_total).grid(row=10,column=4,pady=3)




sc.mainloop()

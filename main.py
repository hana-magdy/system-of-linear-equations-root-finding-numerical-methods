import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import urllib.request
from tkinter import *
from tkinter.tix import *
import array as arr
import Parse
import ReadFile
import LU
import Gaussian_elimination
import Gauss_Jordan
import  seidel
import ReadFile

import time

elapsed_time=0
elapsed_time1=0
elapsed_time2=0
elapsed_time3=0
elapsed_time4=0
file=0
LARGE_FONT = ("Verdana", 12)
expression = ""
popup=''
x0=0
x1=0

error = arr.array('d', [0.0])
xi = arr.array('d', [0.0])
xii = arr.array('d', [0.0])


global x2
class Intialization(tk.Tk):

 def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)








    self.frames = {}

    for F in (StartPage, PageOne):
        frame = F(container, self)

        self.frames[F] = frame

        frame.grid(row=0, column=0, sticky="nsew")

    self.show_frame(StartPage)
 def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()




class StartPage(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label=tk.Label(self,text="enter number of equations")
        label.grid(row=0,column=1)

        self.equation=tk.IntVar()
        self.equation.set('')



        expression_field = tk.Entry(self, textvariable=self.equation, bg='white')
        expression_field.grid(row=0,column=2,columnspan=50, ipadx=23)

        self.v = tk.IntVar()
        self.v.set("1")
        self.FromFile=tk.IntVar()
        self.FromFile.set("0")
        self.filename=tk.StringVar()
        label = tk.Label(self, text="OR")
        label.grid(row=0,column=50)
        tk.Radiobutton(self,
                       text="file",
                       padx=20,
                       variable=self.FromFile,
                       value=6, width=1, command=self.print_path, fg='black', bg='white').grid(row=0, column=100)
        SubmitButton = tk.Button(self, text='Done', fg='white', bg='black',
                                 command=lambda: self.OnSubmit(), height=2, width=9)
        SubmitButton.grid(row=1, column=2, pady=10)



    def OnSubmit(self):
     self.NumberOfEquations=tk.IntVar()
     self.NumberOfEquations=self.equation.get();


     self.namR = []
     for numbers in range(self.NumberOfEquations):
             self.namR.append(tk.Entry(self))
             self.namR[numbers].grid(row=2 + numbers, column=3)

     tk.Label(self,
              text="""Choose a method:""",
              justify=tk.LEFT,
              padx=18, fg='white', bg='black').grid(row=10, column=1)

     tk.Radiobutton(self,
                    text="gauss elimination",
                    padx=20,
                    variable=self.v,
                    value=1, width=12, bg='white').grid(row=11, column=1)

     tk.Radiobutton(self,
                    text="gauss jordan",
                    padx=20,
                    variable=self.v,
                    value=2, width=12, bg='white').grid(row=12, column=1)
     tk.Radiobutton(self,
                    text="LU decomposition",
                    padx=20,
                    variable=self.v,
                    value=3, width=12, bg='white').grid(row=13, column=1)

     tk.Radiobutton(self,
                    text="Gauss siedle",
                    padx=20,
                    variable=self.v,
                    value=4, width=12, bg='white').grid(row=14, column=1)

     tk.Radiobutton(self,
                    text="All",
                    padx=20,
                    variable=self.v,
                    value=5, width=12, bg='white').grid(row=15, column=1)
     lb = tk.Label(self, text="Incase of gauss seidel:", fg='white', bg='black').grid(column=1, row=16, pady=10)
     lbl = tk.Label(self, text=" Enter Tolerence", fg='white', bg='black').grid(column=1, row=17, pady=10)
     lb2 = tk.Label(self, text="Number of iterations", fg='white', bg='black').grid(column=1, row=18)
     self.expression_field_1 = tk.Entry(self, width=9)
     self.expression_field_1.grid(row=17, column=2, pady=10)
     self.expression_field_2 = tk.Entry(self, width=9)
     self.expression_field_2.grid(row=18, column=2)
     l = tk.Label(self, text="Intial guesses:", fg='white', bg='black').grid(column=1, row=19, pady=10)
     self.guess = []
     for numbers in range(self.NumberOfEquations):
         self.guess.append(tk.Entry(self))
         self.guess[numbers].grid(row=20 + numbers, column=1)

     ShowButton = tk.Button(self, text='Done', fg='white', bg='black',
                              command=lambda: self.collect(), height=2, width=9)
     ShowButton.grid(row=20+self.NumberOfEquations, column=1)



    def collect(self):
        global elapsed_time
        global elapsed_time1
        global elapsed_time2
        global elapsed_time3
        global elapsed_time4
        self.results=[]
        self.string=''
        imax = 50
        ea = 0.00001
        equations = [e.get() for e in self.namR]
        temp=[e.get() for e in self.guess]

        if self.v.get() == 3:
         start = time.perf_counter()
         self.results,self.string=Parse.Parse(equations,"LU",self.NumberOfEquations,[],0,0)
         end = time.perf_counter()
         elapsed_time = end - start
         self.PassDataToPage1()

        if self.v.get() == 2:
            start = time.perf_counter()
            Parse.Parse(equations, "Gaussian-jordan", self.NumberOfEquations,[],0,0)
            end = time.perf_counter()
            elapsed_time = end - start
            self.PassDataToPage1()

        if self.v.get()== 1:
            start = time.perf_counter()
            self.results=Parse.Parse(equations, "Gaussian-elimination", self.NumberOfEquations,[],0,0)
            end = time.perf_counter()
            elapsed_time = end - start
            self.PassDataToPage1()

        if self.v.get()== 4:
            if self.expression_field_1.get() != '':
                ea = float(self.expression_field_1.get())
            if self.expression_field_2.get() != '':
                imax = int(self.expression_field_2.get())
            IntialGuesses = [int(numeric_string) for numeric_string in temp]
            start = time.perf_counter()
            Parse.Parse(equations, "seidel", self.NumberOfEquations,IntialGuesses, ea, imax)
            end = time.perf_counter()
            elapsed_time = end - start
            self.PassDataToPage1()

        if self.v.get()== 5:

            if self.expression_field_1.get() != '':
                ea = float(self.expression_field_1.get())
            if self.expression_field_2.get() != '':
                imax = int(self.expression_field_2.get())
            IntialGuesses = [int(numeric_string) for numeric_string in temp]

            start = time.perf_counter()
            Parse.Parse(equations, "LU", self.NumberOfEquations, [], 0, 0)
            end = time.perf_counter()
            elapsed_time1 = end - start

            start = time.perf_counter()
            Parse.Parse(equations, "Gaussian-jordan", self.NumberOfEquations, [], 0, 0)
            end = time.perf_counter()
            elapsed_time2 = end - start

            start = time.perf_counter()
            Parse.Parse(equations, "Gaussian-elimination", self.NumberOfEquations, [], 0, 0)
            end = time.perf_counter()
            elapsed_time3 = end - start

            start = time.perf_counter()
            Parse.Parse(equations, "seidel", self.NumberOfEquations, IntialGuesses, ea, imax)
            end = time.perf_counter()
            elapsed_time4 = end - start

            self.PassDataToPage1()

    def PassDataToPage1(self):
        self.controller.method = self.v.get()
        self.controller.frames[PageOne].correct_label()  # call correct_label function
        self.controller.show_frame(PageOne)


    def print_path(self):
         self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                           filetypes=(("text file", ".txt"), ("all files", ".*")))

         self.configure(background="white")
         global file
         file=1
         ReadFile.ReadFromFile(self.filename)





class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.LabelTitle = tk.Label(self, text="")
        self.LabelTitle1 = tk.Label(self, text="")
        self.LabelTitle2 = tk.Label(self, text="")
        self.LabelTitle3 = tk.Label(self, text="")
        self.LabelTitle4 = tk.Label(self, text="")
        self.sperator = tk.Label(self, text="***************************************************************************")



    def correct_label(self):
        if self.controller.method == 3:
            self.LabelTitle.config(text="Result of LU decompostion method", font=("Helvetica", 8))
            self.LabelTitle.grid(row=0, column=0)
            if LU.string=="":
                for i in range(LU.n):
                    tempno=str(i+1)
                    temp="variable "+ tempno +":  "+ str(LU.x[i])+"\n"
                    self.label=tk.Label(self,text=temp)
                    self.label.grid(row=1+i, column=1)

                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time), font=("Helvetica", 8))
                self.label.grid(row=2+LU.n, column=0)

            else:
                self.label = tk.Label(self, text=LU.string)
                self.label.grid(row=1, column=1)
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time), font=("Helvetica",8))
                self.label.grid(row=2, column=0)


        elif self.controller.method==1:
            self.LabelTitle.config(text="Result of Gauss Elmination method", font=("Helvetica",8))
            self.LabelTitle.grid(row=0, column=0)
            if Gaussian_elimination.string =="":
                for i in range(Gaussian_elimination.n):
                    tempno = str(i + 1)
                    temp = "variable " + tempno + ":  " + str(Gaussian_elimination.x[i]) + "\n"
                    self.label = tk.Label(self, text=temp)
                    self.label.grid(row=1 + i, column=1)
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time), font=("Helvetica",8))
                self.label.grid(row=2 + Gaussian_elimination.n, column=0)
            else:
                self.label = tk.Label(self, text=Gaussian_elimination.string)
                self.label.grid(row=1, column=1)
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time), font=("Helvetica", 8))
                self.label.grid(row=2, column=0)


        elif self.controller.method==2:
            self.LabelTitle.config(text="Result of Gauss jordan method", font=("Helvetica", 8))
            self.LabelTitle.grid(row=0, column=0)
            if Gauss_Jordan.string =="":
                for i in range(Gauss_Jordan.n):
                    tempno = str(i + 1)
                    temp = "variable " + tempno + ":  " + str(Gauss_Jordan.x[i]) + "\n"
                    self.label = tk.Label(self, text=temp)
                    self.label.grid(row=1 + i, column=1)
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time), font=("Helvetica",8))
                self.label.grid(row=2 + Gauss_Jordan.n, column=0)

            else:
                self.label = tk.Label(self, text=Gauss_Jordan.string)
                self.label.grid(row=1, column=1)
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time), font=("Helvetica",8))
                self.label.grid(row=2, column=0)

        elif self.controller.method==4:
            self.LabelTitle.config(text="Result of Gauss seidel method", font=("Helvetica", 8))
            self.LabelTitle.grid(row=0, column=0)
            if seidel.string =="":
                self.LabelTabelIteration=tk.Label(self, text="Iteration", font=("Helvetica", 8))
                self.LabelTabelIteration.grid(row=1, column=0)
                for i in range(seidel.n):
                    tempno = str(i + 1)
                    temp = " variable " + tempno
                    self.label = tk.Label(self, text=temp , font=("Helvetica", 8))
                    self.label.grid(row=1, column=1+i)
                for i in range(seidel.n):
                    tempno = str(i + 1)
                    temp = "  error of variable " + tempno
                    self.label = tk.Label(self, text=temp , font=("Helvetica",8))
                    self.label.grid(row=1, column=1+i+seidel.n)
                for i in range(len(seidel.results)):
                    self.LabelTabelIteration = tk.Label(self, text=i, font=("Helvetica",8))
                    self.LabelTabelIteration.grid(row=2 + i, column=0)
                    for j in range(seidel.n):
                     self.label = tk.Label(self, text=seidel.results[i][j], font=("Helvetica", 8))
                     self.label.grid(row=2+i, column=1 +j)
                for i in range(len(seidel.terrors)):
                    for j in range(seidel.n):
                     self.label = tk.Label(self, text=seidel.terrors[i][j], font=("Helvetica", 8))
                     self.label.grid(row=3+i, column=1+seidel.n +j)

                self.label = tk.Label(self, text="Number of iterations= "+str(len(seidel.terrors)), font=("Helvetica", 8))
                self.label.grid(row=4 + len(seidel.results), column=0)
                self.label = tk.Label(self, text="Elapsed time= "+str(elapsed_time), font=("Helvetica", 8))
                self.label.grid(row=5 + len(seidel.results), column=0)

            else:
                self.label = tk.Label(self, text=seidel.string)
                self.label.grid(row=1, column=1)
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time), font=("Helvetica",8))
                self.label.grid(row=2, column=0)

        elif self.controller.method == 5:
            RowCounter=0
            ###############################
            self.LabelTitle1.config(text="Result of Gauss Elmination method", font=("Helvetica", 8))
            self.LabelTitle1.grid(row=RowCounter, column=0)
            RowCounter+=1
            if Gaussian_elimination.string =="":
                for i in range(Gaussian_elimination.n):
                    tempno = str(i + 1)
                    temp = "variable " + tempno + ":  " + str(Gaussian_elimination.x[i]) + "\n"
                    self.label = tk.Label(self, text=temp)
                    self.label.grid(row=RowCounter, column=1)
                    RowCounter+=1
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time3), font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)
                RowCounter += 1
            else:
                self.label = tk.Label(self, text=Gaussian_elimination.string)
                self.label.grid(row=RowCounter, column=1)
                RowCounter += 1
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time3), font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)

            RowCounter +=1
            self.sperator = tk.Label(self,
                                     text="***************************************************************************")
            self.sperator.grid(row=RowCounter, column=0)
            RowCounter += 1
            self.LabelTitle2.config(text="Result of Gauss jordan method", font=("Helvetica", 8))
            self.LabelTitle2.grid(row=RowCounter, column=0)
            RowCounter += 1
            if Gauss_Jordan.string =="":
                for i in range(Gauss_Jordan.n):
                    tempno = str(i + 1)
                    temp = "variable " + tempno + ":  " + str(Gauss_Jordan.x[i]) + "\n"
                    self.label = tk.Label(self, text=temp)
                    self.label.grid(row=RowCounter, column=1)
                    RowCounter += 1
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time2), font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)
                RowCounter += 1

            else:
                self.label = tk.Label(self, text=Gauss_Jordan.string)
                self.label.grid(row=RowCounter, column=1)
                RowCounter += 1
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time2), font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)
            RowCounter += 1
            self.sperator = tk.Label(self,text="***************************************************************************")
            self.sperator.grid(row=RowCounter, column=0)
            RowCounter += 1
            self.LabelTitle3.config(text="Result of LU decompostion method", font=("Helvetica", 8))
            self.LabelTitle3.grid(row=RowCounter, column=0)
            RowCounter += 1
            if LU.string =="":
                for i in range(LU.n):
                    tempno = str(i + 1)
                    temp = "variable " + tempno + ":  " + str(LU.x[i]) + "\n"
                    self.label = tk.Label(self, text=temp)
                    self.label.grid(row=RowCounter, column=1)
                    RowCounter += 1

                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time1), font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)
                RowCounter += 1

            else:
                self.label = tk.Label(self, text=LU.string)
                self.label.grid(row=RowCounter, column=1)
                RowCounter += 1
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time1), font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)
                RowCounter += 1

            self.sperator = tk.Label(self,
                                     text="***************************************************************************")
            self.sperator.grid(row=RowCounter, column=0)
            RowCounter += 1
            self.LabelTitle4.config(text="Result of Gauss seidel method", font=("Helvetica", 8))
            self.LabelTitle4.grid(row=RowCounter, column=0)
            RowCounter += 1
            if seidel.string =="":
                self.LabelTabelIteration = tk.Label(self, text="Iteration", font=("Helvetica", 8))
                self.LabelTabelIteration.grid(row=RowCounter, column=0)
                for i in range(seidel.n):
                    tempno = str(i + 1)
                    temp = " variable " + tempno
                    self.label = tk.Label(self, text=temp, font=("Helvetica", 8))
                    self.label.grid(row=RowCounter, column=1 + i)
                for i in range(seidel.n):
                    tempno = str(i + 1)
                    temp = "  error of variable " + tempno
                    self.label = tk.Label(self, text=temp, font=("Helvetica", 8))
                    self.label.grid(row=RowCounter, column=1 + i + seidel.n)
                temp = RowCounter+1
                for i in range(len(seidel.results)):
                    RowCounter += 1
                    self.LabelTabelIteration = tk.Label(self, text=i, font=("Helvetica", 8))
                    self.LabelTabelIteration.grid(row=RowCounter, column=0)
                    for j in range(seidel.n):
                        self.label = tk.Label(self, text=seidel.results[i][j], font=("Helvetica", 8))
                        self.label.grid(row=RowCounter, column=1 + j)
                for i in range(len(seidel.terrors)):
                    temp += 1
                    for j in range(seidel.n):
                        self.label = tk.Label(self, text=seidel.terrors[i][j], font=("Helvetica", 8))
                        self.label.grid(row=temp, column=1 + seidel.n + j)
                RowCounter+=1
                self.label = tk.Label(self, text="Number of iterations= " + str(len(seidel.terrors)),
                                      font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)
                RowCounter += 1
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time4), font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)
                RowCounter += 1

            else:
                self.label = tk.Label(self, text=seidel.string)
                self.label.grid(row=RowCounter, column=1)
                RowCounter += 1
                self.label = tk.Label(self, text="Elapsed time= " + str(elapsed_time4), font=("Helvetica", 8))
                self.label.grid(row=RowCounter, column=0)









app = Intialization()
app.geometry("550x800")
app.title("Numerical Analysis")
app.mainloop()

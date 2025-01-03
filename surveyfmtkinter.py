"survey form using tkinter"


from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox


x = Tk()
x.title("Survey Form")
x.geometry("400x500")


l = Label(x, text="Let us know how we can improve", font="san-serif 15 bold")
l.grid(row=0, columnspan=2, pady=10)


l2 = Label(x, text="Name:", font="san-serif 10 bold")
l2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
e = Entry(x, justify="left")
e.grid(row=1, column=1, padx=10, pady=5)


l3 = Label(x, text="Email:", font="san-serif 10 bold")
l3.grid(row=2, column=0, sticky="w", padx=10, pady=5)
e1 = Entry(x, justify="left")
e1.grid(row=2, column=1, padx=10, pady=5)


l4 = Label(x, text="Age:", font="san-serif 10 bold")
l4.grid(row=3, column=0, sticky="w", padx=10, pady=5)
e2 = Entry(x, justify="left")
e2.grid(row=3, column=1, padx=10, pady=5)

def fileclick():
    u = filedialog.askopenfilename()

bb = Button(x, text="Choose file", bg="skyblue", fg="black", bd=5, command=fileclick)
bb.grid(row=4, columnspan=2, pady=5)


l5 = Label(x, text="Which option best describes your current role ?", font="san-serif 10 bold")
l5.grid(row=5, column=0, sticky="w", padx=10, pady=5)
cc = Combobox(x)
cc["values"] = ["Student", "Employee", "UNEMPLOYED"]
cc.current(0)
cc.grid(row=5, column=1, padx=10, pady=5)


l6 = Label(x, text="How likely is it that you would recommend this program to a friend?", font="san-serif 10 bold")
l6.grid(row=6, column=0, sticky="w", padx=10, pady=5)

r1 = Radiobutton(x, text="Definitely", value=1)
r1.grid(row=6, column=1, sticky="w", padx=10)

r2 = Radiobutton(x, text="Maybe", value=2)
r2.grid(row=7, column=1, sticky="w", padx=10)

r3 = Radiobutton(x, text="Not sure", value=3)
r3.grid(row=8, column=1, sticky="w", padx=10)


l7 = Label(x, text="Things that should be improved in the future (Check all that apply):", font="san-serif 10 bold")
l7.grid(row=9, column=0, sticky="w", padx=10, pady=5)

cb1 = Checkbutton(x, text="Front-end Projects")
cb1.grid(row=9, column=1, sticky="w", padx=10)

cb2 = Checkbutton(x, text="Back-end Projects")
cb2.grid(row=10, column=1, sticky="w", padx=10)

cb3 = Checkbutton(x, text="Data Visualization")
cb3.grid(row=11, column=1, sticky="w", padx=10)


l8 = Label(x, text="Any Comments or Suggestions?", font="san-serif 10 bold")
l8.grid(row=12, column=0, sticky="w", padx=10, pady=5)

e3 = Text(x, height=4, width=30)
e3.grid(row=12, column=1, padx=10, pady=5)


b1 = Button(x, text="Submit", bg="green", fg="white", bd=5)
b1.grid(row=13, columnspan=2, pady=10)


x.mainloop()

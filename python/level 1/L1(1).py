from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("320x450")

expression = ""
equation = StringVar()

def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

entry = Entry(
    root,
    textvariable=equation,
    font=("Arial", 20),
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        Button(
            root,
            text=text,
            width=8,
            height=3,
            command=equal
        ).grid(row=row, column=col)
    else:
        Button(
            root,
            text=text,
            width=8,
            height=3,
            command=lambda t=text: press(t)
        ).grid(row=row, column=col)

Button(
    root,
    text="DEL",
    width=8,
    height=3,
    command=backspace
).grid(row=5, column=0)

Button(
    root,
    text="CLEAR",
    width=17,
    height=3,
    command=clear
).grid(row=5, column=1, columnspan=2)

Button(
    root,
    text="EXIT",
    width=8,
    height=3,
    command=root.destroy
).grid(row=5, column=3)

root.mainloop()

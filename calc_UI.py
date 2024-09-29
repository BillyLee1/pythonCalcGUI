import tkinter as tk

def calcUI(root):
    btnframe = tk.Frame(root)
    btnframe.columnconfigure(0, weight=3)
    btnframe.columnconfigure(1, weight=3)
    btnframe.columnconfigure(2, weight=3)
    btnframe.columnconfigure(3, weight=3)

    btn1 = tk.Button(btnframe, text = '1')
    btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(btnframe, text = '2')
    btn2.grid(row=2, column=1, sticky=tk.W+tk.E)

    btn3 = tk.Button(btnframe, text = '3')
    btn3.grid(row=2, column=2, sticky=tk.W+tk.E)

    btnMin = tk.Button(btnframe, text = '-')
    btnMin.grid(row=2, column=3, sticky=tk.W+tk.E)

    btn4 = tk.Button(btnframe, text = '4')
    btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

    btn5 = tk.Button(btnframe, text = '5')
    btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

    btn6 = tk.Button(btnframe, text = '6')
    btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

    btnMul = tk.Button(btnframe, text = 'x')
    btnMul.grid(row=1, column=3, sticky=tk.W+tk.E)

    btn7 = tk.Button(btnframe, text = '7')
    btn7.grid(row=0, column=0, sticky=tk.W+tk.E)

    btn8 = tk.Button(btnframe, text = '8')
    btn8.grid(row=0, column=1, sticky=tk.W+tk.E)

    btn9 = tk.Button(btnframe, text = '9')
    btn9.grid(row=0, column=2, sticky=tk.W+tk.E)

    btnDiv = tk.Button(btnframe, text = '÷')
    btnDiv.grid(row=0, column=3, sticky=tk.W+tk.E)

    btn0 = tk.Button(btnframe, text = '0')
    btn0.grid(row=3, column=1, sticky=tk.W+tk.E)

    btnAdd = tk.Button(btnframe, text = '+')
    btnAdd.grid(row=3, column=3, sticky=tk.W+tk.E)

    btnEquals = tk.Button(btnframe, text = '=')
    btnEquals.grid(row=4, column=3, sticky=tk.W+tk.E)

    btnframe.pack(fill='x', padx=20)

    return btnframe

  
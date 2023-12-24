import tkinter as tk

class CalculatorGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Standard Calculator v1")
        self.geometry('380x550')

        self.gui_widgets()
    
    def gui_widgets(self):
        self.ref_y = 50
        self.button_zero = tk.Button(self, text="0", width=22, height=4)
        self.button_zero.place(x=5, y=self.ref_y + 425)

        self.button_dot = tk.Button(self, text=".", width=10, height=4)
        self.button_dot.place(x=175, y=self.ref_y + 425) 

        self.button_one = tk.Button(self, text="1", width=10, height=4)
        self.button_one.place(x=5, y=self.ref_y + 350) 

        self.button_two = tk.Button(self, text="2", width=10, height=4)
        self.button_two.place(x=90, y=self.ref_y + 350) 

        self.button_three = tk.Button(self, text="3", width=10, height=4)
        self.button_three.place(x=175, y=self.ref_y + 350)

        self.button_four = tk.Button(self, text="4", width=10, height=4)
        self.button_four.place(x=5, y=self.ref_y + 275)

        self.button_five = tk.Button(self, text="5", width=10, height=4)
        self.button_five.place(x=90, y=self.ref_y + 275)

        self.button_six = tk.Button(self, text="6", width=10, height=4)
        self.button_six.place(x=175, y=self.ref_y + 275)

        self.button_seven = tk.Button(self, text="7", width=10, height=4)
        self.button_seven.place(x=5, y=self.ref_y + 200)

        self.button_eight = tk.Button(self, text="8", width=10, height=4)
        self.button_eight.place(x=90, y=self.ref_y + 200)

        self.button_nine = tk.Button(self, text="9", width=10, height=4)
        self.button_nine.place(x=175, y=self.ref_y + 200)

        self.button_per = tk.Button(self, text="%", width=10, height=4)
        self.button_per.place(x=5, y=self.ref_y + 125)

        self.button_ac = tk.Button(self, text="AC", width=10, height=4)
        self.button_ac.place(x=90, y=self.ref_y + 125)

        self.button_back = tk.Button(self, text="Del", width=10, height=4)
        self.button_back.place(x=175, y=self.ref_y + 125)

        self.button_equal = tk.Button(self, text="=", width=15, height=4)
        self.button_equal.place(x=260, y=self.ref_y + 425) 

        self.button_plus = tk.Button(self, text="+", width=15, height=4)
        self.button_plus.place(x=260, y=self.ref_y + 350)

        self.button_minus = tk.Button(self, text="-", width=15, height=4)
        self.button_minus.place(x=260, y=self.ref_y + 275)

        self.button_times = tk.Button(self, text="x", width=15, height=4)
        self.button_times.place(x=260, y=self.ref_y + 200)

        self.button_divide = tk.Button(self, text="/", width=15, height=4)
        self.button_divide.place(x=260, y=self.ref_y + 125)



if __name__ == "__main__":
    app = CalculatorGui()
    app.mainloop()
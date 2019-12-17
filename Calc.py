"""Simple pay calculator with ability to calculate total pay before
    tax for given shifts, including weekends and public holidays. Work commenced
    17/12/2019, Danielle"""

from tkinter import *
from math import *

class Calc:

    rate = 36.6
    day_allowance = 29.7
    night_allowance = 80.3

    def __init__(self, master):
        self.master = master
        master.title("Weekly Pay")

        self.calculate_pay = Button(master, text = "Calculate My Pay")

root = Tk()
my_calc = Calc(root)
root.mainloop()
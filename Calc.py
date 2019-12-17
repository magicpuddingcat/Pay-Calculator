"""Simple pay calculator with ability to calculate total pay before
    tax for given shifts, including weekends and public holidays. Work commenced
    17/12/2019, Danielle"""

from tkinter import *
from math import *

"""Create the calculator, which can gather employment data from the user
    and then generate a pre-tax pay sum."""
class Calc:

    rate = 36.6
    day_allowance = 29.7
    night_allowance = 80.3
    weekend_loading = 0.5
    holiday_loading = 1

    def __init__(self, master):
        self.master = master
        master.title("My Pay Calculator")

        # add all of the labels to prompt the user for input and the input fields
        #
        # Widgets to gather total hours from user
        self.total_hours_lbl = Label(master, text = "Enter this week's hours: ")
        self.total_hours_lbl.pack()
        self.user_total_hours = Entry(master)
        self.user_total_hours.pack()

        # Widgets to get number of day shifts the user worked
        self.days_worked_lbl = Label(master, text = "How many morning/afternoon shifts did you work?")
        self.days_worked_lbl.pack()
        self.user_days = Entry(master)
        self.user_days.pack()

        # Widgets for number night shifts that the user has worked
        self.nights_worked_lbl = Label(master, text = "How many night shifts did you work?")
        self.nights_worked_lbl.pack()
        self.user_nights = Entry(master)
        self.user_nights.pack()

        # Widgets for hours user completed in a weekend
        self.hours_wkend_lbl = Label(master, text = "How many hours did you work during a weekend?")
        self.hours_wkend_lbl.pack()
        self.user_wkend_hours = Entry(master)
        self.user_wkend_hours.pack()

        # Widgets for number of hours user completed on a public holiday
        self.hours_holiday_lbl = Label(master, text = "How may hours did you work during a public holiday?")
        self.hours_holiday_lbl.pack()
        self.user_holiday_hours = Entry(master)
        self.user_holiday_hours.pack()

        # add button that will return the weekly payment sum to the user
        self.pay_calc_button = Button(master, text = "Calculate Pay", command = self.say_hello())
        self.pay_calc_button.pack()

    # Note, THIS IS TO BE DELETED WHEN A MORE SUITABLE FUNCTION IS READY
    def say_hello(self):
        print("Hello!")

    def calculate_pay(self, total_hours, nights, days, hours_wkend, hours_holiday):
        pay = total_hours * self.rate + nights * self.night_allowance + \
            days * self.day_allowance + hours_wkend * self.rate * self.weekend_loading \
            + hours_holiday * self.rate * self.holiday_loading
        return pay


# Initialize the GUI window
root = Tk()
my_calc = Calc(root)
root.mainloop()
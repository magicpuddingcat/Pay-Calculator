"""Simple pay calculator with ability to calculate total pay before
    tax for my current job, including weekends and public holidays. Work commenced
    17/12/2019, Danielle"""

from tkinter import *
from math import *

class Calc:

    rate = 48.0
    pm_allowance = 29.7
    night_allowance = 82.0
    weekend_loading = 0.5
    holiday_loading = 1.0

    def __init__(self, master):
        self.master = master
        master.title("My Pay Calculator")

        self.title = Label(master, text="Calculate my pay!")
        self.title.pack()

        # add all of the labels to prompt the user for input and the input fields
        #
        # Widgets to gather total hours from user
        self.total_hours_lbl = Label(master, text = "Enter this week's hours: ")
        self.total_hours_lbl.pack()
        self.user_total_hours = Entry(master)
        self.user_total_hours.pack()

        # Widgets to get number of day shifts the user worked
        self.days_worked_lbl = Label(master, text = "How many afternoon shifts did you work?")
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
        self.pay_calc_button = Button(master, text="Calculate Pay", command=self.display)
        self.pay_calc_button.pack()

        #add the lable that will display the final amount
        self.pay_display = Label(self.master, text="")
        self.pay_display.pack()

    def calculate_pay(self):
        # If the user has entered something in all fields and clicks calculate, calculate pay
        pay = self.num_total_hours * self.rate + self.num_nights * self.night_allowance + \
              self.num_days * self.pm_allowance + \
            self.num_hours_wkend * self.rate * self.weekend_loading \
              + self.num_hours_holiday * self.rate * self.holiday_loading
        return pay

    def display(self):

        # Get all relevant values entered by the user
        self.num_total_hours = float(self.user_total_hours.get())
        self.num_days = float(self.user_days.get())
        self.num_nights = float(self.user_nights.get())
        self.num_hours_wkend = float(self.user_wkend_hours.get())
        self.num_hours_holiday = float(self.user_holiday_hours.get())

        if (float(self.num_total_hours + self.num_hours_wkend + self.num_hours_holiday))>=0:
            self.pay_amount = self.calculate_pay()
            self.pay_display['text'] = str(self.pay_amount)
            self.pay_display.pack()

# Initialize the GUI window
root = Tk()
my_calc = Calc(root)
root.mainloop()

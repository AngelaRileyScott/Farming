'''
Program: farm_calculator
Author: Angela Scott
Last Modified: 29 FEB 2024
This program will display a entry box to accept information. It will ask the user for a farmers first name, last name, and id number.
It will also ask for the produce picked and the quanities in gallons and quarts.
'''

#Import the tools and classes
import class_input
import tkinter
from tkinter import ttk

#Get data from entry boxes
def enter_data():
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    produce = produce_combobox.get()
    gallons = gallon_spinbox.get()
    quarts = quart_spinbox.get()
   
#Print data from form
    print("You are inputting data for:", firstname, lastname)
    print("The farmer has picked", gallons, "gallons", "&", quarts, "quarts of", produce)

#Create Window
window = tkinter.Tk()
window.title("Welcome to the Farm Calculator")

frame = tkinter.Frame(window)
frame.pack()

#Use Window and Prompt Boxes to Collect Data
user_info_frame = tkinter.LabelFrame(frame, text="Farmer Information")
user_info_frame.grid(row=0, column=0, padx = 10, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
id_number_label = tkinter.Label(user_info_frame, text="ID Number")
id_number_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
id_number_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
id_number_entry.grid(row=1, column=2)

#Use a widget to adjust spacing
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

#Build a frame for produce and collect quantity
produce_frame = tkinter.LabelFrame(frame, text="Produce Counter")
produce_frame.grid(row=1, column=0, padx=20, pady=20)

produce_label = tkinter.Label(produce_frame, text="Select the Produce")
produce_combobox = ttk.Combobox (produce_frame, values=["Blackberries", "Raspberries", "Strawberries"])
produce_label.grid(row=2, column=0)
produce_combobox.grid(row=3, column=0)

gallon_label = tkinter.Label(produce_frame, text="Enter the gallons picked.")
gallon_spinbox = tkinter.Spinbox(produce_frame, from_=0, to="infinity")
gallon_label.grid(row=2, column=1)
gallon_spinbox.grid(row=3, column=1)

quart_label = tkinter.Label(produce_frame, text="Enter the quarts picked.")
quart_spinbox = tkinter.Spinbox(produce_frame, from_=0, to="infinity")
quart_label.grid(row=2, column=2)
quart_spinbox.grid(row=3, column=2)

#Use a widget to adjust spacing
for widget in produce_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#button
button = tkinter.Button(frame, text="Enter Data", command = enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

window.mainloop()
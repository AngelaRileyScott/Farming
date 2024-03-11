'''
Program: farm_calculator
Author: Angela Scott
Last Modified: 10 MARCH 2024
This program will display a window to allow produce pickers to estimate their profit. 
It will provide a report of total money collected and give the picker their take home pay.
It also takes into account the price discounts for the quality of the produce during the season.
'''

#Import the tools and classes
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

'''This section will initialze a window to create the GUI.'''

#Create a class to handle the initial screen and submission form      
class OrderBerries:
   
    def __init__(self, master):       
        self.master = master
        master.title("Riley Ridge Farm Calculator")

        #Import the image from the directory (import from VS Code)
        self.img = Image.open("rows.jpg")
        self.photo = ImageTk.PhotoImage(self.img)
        self.img2 = Image.open("strawberryjam.jpg")
        self.photo2 = ImageTk.PhotoImage(self.img2)
        
        #Create a label to display the image
        self.label = tk.Label(master, image=self.photo, text="Picture of strawberries in rows.", font=("bold", 10))
        self.label.grid(row=0, column=0)
        self.label2 = tk.Label(master, image=self.photo2, text="Picture of strawberry jam.", font=("bold", 10))
        self.label2.grid(row=0, column=2)
        self.label3 = tk.Label(master, text="Picture of strawberries in rows.", font=("bold", 8))
        self.label3.grid(row=1, column=0)
        self.label4 = tk.Label(master, text="Picture of strawberry jam.", font=("bold", 8))
        self.label4.grid(row=1, column=2)

        #Create a label and entry form for the farm
        self.farm_label = tk.Label(master, text="Welcome to the \nRiley Ridge Farm Calculator", bg="#a47200", font=("Bell MT", 24))
        self.farm_label.grid(row=0, column=1, padx=10, pady=10)
        
        self.user_info_frame = tkinter.LabelFrame(master, text="Farmer Information")
        self.user_info_frame.grid(row=2, column=1)

        self.first_name_label = tkinter.Label(master, text="First Name", font="bold")
        self.first_name_label.grid(row=3, column=0, padx=10, pady=10)
        self.last_name_label = tkinter.Label(master, text="Last Name", font="bold")
        self.last_name_label.grid(row=3, column=1, padx=10, pady=10)
        self.id_number_label = tkinter.Label(master, text="ID Number", font="bold")
        self.id_number_label.grid(row=3, column=2, padx=10, pady=10)

        self.first_name_entry = tkinter.Entry(master)
        self.last_name_entry = tkinter.Entry(master)
        self.id_number_entry = tkinter.Entry(master)
        self.first_name_entry.grid(row=4, column=0, padx=10, pady=10)
        self.last_name_entry.grid(row=4, column=1, padx=10, pady=10)
        self.id_number_entry.grid(row=4, column=2, padx=10, pady=10)
        
        #Build a frame for produce and collect quantity, Commented frame to access attributes from self.
        #produce_frame = tkinter.LabelFrame(master, text="Produce Counter")
        #produce_frame.grid(row=9, column=1, padx=20, pady=20)

        self.produce_label = tkinter.Label(master, text="Select the Produce", font="bold")
        self.produce_combobox = ttk.Combobox (master, values=["Blackberries", "Raspberries", "Strawberries"])
        self.produce_label.grid(row=5, column=0, padx=10, pady=10)
        self.produce_combobox.grid(row=6, column=0, padx=10, pady=10)

        self.gallon_label = tkinter.Label(master, text="Enter the gallons picked.", font="bold")
        self.gallon_spinbox = tkinter.Spinbox(master, from_=0, to="infinity")
        self.gallon_label.grid(row=5, column=1, padx=10, pady=10)
        self.gallon_spinbox.grid(row=6, column=1, padx=10, pady=10)

        self.quart_label = tkinter.Label(master, text="Enter the quarts picked.", font="bold")
        self.quart_spinbox = tkinter.Spinbox(master, from_=0, to="infinity")
        self.quart_label.grid(row=5, column=2, padx=10, pady=10)
        self.quart_spinbox.grid(row=6, column=2, padx=10, pady=10)

        self.quality_label = tkinter.Label(master, text="What is the produce quality?", font="bold")
        self.quality_combobox = ttk.Combobox (master, values=["EXCELLENT-Early Season", "GREAT-Mid Season", "GOOD-Mid or Late Season", "FARMER/JAM QUALITY-Late Season"])
        self.quality_label.grid(row=7, column=1, padx=10, pady=10)
        self.quality_combobox.grid(row=8, column=1, padx=10, pady=10)

        #Create a button to submit data
        self.order_button = tk.Button(master, text="Submit Your Data", bg="#a9ac00", command=self.enter_data)
        self.order_button.grid(row=9, column=1, padx=10, pady=10)
        
        #Create a button to submit data
        self.order_button = tk.Button(master, text="Request Farmer Payout", bg="#ffac00", command=self.payout_data)
        self.order_button.grid(row=10, column=1, padx=10, pady=10)
        
        #Create a button to submit data
        self.exit_button = tk.Button(master, text="Exit the Program", bg="#7c1e14", command=self.exit_window)
        self.exit_button.grid(row=11, column=1, padx=10, pady=10) 
          
        #Create a menu bar
        self.menu_bar = tk.Menu(master)
        self.about_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label="Hours of Operation", command=self.show_hours)
        self.about_menu.add_command(label="Current Prices", command=self.show_prices)
        self.about_menu.add_command(label="Contact Information", command=self.show_contact)
        
        self.menu_bar.add_cascade(label="Menu", menu=self.about_menu)
        master.config(menu=self.menu_bar)  

    '''The section will take the data inputs and run the calculations.'''
    #Get data from form and report results.
    def enter_data(self):
        firstname = self.first_name_entry.get()
        lastname = self.last_name_entry.get()
        produce = self.produce_combobox.get()
        gallons = self.gallon_spinbox.get()
        quarts = self.quart_spinbox.get()
        quality = self.quality_combobox.get()
        messagebox.showinfo ("Submission", "Your data has been submitted. \nSee the program screen for results.")
        print("You are inputting data for:", firstname, lastname)
        print("The farmer has reported", gallons, "gallons and", quarts, "quarts of", produce, "picked.")
        print("Today's berry quality is", quality)
                
        #Calculate the price
        gallons_price = float(gallons) * 16
        quarts_price = float(quarts) * 4
        price_total = (gallons_price + quarts_price)
        discount1 = 0.875
        discount2 = 0.625
        
        #Calculate the discount
        if quality == "GOOD-Mid or Late Season":
            #float(price_total * discount1)
            print("The new price with discounts is: $", price_total*discount1)
            print("The total amount due to the farmer is: $", price_total*0.25)
        elif quality == "FARMER/JAM QUALITY-Late Season":
            #float(price_total * discount2)
            print("The new price with discounts is: $", price_total*discount2)
            print("The total amount due to the farmer is: $", price_total*0.25)
        else:
            print("The total money collected is: $", price_total)
            print("The total amount due to the farmer is: $", price_total*0.25)
            
            final_price = price_total
                
            #with open('document.txt', 'a') as file:
                #file.write(price_total)
                
            return final_price
        
    #Response to the requested data payout, Show percentage paid to the farmer for labor        
    def payout_data(self):
        payout = "25%"
        print("The current payout is calculated at:", payout)
        messagebox.showinfo ("Payout", payout)
        return payout
    
    #Window for exiting the program  
    def exit_window(self):
        root.destroy()
        messagebox.showinfo ("Exit", "You have exited the program.")
        
    def on_invalid(self):
        self.show_message('Please enter a valid input.', 'red')
    
    '''The section will build the drop down menus for the menu bar. It includes information such as farm hours, seasonal prices,
    and the farm email.'''
    #Information to display in Menu Bar       
    def show_hours(self):
        messagebox.showinfo("Hours of Operation", "May thru June \n8:00am - 8:00pm \nField Conditions are updated on social media.")
   
    #Placeholder for current prices, can be updated     
    def show_prices(self):
        messagebox.showinfo("Prices", "Farmer Picked Gallon - $16\nU-Pick Gallon - $10\nDiscounts are applied by the farmer.")

    #Link to information
    def show_contact(self):
        messagebox.showinfo("Contact Information", "farmer@rileyridgefarm.com")

#Close the program        
root = tk.Tk()
app = OrderBerries(root)
root.mainloop()
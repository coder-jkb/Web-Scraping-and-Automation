'''
Please Note:
1.  The ChromeDriver is for the Version 104.0.5112.102 of Chrome,
    Please install another chromedriver.exe and add new .exe in this directory
    in case of difference in version

2. The given link (http://demoserver99.com/assignments/index2.html) was not working 
    hence I have found an altenative link (https://cybertext.wordpress.com/2007/04/30/fake-names-for-documentation/) 
    This link has a large record of names
    I have completed the assignment using this alternative link link

'''
from tkinter import *
from tkinter import messagebox

# Importing functions from web.py in the same dir
from web import validate, scrape

# Create root window
root = Tk()

# Setting up window
root.title("Patients Search")
root.geometry('500x400') # widthxheight
root.minsize(450,300)
root.maxsize(600,400)
root.configure(bg='black') # set window background color black
root.option_add( "*font", "Arial 15" )


# Function called when search button is clicked 
def search_clicked(event):
    name = input.get()   
    valid_name, name_list = validate(name)

    if valid_name:
        # scrape using name_list
        scrape(name_list)
        label_txt = "Input: " + str(name_list) + "\nPlease check the console for result (objact)"
        result.config(text = label_txt)
        result.grid(row=4,column=2)
    else:
        # display msg box in case of invalid name
        messagebox.showwarning("showwarning", "Opps! Invalid name entered.\n"+txt)




# message to the user
txt = "NOTE: Patient name should be in the format\n  FirstName<space>LastName\n  (Example: John Peter Doe)"

Label( root, text=txt, 
       bg="black",fg="yellow", 
       justify=LEFT,anchor='e').grid(row=1, column=1,padx=15, pady=15,columnspan=2)

patient_name = Label(root, 
                    text = "Patient: ", 
                    bg="black", fg="white")

input = Entry(root, width = 20,
              bg="#f4b6fc", fg="black")

search = Button(root, text = "Search" ,
                bg="purple", fg="yellow", 
                command=lambda:search_clicked('<Return>'))

result = Label(root,bg="black", fg="white")

# the parameter '<Return>' is passed in 
# local variable (event) of function search_data
# for enabling key binding of 'Enter' key press

root.bind('<Return>', search_clicked)

patient_name.grid(row=2,column=1, padx=10)
input.grid(row=2,column=2)
search.grid(row=3,column=1, pady=20)

root.mainloop()

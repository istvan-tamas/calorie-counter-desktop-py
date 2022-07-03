from tkinter import *

# main windows obj
app = Tk()

app.title = ('Calorie counter')
app.geometry('700x350')


# food item

food = StringVar()
food_label = Label(app, text='Food', font=('Bold', 14), pady=20, padx=10)
food_label.grid(row=0, column=0, sticky=W)
food_entry = Entry(app,textvariable=food)
food_entry.grid(row=0, column=1)

#food calorie
calorie = IntVar()
calorie_label = Label(app, text='Calorie', font=('Bold', 14), pady=20, padx=10)
calorie_label.grid(row=0, column=2, sticky=W)
calorie_entry = Entry(app,textvariable=calorie)
calorie_entry.grid(row=0, column=3)

# calling the main window

app.mainloop()

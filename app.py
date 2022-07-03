from tkinter import *
from typing import List

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

# food list
food_list = Listbox(app, height=8, width=50)
food_list.grid(row=1, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

food_scroll_bar = Scrollbar(app)
food_scroll_bar.grid(row=1, column=4)
# attach scrollbar

food_list.configure(yscrollcommand=food_scroll_bar.set)
food_scroll_bar.configure(command=food_list.yview)

# calling the main window

app.mainloop()

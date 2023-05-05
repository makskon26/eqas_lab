import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# створюємо список днів на тиждень
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# створюємо словник, де ключі - дати, а значення - список доступних проміжків часу
time_slots = {
    datetime.today().strftime('%Y-%m-%d'): ['10:00-12:00', '14:00-16:00', '18:00-20:00'],
}


class App:
    def __init__(self, master):
        self.master = master
        mediator = Mediator()  # create mediator instance
        master.title("Date and Time Selector")
        master.geometry('400x500')

        # create Checkbox instance and pass mediator instance to it
        self.checkbox = Checkbox(master, mediator)

        # create Textfield instance and pass mediator instance to it
        self.textfield = Textfield(master, mediator)

        self.data = Data(master, mediator)

        # add submit button
        self.submit_button = ttk.Button(master, text='Submit', command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        selected_date = self.data.date_picker.get()
        selected_time = self.data.time_picker.get()
        print(f'Date: {selected_date}, Time: {selected_time}')
        if self.checkbox.other_person_var.get():
            print(self.textfield.name_entry.get())
            print(self.textfield.phone_entry.get())
        # update available times list based on selected date
        self.data.time_picker.config(values=time_slots[selected_date])

class Mediator:
    def __init__(self):
        self.checkbox = None
        self.textfield = None
        self.data = None

    def register_checkbox(self, checkbox):
        self.checkbox = checkbox

    def register_textfield(self, textfield):
        self.textfield = textfield

    def register_time(self, data):
        self.data = data

    def update_other_person_fields(self):
        if self.checkbox.other_person_var.get():
            self.textfield.name_entry.config(state='normal')
            self.textfield.phone_entry.config(state='normal')
        else:
            self.textfield.name_entry.delete(0, tk.END)
            self.textfield.phone_entry.delete(0, tk.END)
            self.textfield.name_entry.config(state='disabled')
            self.textfield.phone_entry.config(state='disabled')

    def update_pickup_fields(self):
        if self.checkbox.costumer_pickup_var.get():
            self.textfield.name_entry.config(state='disabled')
            self.textfield.phone_entry.config(state='disabled')
            self.data.time_picker.config(state='disabled')
            self.data.date_picker.config(state='disabled')
        else:
            self.textfield.name_entry.delete(0, tk.END)
            self.textfield.phone_entry.delete(0, tk.END)
            self.textfield.name_entry.config(state='disabled')
            self.textfield.phone_entry.config(state='disabled')
            self.data.time_picker.config(state='normal')
            self.data.date_picker.config(state='normal')




class Checkbox:
    def __init__(self, master, mediator):
        self.mediator = mediator
        self.other_person_var = tk.BooleanVar()
        self.other_person_var.set(False)
        self.other_person_cb = tk.Checkbutton(master, text="Other Person", variable=self.other_person_var, command=self.mediator.update_other_person_fields)
        self.other_person_cb.pack()

        self.costumer_pickup_var = tk.BooleanVar()
        self.costumer_pickup_var.set(False)
        self.costumer_pickup_cb = tk.Checkbutton(master, text="Costumer pickup", variable=self.costumer_pickup_var,
                                              command=self.mediator.update_pickup_fields)
        self.costumer_pickup_cb.pack()
        self.mediator.register_checkbox(self)

class Textfield:
    def __init__(self, master, mediator):
        self.mediator = mediator
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master, state='disabled')
        self.name_entry.pack(padx=10, pady=10)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(master, state='disabled')
        self.phone_entry.pack(padx=10, pady=10)

        self.mediator.register_textfield(self)
        self.mediator.update_other_person_fields()

class Data:
    def __init__(self, master, mediator):
        # create widget for selecting date
        self.mediator = mediator
        self.date_label = ttk.Label(master, text='Select a date:')
        self.date_label.pack(pady=(10, 0))
        self.date_picker = ttk.Combobox(master, values=days_of_week)
        self.date_picker.current(0)
        self.date_picker.pack()

        # create widget for selecting time
        self.time_label = ttk.Label(master, text='Select a time:')
        self.time_label.pack(pady=(10, 0))
        self.time_picker = ttk.Combobox(master, values=time_slots[datetime.today().strftime('%Y-%m-%d')])
        self.time_picker.current(0)
        self.time_picker.pack()

        self.mediator.register_time(self)
        self.mediator.update_pickup_fields()

root = tk.Tk()
app = App(root)
root.mainloop()

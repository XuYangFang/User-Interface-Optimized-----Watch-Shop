#XuYang Fang
#05/09/2022


import tkinter
import tkinter.messagebox
import sqlite3 as lite
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

# Define the class Employee:
class Employee:
    def __init__(self):
        self.employee_window = tkinter.Tk()
        self.employee_window.title('Employee')
        self.conn = lite.connect('WatchData.db')

        # Create frames
        self.title_frame = tkinter.Frame(self.employee_window)
        self.results_frame = tkinter.Frame(self.employee_window)
        self.cid_frame = tkinter.Frame(self.employee_window)
        self.lastname_frame = tkinter.Frame(self.employee_window)
        self.firstname_frame = tkinter.Frame(self.employee_window)
        self.city_frame = tkinter.Frame(self.employee_window)
        self.state_frame = tkinter.Frame(self.employee_window)
        self.phone_frame = tkinter.Frame(self.employee_window)
        self.email_frame = tkinter.Frame(self.employee_window)
        self.payweek_frame = tkinter.Frame(self.employee_window)
        self.button_frame = tkinter.Frame(self.employee_window)

        #  attributes
        self.message = ''
        self.value = ''
        self.results = ''

        # title frame
        self.title = tkinter.Label(self.title_frame, height=5, width=60,
                                                text='Employee Interface',
                                                borderwidth=10, relief='sunken')
        self.title.pack(side='top')

        # results frame
        self.results = tkinter.Label(self.results_frame, height=1, width=1, text=' ')
        self.results.pack(side='bottom')


         # information frame
        self.prompt1 = tkinter.Label(self.cid_frame, height=2, width=18, text='Employee ID')
        self.id_entry = tkinter.Entry(self.cid_frame, width=30)
        self.prompt2 = tkinter.Label(self.lastname_frame, height=2, width=18, text='Last Name ')
        self.ln_entry = tkinter.Entry(self.lastname_frame, width=30)
        self.prompt3 = tkinter.Label(self.firstname_frame, height=2, width=18, text='First Name ')
        self.fn_entry = tkinter.Entry(self.firstname_frame, width=30)
        self.prompt4 = tkinter.Label(self.city_frame, height=2, width=18, text='City: ')
        self.city_entry = tkinter.Entry(self.city_frame, width=30)
        self.prompt5 = tkinter.Label(self.state_frame, height=2, width=18, text='State: ')
        self.state_entry = tkinter.Entry(self.state_frame, width=30)
        self.prompt6 = tkinter.Label(self.phone_frame, height=2, width=18, text='Phone: ')
        self.phone_entry = tkinter.Entry(self.phone_frame, width=30)
        self.prompt7 = tkinter.Label(self.email_frame, height=2, width=18, text='Email: ')
        self.email_entry = tkinter.Entry(self.email_frame, width=30)
        self.prompt8 = tkinter.Label(self.payweek_frame, height=2, width=18, text='Pay/Week')
        self.pay_entry = tkinter.Entry(self.payweek_frame, width=28)

        # Pack the widgets aligned to the left
        self.prompt1.pack(side='left')
        self.id_entry.pack(side='left')
        self.prompt2.pack(side='left')
        self.ln_entry.pack(side='left')
        self.prompt3.pack(side='left')
        self.fn_entry.pack(side='left')
        self.prompt4.pack(side='left')
        self.city_entry.pack(side='left')
        self.prompt5.pack(side='left')
        self.state_entry.pack(side='left')
        self.prompt6.pack(side='left')
        self.phone_entry.pack(side='left')
        self.prompt7.pack(side='left')
        self.email_entry.pack(side='left')
        self.prompt8.pack(side='left')
        self.pay_entry.pack(side='left')

        # Create the buttons for the button_frame:
        self.searchid_button = tkinter.Button(self.button_frame, text='Search ID', command=self.searchid)
        self.search_button = tkinter.Button(self.button_frame, text='Search Name', command=self.search)
        self.insert_button = tkinter.Button(self.button_frame, text='Add', command=self.add)
        self.update_button = tkinter.Button(self.button_frame, text='Update', command=self.update)
        self.remove_button = tkinter.Button(self.button_frame, text='Delete', command=self.delete)
        self.show_button = tkinter.Button(self.button_frame, text='Show All', command=self.show)
        self.menu_button = tkinter.Button(self.button_frame, text='Return', command=self.employee_window.destroy)

        # Pack each button, aligned to the left
        self.searchid_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.search_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.insert_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.update_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.remove_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.show_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.menu_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)

        # Pack the frames
        self.title_frame.pack()
        self.results_frame.pack()
        self.cid_frame.pack()
        self.lastname_frame.pack()
        self.firstname_frame.pack()
        self.city_frame.pack()
        self.state_frame.pack()
        self.phone_frame.pack()
        self.email_frame.pack()
        self.payweek_frame.pack()
        self.button_frame.pack()

        # Commit the changes to the database
        self.conn.commit()


    # Define the searchid function
    def searchid(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM Employee WHERE employee_id = ?', (self.id_entry.get(),))
            rows = cur.fetchone()

            # ID not found
            if rows is None:
                tkinter.messagebox.showinfo('Notification', f'ERROR'
                                                     f'\n\nID not found'
                                                     f'\nPlease try again')
            else:
                # ID found
                self.value = f' ID: {rows[0]}' \
                             f'\n Name: {rows[2]} {rows[1]}' \
                             f'\n Address: {rows[3]}, {rows[4]}' \
                             f'\n Phone: {rows[5]}'\
                             f'\n Email: {rows[6]}'\
                             f'\n Pay Week: {rows[7]}'
                self.results = tkinter.Label(self.results_frame, height=7, width=70, text=self.value)
                self.results.pack(side='left')


    def search(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM Employee WHERE last_name = ? AND first_name = ?', (self.ln_entry.get(), self.fn_entry.get(),))

            rows = cur.fetchone()
            #  name not found
            if rows is None:
                tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                     f'\nName not found.'
                                                     f'\n\nPlease try again.')
            else:
                # name found
                self.value = f' ID: {rows[0]}' \
                             f'\n Name: {rows[2]} {rows[1]}' \
                             f'\n Address: {rows[3]}, {rows[4]}' \
                             f'\n Phone: {rows[5]}' \
                             f'\n Email: {rows[6]}' \
                             f'\n Pay/Week: {rows[7]}'
                self.results = tkinter.Label(self.results_frame, height=6, width=70, text=self.value)
                self.results.pack(side='left')


    # Define the add function
    def add(self):
        # Get and store information
        ln = self.ln_entry.get()
        fn = self.fn_entry.get()
        city = self.city_entry.get()
        st = self.state_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        pay = self.pay_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM Employee WHERE last_name = ? AND first_name = ?', (ln, fn,))
            rows = cur.fetchone()
            # name not found
            if rows is None:
                # Execute the SQL statement to add
                cur.execute('INSERT INTO Employee (last_name, first_name, city, state, phone, email, pay_week)'
                            'SELECT ?, ?, ?, ?, ?, ?, ?',
                            (ln, fn, city, st, phone, email, pay,))
                tkinter.messagebox.showinfo('Notification', f'ATTENTION: '
                                                            f'\nAn entry for {fn} {ln} has been added.')
            else:
                tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                        f'\n{fn} {ln} is already in the customer database.')


    # Define the update function
    def update(self):
        # Get and store information
        ln = self.ln_entry.get()
        fn = self.fn_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        pay = self.pay_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            # Execute SQL statement to find name
            cur.execute('SELECT * FROM Employee WHERE last_name = ? AND first_name = ?', (ln, fn,))
            rows = cur.fetchone()
            #  name not found
            if rows is None:
                tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                        f'\nEntry not found. Cannot update.'
                                                        f'\n\nPlease try again or add a new entry.')
            else:
                # name found
                cur.execute('UPDATE Employee SET city = ?, state = ?, '
                            'phone = ?, email = ?, pay_week = ? WHERE last_name = ? AND first_name = ?',
                            (city, state, phone, email, pay, ln, fn,))
                tkinter.messagebox.showinfo('Notification', f'ATTENTION: '
                                            f'\nThe entry for {fn} {ln} has been updated.')


    # Define the delete function
    def delete(self):
        ln = self.ln_entry.get()
        fn = self.fn_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            # Execute SQL statement to find name
            cur.execute('SELECT * FROM Employee WHERE last_name = ? AND first_name = ?',
                        (ln, fn,))
            row = cur.fetchone()
            # name not found
            if row is None:
                # Notify user that entry does not exist
                tkinter.messagebox.showinfo('Notification', f'ATTENTION:'
                                                            f'\nEntry not found.')
            else:
                # execute the SQL statement to delete
                cur.execute('DELETE FROM Employee WHERE last_name = ? AND first_name = ?',
                            (ln, fn,))

                cur.execute('SELECT * FROM Employee WHERE last_name = ? AND first_name = ?',
                            (ln, fn,))
                row = cur.fetchone()

                if row is None:
                    tkinter.messagebox.showinfo('Notification', f'ATTENTION:'
                                                                    f'\nThe employee {fn} {ln} has been deleted.')
                else:
                    tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                            f'\nThe entry could not be deleted.')

    def show(self):
        class showall(ttk.Frame):
            def __init__(self, parent):
                ttk.Frame.__init__(self, padding="10 10 10 10")
                self.pack(fill=tk.BOTH, expand=True)
                self.scrollbar = Scrollbar(root)

                # Create a listbox
                self.listbox = Listbox(root, heigh=30, selectmode=SINGLE, width=135, yscrollcommand=self.scrollbar.set,
                                       activestyle='none')
                self.scrollbar.config(command=self.listbox.yview)
                self.listbox.pack(side=LEFT, pady="10", padx="10")
                self.scrollbar.pack(side=LEFT, fill=Y)
                self.pack(fill=tk.BOTH, expand=True)

                ttk.Button(self, text="View all the employee", command=self.showemployee).grid(column=3, row=0)

            def showemployee(self):
                self.listbox.delete(0, END)
                c.execute("""SELECT employee_ID,'Last Name: '
                                                || last_name,'First Name: '
                                                || first_name,'City: '
                                                || city, 'State: '
                                                || state, 'Phone: '
                                                || phone, 'Email: '
                                                || email, 'Pay/Week: '
                                                || pay_week FROM Employee""")
                results = c.fetchall()
                for result in results:
                    self.listbox.insert(END, result)

        conn = lite.connect("WatchData.db")
        c = conn.cursor()

        root = tk.Tk()
        tree = ttk.Treeview(root)
        root.title("All Employee")
        root.geometry("1000x1000")
        showall(root)
        root.mainloop()
        c.close()
        conn.close()

if __name__ == '__main__':
    show_employee = Employee()
    tkinter.mainloop()





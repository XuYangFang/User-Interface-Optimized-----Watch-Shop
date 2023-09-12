#XuYang Fang
#05/09/2022

import tkinter
import tkinter.messagebox
import sqlite3 as lite
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


# class Inventory:
class Inventory:
    def __init__(self):
        # Create inventory window
        self.inventory_window = tkinter.Tk()
        self.inventory_window.title('Inventory')
        self.conn = lite.connect('WatchData.db')

        # Create frames
        self.title_frame = tkinter.Frame(self.inventory_window)
        self.results_frame = tkinter.Frame(self.inventory_window)
        self.id_frame = tkinter.Frame(self.inventory_window)
        self.brand_frame = tkinter.Frame(self.inventory_window)
        self.name_frame = tkinter.Frame(self.inventory_window)
        self.cost_frame = tkinter.Frame(self.inventory_window)
        self.qty_frame = tkinter.Frame(self.inventory_window)
        self.button_frame = tkinter.Frame(self.inventory_window)

        self.message = ''
        self.value = ''
        self.results = ''

        # title frame
        self.inventory_title = tkinter.Label(self.title_frame, height=5, width=60,
                                                text='Inventory Interface',
                                                borderwidth=10, relief='sunken')
        self.inventory_title.pack(side='top')

        # results frame
        self.results = tkinter.Label(self.results_frame, height=1, width=1, text=' ')
        self.results.pack(side='bottom')


         # information frame
        self.prompt1 = tkinter.Label(self.id_frame, height=2, width=18, text='Item ID')
        self.id_entry = tkinter.Entry(self.id_frame, width=30)
        self.prompt2 = tkinter.Label(self.brand_frame, height=2, width=18, text='Brand')
        self.brand_entry = tkinter.Entry(self.brand_frame, width=30)
        self.prompt3 = tkinter.Label(self.name_frame, height=2, width=18, text='Item Name ')
        self.name_entry = tkinter.Entry(self.name_frame, width=30)
        self.prompt4 = tkinter.Label(self.cost_frame, height=2, width=18, text='Purchasing Cost ')
        self.cost_entry = tkinter.Entry(self.cost_frame, width=30)
        self.prompt5 = tkinter.Label(self.qty_frame, height=2, width=18, text='Quantity: ')
        self.qty_entry = tkinter.Entry(self.qty_frame, width=30)
        self.prompt1.pack(side='left')
        self.id_entry.pack(side='left')
        self.prompt2.pack(side='left')
        self.brand_entry.pack(side='left')
        self.prompt3.pack(side='left')
        self.name_entry.pack(side='left')
        self.prompt4.pack(side='left')
        self.cost_entry.pack(side='left')
        self.prompt5.pack(side='left')
        self.qty_entry.pack(side='left')

        # button frame
        self.searchid_button = tkinter.Button(self.button_frame, text='Search ID', command=self.searchid)
        self.search_button = tkinter.Button(self.button_frame, text='Search Name', command=self.search)
        self.insert_button = tkinter.Button(self.button_frame, text='Add', command=self.add)
        self.update_button = tkinter.Button(self.button_frame, text='Update', command=self.update)
        self.remove_button = tkinter.Button(self.button_frame, text='Delete', command=self.delete)
        self.show_button = tkinter.Button(self.button_frame, text='Show All', command=self.show)
        self.menu_button = tkinter.Button(self.button_frame, text='Return', command=self.inventory_window.destroy)
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
        self.id_frame.pack()
        self.brand_frame.pack()
        self.name_frame.pack()
        self.cost_frame.pack()
        self.qty_frame.pack()
        self.button_frame.pack()

        self.conn.commit()


    # Define the searchid function
    def searchid(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM Inventory WHERE item_id = ?', (self.id_entry.get(),))
            rows = cur.fetchone()

            # name not found
            if rows is None:
                tkinter.messagebox.showinfo('Notification', f'ERROR !'
                                                     f'\n\nID not found !'
                                                     f'\nPlease type again !')
            else:
                # name found
                self.value = f' ID: {rows[0]}' \
                             f'\n Brand: {rows[4]}'\
                             f'\n Item Name: {rows[1]} ' \
                             f'\n Purchasing Cost: {rows[2]}' \
                             f'\n Quantity: {rows[3]}'
                self.results = tkinter.Label(self.results_frame, height=6, width=70, text=self.value)
                self.results.pack(side='left')


    def search(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM Inventory WHERE item_name = ?', (self.name_entry.get(),))

            rows = cur.fetchone()
            # name not found
            if rows is None:
                tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                     f'\nItem not found.'
                                                     f'\n\nPlease try again.')
            else:
                # name found
                self.value = f' ID: {rows[0]}' \
                             f'\n Brand: {rows[4]}' \
                             f'\n Item Name: {rows[1]} ' \
                             f'\n Purchasing Cost: {rows[2]}' \
                             f'\n Quantity: {rows[3]}'
                self.results = tkinter.Label(self.results_frame, height=6, width=70, text=self.value)
                self.results.pack(side='left')


    # Define add function
    def add(self):
        # Get and store information
        name = self.name_entry.get()
        cost = self.cost_entry.get()
        qty = self.qty_entry.get()
        brand = self.brand_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            # Execute SQL statement to find name
            cur.execute('SELECT * FROM Inventory WHERE item_name = ?', (name,))
            rows = cur.fetchone()

            # name not found
            if rows is None:
                # Execute the SQL statement to add
                cur.execute('INSERT INTO Inventory (item_name, cost, quantity, brand)'
                            'SELECT ?, ?, ?,?',
                            (name, cost, qty, brand,))
                tkinter.messagebox.showinfo('Notification', f'ATTENTION: '
                                                            f'\nAn entry for {name} has been added.')
            else:
                tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                        f'\n{name} is already in the customer database.')


    # Define the update function
    def update(self):
        # Get and store information
        name = self.name_entry.get()
        cost = self.cost_entry.get()
        qty = self.qty_entry.get()
        brand = self.brand_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            # Execute SQL statement to find name
            cur.execute('SELECT * FROM Inventory WHERE item_name = ?', (name,))
            rows = cur.fetchone()
            # name not found
            if rows is None:
                tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                        f'\nEntry not found. Cannot update.'
                                                        f'\n\nPlease try again or add a new entry.')
            else:
                # Execute the SQL statement to update
                cur.execute('UPDATE Inventory SET cost = ?, quantity = ?, brand = ? WHERE item_name = ?',
                            (cost, qty, name, brand))
                tkinter.messagebox.showinfo('Notification', f'ATTENTION: '
                                            f'\nThe entry for {name} has been updated.')


    # Define the delete function
    def delete(self):
        name = self.name_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            # Execute SQL statement to find name
            cur.execute('SELECT * FROM Inventory WHERE item_name = ?',
                        (name,))
            row = cur.fetchone()
            # name not found
            if row is None:
                tkinter.messagebox.showinfo('Notification', f'ATTENTION:'
                                                            f'\nEntry not found.')
            else:
                # execute the SQL statement to delete
                cur.execute('DELETE FROM Inventory WHERE item_name = ?',
                            (name,))
                # Execute SQL statement to find name again
                cur.execute('SELECT * FROM Inventory WHERE item_name = ?',
                            (name,))
                row = cur.fetchone()
                if row is None:
                    tkinter.messagebox.showinfo('Notification', f'ATTENTION:'
                                                                    f'\nThe item {name} has been deleted.')
                else:
                    # Notify user that it is still there.
                    tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                            f'\nThe entry could not be deleted.')

    def show(self):
        class showall(ttk.Frame):
            def __init__(self, parent):
                ttk.Frame.__init__(self, padding="10 10 10 10")
                self.pack(fill=tk.BOTH, expand=True)
                self.scrollbar = Scrollbar(root)

                # Create a listbox for search queries
                self.listbox = Listbox(root, heigh=30, selectmode=SINGLE, width=135, yscrollcommand=self.scrollbar.set,
                                       activestyle='none')
                self.scrollbar.config(command=self.listbox.yview)
                self.listbox.pack(side=LEFT, pady="10", padx="10")
                self.scrollbar.pack(side=LEFT, fill=Y)
                self.pack(fill=tk.BOTH, expand=True)

                ttk.Button(self, text="View all the Inventory", command=self.showcustomer).grid(column=3, row=0)


            def showcustomer(self):
                self.listbox.delete(0, END)
                c.execute("""SELECT item_id,'Brand: '
                                        || brand, 'Item Name: '
                                        || item_name,'Purchasing Cost: '
                                        || cost,'Quantity: '
                                        || quantity FROM Inventory""")
                results = c.fetchall()
                for result in results:
                    self.listbox.insert(END, result)

        conn = lite.connect("WatchData.db")
        c = conn.cursor()

        root = tk.Tk()
        tree = ttk.Treeview(root)
        root.title("All Inventory")
        root.geometry("1000x1000")
        showall(root)
        root.mainloop()
        c.close()
        conn.close()

if __name__ == '__main__':
    show_inventory = Inventory()
    tkinter.mainloop()







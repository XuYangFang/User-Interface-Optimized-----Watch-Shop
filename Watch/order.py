#XuYang Fang
#05/09/2022

import tkinter
import tkinter.messagebox
import sqlite3 as lite
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


# class Order:
class Order:
    def __init__(self):
        # Create Order window
        self.order_window = tkinter.Tk()
        self.order_window.title('Order')
        self.conn = lite.connect('WatchData.db')

        # Create frames
        self.title_frame = tkinter.Frame(self.order_window)
        self.results_frame = tkinter.Frame(self.order_window)
        self.orderid_frame = tkinter.Frame(self.order_window)
        self.customerid_frame = tkinter.Frame(self.order_window)
        self.itemid_frame = tkinter.Frame(self.order_window)
        self.qty_frame = tkinter.Frame(self.order_window)
        self.payout_frame = tkinter.Frame(self.order_window)
        self.profit_frame = tkinter.Frame(self.order_window)
        self.button_frame = tkinter.Frame(self.order_window)

        self.message = ''
        self.value = ''
        self.results = ''

        # title frame
        self.order_title = tkinter.Label(self.title_frame, height=5, width=60,
                                                text='Order Interface',
                                                borderwidth=10, relief='sunken')
        self.order_title.pack(side='top')

        # results frame
        self.results = tkinter.Label(self.results_frame, height=1, width=1, text=' ')
        self.results.pack(side='bottom')


         # information frame
        self.prompt1 = tkinter.Label(self.orderid_frame, height=2, width=18, text='Order ID')
        self.orderid_entry = tkinter.Entry(self.orderid_frame, width=30)
        self.prompt2 = tkinter.Label(self.customerid_frame, height=2, width=18, text='Customer ID')
        self.customerid_entry = tkinter.Entry(self.customerid_frame, width=30)
        self.prompt3 = tkinter.Label(self.itemid_frame, height=2, width=18, text='Item ID ')
        self.itemid_entry = tkinter.Entry(self.itemid_frame, width=30)
        self.prompt4 = tkinter.Label(self.qty_frame, height=2, width=18, text='Quantity ')
        self.qty_entry = tkinter.Entry(self.qty_frame, width=30)
        self.prompt5 = tkinter.Label(self.payout_frame, height=2, width=18, text='Payout: ')
        self.payout_entry = tkinter.Entry(self.payout_frame, width=30)
        self.prompt6 = tkinter.Label(self.profit_frame, height=2, width=18, text='Profit: ')
        self.profit_entry = tkinter.Entry(self.profit_frame, width=30)
        self.prompt1.pack(side='left')
        self.orderid_entry.pack(side='left')
        self.prompt2.pack(side='left')
        self.customerid_entry.pack(side='left')
        self.prompt3.pack(side='left')
        self.itemid_entry.pack(side='left')
        self.prompt4.pack(side='left')
        self.qty_entry.pack(side='left')
        self.prompt5.pack(side='left')
        self.payout_entry.pack(side='left')
        self.prompt6.pack(side='left')
        self.profit_entry.pack(side='left')

        # button frame:
        self.search_button = tkinter.Button(self.button_frame, text='Search ID', command=self.search)
        self.insert_button = tkinter.Button(self.button_frame, text='Add', command=self.add)
        self.update_button = tkinter.Button(self.button_frame, text='Update', command=self.update)
        self.remove_button = tkinter.Button(self.button_frame, text='Delete', command=self.delete)
        self.show_button = tkinter.Button(self.button_frame, text='Show All', command=self.show)
        self.menu_button = tkinter.Button(self.button_frame, text='Return', command=self.order_window.destroy)
        self.search_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.insert_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.update_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.remove_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.show_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)
        self.menu_button.pack(side='left', padx=10, pady=10, ipadx=6, ipady=6)

        # Pack the frames
        self.title_frame.pack()
        self.results_frame.pack()
        self.orderid_frame.pack()
        self.customerid_frame.pack()
        self.itemid_frame.pack()
        self.qty_frame.pack()
        self.payout_frame.pack()
        self.profit_frame.pack()
        self.button_frame.pack()

        self.conn.commit()


    # Define the search function
    def search(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute('SELECT * FROM Dindan WHERE hao = ?', (self.orderid_entry.get(),))
            rows = cur.fetchone()

            # id not found
            if rows is None:
                tkinter.messagebox.showinfo('Notification', f'ERROR !'
                                                     f'\n\nID not found !'
                                                     f'\nPlease type again !')
            else:
                # id found
                self.value = f' Order ID: {rows[0]}' \
                             f'\n Customer ID: {rows[1]}'\
                             f'\n Item ID: {rows[2]} ' \
                             f'\n Quantity: {rows[3]}' \
                             f'\n Payout: {rows[4]}' \
                             f'\n Profit: {rows[5]}'
                self.results = tkinter.Label(self.results_frame, height=6, width=70, text=self.value)
                self.results.pack(side='left')



    # Define the add function
    def add(self):
        # Get and store the information
        orderid = self.orderid_entry.get()
        customerid = self.customerid_entry.get()
        itemid = self.itemid_entry.get()
        qty = self.qty_entry.get()
        payout = self.payout_entry.get()
        profit = self.profit_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            # Execute SQL statement to find name
            cur.execute('SELECT * FROM Dindan WHERE order = ?', (orderid,))
            rows = cur.fetchone()
            # name not found
            if rows is None:
                # Execute the SQL statement to add
                cur.execute('INSERT INTO Dindan (customer, item, quantity, payout, profit)'
                            'SELECT ?, ?, ?, ?, ?',
                            (customerid, itemid, qty, payout,profit))
                tkinter.messagebox.showinfo('Notification', f'ATTENTION: '
                                                            f'\nAn entry for {orderid} has been added.')
            else:
                tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                        f'\n{orderid} is already in the customer database.')


    # Define the update function
    def update(self):
        # Get and store information
        orderid = self.orderid_entry.get()
        customerid = self.customerid_entry.get()
        itemid = self.itemid_entry.get()
        qty = self.qty_entry.get()
        payout = self.payout_entry.get()
        profit = self.profit_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            # Execute SQL statement to find id
            cur.execute('SELECT * FROM Dindan WHERE hao = ?', (orderid,))
            rows = cur.fetchone()
            # id not found
            if rows is None:
                tkinter.messagebox.showinfo('Notification', f'ERROR:'
                                                        f'\nEntry not found. Cannot update.'
                                                        f'\n\nPlease try again or add a new entry.')
            else:
                # Execute the SQL statement to update id
                cur.execute('UPDATE Dindan SET customer = ?, item = ?, quantity = ?, payout = ?, profit = ? WHERE hao = ?',
                            (customerid, itemid, qty, payout,profit, orderid))
                tkinter.messagebox.showinfo('Notification', f'ATTENTION: '
                                            f'\nThe entry for {orderid} has been updated.')


    # Define the delete function
    def delete(self):
        orderid = self.orderid_entry.get()

        with self.conn:
            cur = self.conn.cursor()
            # Execute SQL statement to find id
            cur.execute('SELECT * FROM Dindan WHERE hao = ?',
                        (orderid,))
            row = cur.fetchone()
            # id not found
            if row is None:
                tkinter.messagebox.showinfo('Notification', f'ATTENTION:'
                                                            f'\nEntry not found.')
            else:
                # execute the SQL statement to delete
                cur.execute('DELETE FROM Dindan WHERE hao = ?',
                            (orderid,))
                # Execute SQL statement to find id again
                cur.execute('SELECT * FROM Dindan WHERE hao = ?',
                            (orderid,))
                row = cur.fetchone()
                if row is None:
                    tkinter.messagebox.showinfo('Notification', f'ATTENTION:'
                                                                    f'\nThe order {orderid} has been deleted.')
                else:
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

                ttk.Button(self, text="View all the Order", command=self.showcustomer).grid(column=3, row=0)


            def showcustomer(self):
                self.listbox.delete(0, END)
                c.execute("""SELECT hao,'Customer ID: '
                                        ||customer, 'Item ID: '
                                        || item, 'Quantity: '
                                        || quantity,'Payout: '
                                        || payout,'Profit: '
                                        || profit FROM Dindan""")
                results = c.fetchall()
                for result in results:
                    self.listbox.insert(END, result)

        conn = lite.connect("WatchData.db")
        c = conn.cursor()

        root = tk.Tk()
        tree = ttk.Treeview(root)
        root.title("All Order")
        root.geometry("1000x1000")
        showall(root)
        root.mainloop()
        c.close()
        conn.close()


if __name__ == '__main__':
    show_order = Order()
    tkinter.mainloop()

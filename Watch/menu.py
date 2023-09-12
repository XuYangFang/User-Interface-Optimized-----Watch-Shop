#XuYang Fang
#05/09/2022

import tkinter
import tkinter.messagebox
import customer
import employee
import order
import inventory

# class Menu
class Menu:
    def __init__(self):
        #  main window
        self.main_window = tkinter.Tk()
        self.main_window.title('Watch Business Data')

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Top frame
        self.title = tkinter.Label(self.main_window, height=15, width=90,
                                        text='Main Menu', borderwidth=10, relief='sunken')
        self.title.pack(ipadx=10, ipady=10, pady=10)

        #   radio button
        self.rb_var = tkinter.IntVar()
        self.rb_var.set(1)
        self.rb_1 = tkinter.Radiobutton(self.top_frame, text='Customer',
                                        variable=self.rb_var, value=1, height=2, width=30)
        self.rb_2 = tkinter.Radiobutton(self.top_frame, text='Employee',
                                        variable=self.rb_var, value=2, height=2, width=30)
        self.rb_3 = tkinter.Radiobutton(self.top_frame, text='Order',
                                        variable=self.rb_var, value=3, height=2, width=30)
        self.rb_4 = tkinter.Radiobutton(self.top_frame, text='Inventory',
                                        variable=self.rb_var, value=4, height=2, width=30)
        self.rb_1.pack(padx=8, pady=8, ipadx=4, ipady=4)
        self.rb_2.pack(padx=8, pady=8, ipadx=4, ipady=4)
        self.rb_3.pack(padx=8, pady=8, ipadx=4, ipady=4)
        self.rb_4.pack(padx=8, pady=8, ipadx=4, ipady=4)

        #  bottom frame:
        self.choose_button = tkinter.Button(self.bottom_frame, text='Enter', command=self.decision)
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit Menu', command=self.main_window.destroy)
        self.choose_button.pack(side='left', padx=10, pady=10, ipadx=10, ipady=10)
        self.exit_button.pack(side='left', padx=10, pady=10, ipadx=10, ipady=10)

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    #  decision function
    def decision(self):
        if self.rb_var.get() == 1:
            c = customer.Customer()
        if self.rb_var.get() == 2:
            e = employee.Employee()
        if self.rb_var.get() == 3:
            o = order.Order()
        if self.rb_var.get() == 4:
            i = inventory.Inventory()

if __name__ == '__main__':
    show_menu = Menu()
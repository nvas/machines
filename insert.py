#!/usr/bin/python3
# main.py by Sajid Fadlelseed


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

from db import DB
import create_schema


class Machine:
    def __init__(self, machine_id, parts={}, oil={}):
        self.machine_id = machine_id
        self.parts = parts
        self.oil   = oil

class App:
    # database file name
    db_name ='machines.db'
    # path to this script
    cwd = os.getcwd()

    # App constructor
    def __init__(self, master):
        self.master = master
        self.title = 'App'
        master.resizable(False, False)
        master.configure(background = '#e1d8b9')
        self.parts_labels = []
        self.parts_entries = []
        self.oils_labels = []
        self.oils_entries = []
        # set App style
        self.set_style()
        
        # Frame A
        self.set_frameA()
        self.set_frameA_widgets()
        
        # Frame E
        self.set_frameE()
        self.set_frameE_widgets()

        # Frame C
        self.set_frameC()
        self.set_frameC_widgets()

        # Frame D
        self.set_frameD()
        self.set_frameD_widgets()        

        # Frame B
        self.set_frameB()
        self.set_frameB_widgets()


    # set widgtes style
    def set_style(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#e1d8b9')
        self.style.configure('TButton', background = '#e1d8b9')
        self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
        self.style.configure('Header.TLabel', background = '#e1d8b9', font = ('Arial', 18, 'bold'))

    # create frameA
    def set_frameA(self):
        self.frameA = ttk.Frame(self.master)
        self.frameA.pack()
    
    # create frameA widgets logo, header, and sub-header
    def set_frameA_widgets(self):
        ttk.Label(self.frameA, text = 'Insert Machine', style = 'Header.TLabel').grid(row = 1, column = 1)
        ttk.Label(self.frameA, text = '', style = 'Header.TLabel').grid(row = 2, column = 1)

    # create frameB
    def set_frameB(self):
        self.frameB = ttk.Frame(self.master)
        self.frameB.pack()
        
    # create frameB widgets search label, and search entry 
    def set_frameB_widgets(self):
        # ttk.Label(self.frameB, text = 'Machine #').grid(row = 0, column = 0, padx = 5, stick = 's')
        # self.entry_search = ttk.Entry(self.frameB, width = 24, font = ('Arial', 10))
        # self.entry_search.grid(row = 0, column = 1, padx = 5)
        ttk.Button(self.frameB, text= 'Insert', command = self.insert_button).grid(row = 1, column = 1, padx = 5)
        ttk.Button(self.frameB, text= 'Clear', command = self.clear_button).grid(row =2 , column = 1, padx = 5)

    # create frameC
    def set_frameC(self):
        self.frameC = ttk.Frame(self.master)
        self.frameC.pack()
        
    # create frameC widgets 8 label, and 8 entries
    def set_frameC_widgets(self):
        ttk.Label(self.frameC, text = 'Parts No:').grid(row = 0, column = 0, padx = 5)
        # create parts labels
        for i in range(1, 9):
            label = ttk.Label(self.frameC, text = f'{i}').grid(row = i, column = 0, padx = 1)
            self.parts_labels.append(label)
        # create parts text entries
        for i in range(1, 9):
            entry = ttk.Entry(self.frameC, width = 48, font = ('Arial', 10))
            entry.grid(row = i, column = 1, padx = 5, pady = 5, stick = 'w')
            self.parts_entries.append(entry)


    # create frameD
    def set_frameD(self):
        self.frameD = ttk.Frame(self.master)
        self.frameD.pack()
        
    # create frameD widgets 8 label, and 8 entries
    def set_frameD_widgets(self):

        ttk.Label(self.frameD, text = 'Oil          :').grid(row = 0, column = 0, padx = 5)
        # create parts labels
        for i in range(1, 9):
            label = ttk.Label(self.frameD, text = f'{i}').grid(row = i, column = 0, padx = 5)
            self.oils_labels.append(label)
        # create parts text entries
        for i in range(1, 9):
            entry = ttk.Entry(self.frameD, width = 48, font = ('Arial', 10))
            entry.grid(row = i, column = 1, padx = 5, pady = 5, stick = 'w')
            self.oils_entries.append(entry)
    

    # create frameE
    def set_frameE(self):
        self.frameE = ttk.Frame(self.master)
        self.frameE.pack()

    # create frameE widgets one Label andf one entry
    def set_frameE_widgets(self):
        ttk.Label(self.frameE, text = 'Machine #').grid(row = 0, column = 0, padx = 5)
        self.entry_insert = ttk.Entry(self.frameE, width = 24, font = ('Arial', 10))
        self.entry_insert.grid(row = 0, column = 1, padx = 5)

    # clear text entries
    def clear_button(self):
        self.entry_insert.delete(0, 'end')
        for i in range(0, len(self.parts_entries)):
            self.parts_entries[i].delete(0, 'end')
            self.oils_entries[i].delete(0, 'end')
        
    def insert_button(self):
        # init database connection
        object_db = DB(App.db_name)
        object_db.connect()
            

        # prepare machine data
        insert_machine = self.entry_insert.get()
        
        if insert_machine != '':
            # prepare parts data
            insert_parts = [x.get() for x in self.parts_entries]
            insert_parts = [(insert_machine, x) for x in insert_parts]

            # prepare oils data
            insert_oils = [x.get() for x in self.oils_entries]
            insert_oils = [(insert_machine, x) for x in insert_oils]

            # prepare machine query
            x_machine = f"INSERT INTO machines (name) VALUES (?)"

            # prepare parts query
            y_parts = f"INSERT INTO parts (machine_id, name) VALUES (?, ?)"

            # prepare oils query
            z_oils = f"INSERT INTO oils (machine_id, name) VALUES (?, ?)"

            object_db.insert_many(x_machine, insert_machine)
            object_db.insert_many(y_parts, insert_parts)
            object_db.insert_many(z_oils, insert_oils)
            messagebox.showinfo(title = 'X', message='Data Insertion Succeed!')

        else:
            messagebox.showerror(title = 'y', message='Data Insertion Failed!')

        # abort database connection 
        object_db.disconnect()
        
        



        
def main():            
    
        root = Tk()
        app = App(root)
        root.mainloop()
    
if __name__ == "__main__": main()

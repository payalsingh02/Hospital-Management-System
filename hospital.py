from cProfile import label
from cgitb import text
from ctypes import sizeof
from tkinter import *
from tkinter import ttk
import random
import datetime
import time
from tkinter import messagebox
from turtle import width
# import mysql.connector


class Hospital:
    def __init__ (self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1240x800+0+0")  # width and axis


        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=('times new roman',50,"bold"))
        lbltitle.pack(side=TOP, fill=X)

        #=========================Data Frame============================

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1375, height=360)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20,
                                                            font = ('arial', 12 , "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=840, height=310 )

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=20,
                                                            font = ('arial', 12 , "bold"), text="Prescription")
        DataframeRight.place(x=845, y=5, width=410, height=310 )

        #=========================Buttons Frame============================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=490, width=1375, height=70)

        #=========================Details Frame============================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=560, width=1375, height=145)

        #=============================DataframeLeft============================

        lblNameTablet = Label(DataframeLeft, text="Tablet Names", font = ('arial', 12 , "bold"),padx=2, pady=5)
        lblNameTablet.grid(row=0, column=0, sticky=W)

        comNametablet = ttk.Combobox(DataframeLeft, state='readonly', font = ('arial', 12 , "bold"),
                                                                                  width=31)
        comNametablet["values"] = ('Painkiller', 'corona Dose' ,'Vacacine', 'Ativan', 'Donafide', 'Adderall')
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1,  )

        lblref = Label(DataframeLeft, text="Reference no:", font = ('arial', 12 , "bold"),padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font = ('arial', 13 , "bold"), width=33)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, text="Dose: ", font = ('arial', 12 , "bold"),padx=2, pady=5)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font = ('arial', 13 , "bold"), width=33)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft, text="No of Tablets: ", font = ('arial', 12 , "bold"),padx=2, pady=4)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOfTablets = Entry(DataframeLeft, font = ('arial', 13 , "bold"), width=33)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Lot: ', padx=2,pady=5)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Issue Date', padx=2,pady=4)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Exp Date', padx=2,pady=4)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtExpDate.grid(row=6, column=1)

        lbldailyDose = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Daily Dose: ', padx=2,pady=4)
        lbldailyDose.grid(row=7, column=0, sticky=W)
        txtdailyDose = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtdailyDose.grid(row=7, column=1)

        lblsideEffect = Label(DataframeLeft, font = ('arial', 12, 'bold'), text='Side Effect: ', padx=2,pady=4)
        lblsideEffect.grid(row=8, column=0, sticky=W)
        txtsideEffect = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtsideEffect.grid(row=8, column=1)

        lblfurtherInfo = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' Further Info:', padx=2,pady=4)
        lblfurtherInfo.grid(row=0, column=2, sticky=W)
        txtfurtherInfo = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtfurtherInfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' Blood Pressure:', padx=2,pady=4)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtBloodPressure.grid(row=1, column=3)

        lblstorageAdvice = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' Storage Advice:', padx=2,pady=4)
        lblstorageAdvice.grid(row=2, column=2, sticky=W)
        txtstorageAdvice = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtstorageAdvice.grid(row=2, column=3)

        lblMedication = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' Medication:', padx=2,pady=4)
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtMedication.grid(row=3, column=3)

        lblPID = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' Patient ID:', padx=2,pady=4)
        lblPID.grid(row=4, column=2, sticky=W)
        txtPID = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtPID.grid(row=4, column=3)

        lblNHSnumber = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' NHS Number:', padx=2,pady=4)
        lblNHSnumber.grid(row=5, column=2, sticky=W)
        txtNHSnumber = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtNHSnumber.grid(row=5, column=3)

        lblPName = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' Patient Name:', padx=2,pady=4)
        lblPName.grid(row=6, column=2, sticky=W)
        txtPName = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtPName.grid(row=6, column=3)
        
        lblDOB = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' Date Of Birth:', padx=2,pady=4)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtDOB.grid(row=7, column=3)

        lblPaddress = Label(DataframeLeft, font = ('arial', 12, 'bold'), text=' Patient Address:', padx=2,pady=4)
        lblPaddress.grid(row=8, column=2, sticky=W)
        txtPaddress = Entry(DataframeLeft, font = ('arial', 13, 'bold'), width=33)
        txtPaddress.grid(row=8, column=3)









root=Tk()
ob=Hospital(root)
root.mainloop()

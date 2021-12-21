from tkinter.constants import LEFT, TOP
import pyodbc 
from tkinter import *
import os
from tkinter import ttk
import tkinter as tk
from datetime import date
from tkinter import messagebox

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-QDT87ER;'
                      'Database=HRMS;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

root = Tk()
			
root.geometry('900x500')	
root.title("Welcome to HR Management System")
Label(root, text ="HRMS System", font=150).pack()

class Applicant(object):
    def ViewApplicant(self):
        newWindow = Toplevel(root)
        newWindow.title("View Applicants")
        newWindow.geometry("1100x500")
        Label(newWindow, text ="View Applicants", font=50).pack()
        
        tree = ttk.Treeview(newWindow, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')

        tree.column("#1", anchor=tk.CENTER, width=30)

        tree.heading("#1", text="ID")

        tree.column("#2", anchor=tk.CENTER, width=80)

        tree.heading("#2", text="Name")

        tree.column("#3", anchor=tk.CENTER, width=80)

        tree.heading("#3", text="CNIC")

        tree.column("#4", anchor=tk.CENTER, width=80)

        tree.heading("#4", text="Email")

        tree.column("#5", anchor=tk.CENTER, width=80)

        tree.heading("#5", text="Qualification")

        tree.column("#6", anchor=tk.CENTER, width=80)

        tree.heading("#6", text="City")

        tree.column("#7", anchor=tk.CENTER, width=80)

        tree.heading("#7", text="Sex")

        tree.column("#8", anchor=tk.CENTER, width=80)

        tree.heading("#8", text="Submission Date")
        tree.pack()
        scroll_bar = Scrollbar(newWindow)
  
        scroll_bar.pack(side = RIGHT,fill = Y)

        cursor.execute("SELECT ap_id, Name, CNIC, email, Qualification, City, Sex, submission_date FROM Applicant")
        
        rows = cursor.fetchall()    

        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)
            scroll_bar.config( command = tree.yview )

    def __init__(self):
        self.apid = StringVar()
        self.name = StringVar()
        self.cnic = StringVar()
        self.contact = StringVar()
        self.email = StringVar()
        self.qual = StringVar()
        self.city = StringVar()
        self.address = StringVar()
        self.sex = StringVar()

    def AddApplicant(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Applicant")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Add Applicant", font=50).pack()
        
        Label(newWindow, text="Applicant ID:").place(x=100, y=20)
        Label(newWindow, text="Name:").place(x=100, y=60)
        Label(newWindow, text="CNIC:").place(x=100, y=100)
        Label(newWindow, text="Contact:").place(x=100, y=140)
        Label(newWindow, text="Email:").place(x=100, y=180)
        Label(newWindow, text="Qualification:").place(x=100, y=220)
        Label(newWindow, text="City:").place(x=100, y=260)
        Label(newWindow, text="Address:").place(x=100, y=300)
        Label(newWindow, text="Sex:").place(x=100, y=340)
        Label(newWindow, text="Submission Date:").place(x=100, y=380)

        api = Entry(newWindow, textvariable=self.apid)
        nam = Entry(newWindow, textvariable=self.name)
        cni = Entry(newWindow, textvariable=self.cnic)
        cont = Entry(newWindow, textvariable=self.contact)
        em = Entry(newWindow, textvariable=self.email)
        qualif = Entry(newWindow, textvariable=self.qual)
        cit = Entry(newWindow, textvariable=self.city)
        add = Entry(newWindow, textvariable=self.address)
        se = Entry(newWindow, textvariable=self.sex)

        api.place(x=200, y=20)
        nam.place(x=200, y=60)
        cni.place(x=200, y=100)
        cont.place(x=200, y=140)
        em.place(x=200, y=180)
        qualif.place(x=200, y=220)
        cit.place(x=200, y=260)
        add.place(x=200, y=300)
        se.place(x=200, y=340)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitApplicant)
        submit.place(x=200,y=420) 

    def SubmitApplicant(self):
        try: 
            today = date.today()
            cursor.execute("INSERT INTO Applicant(ap_id, Name, CNIC, Contact, email, Qualification, City, Address, Sex, submission_date) values (?,?,?,?,?,?,?,?,?,?)", self.apid.get(), self.name.get(), self.cnic.get(), self.contact.get(), self.email.get(),self.qual.get(), self.city.get(), self.address.get(), self.sex.get(), today.strftime("%Y/%m/%d"))
            conn.commit()
            messagebox.showinfo("Record Inserted", "Record inserted Succesfully" )
            print(cursor.rowcount, "record inserted.")
        except:
            messagebox.showerror("Record Not Inserted", "Error inserting Record" )

    def DeleteApplicant(self):
        newWindow = Toplevel(root)
        newWindow.title("Delete Applicant")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Delete Applicant", font=50).pack()

        Label(newWindow, text="Applicant ID:").place(x=100, y=40)
        
        aid = Entry(newWindow, textvariable=self.apid)
        aid.place(x=200, y=40)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitDeleteApplicant)
        submit.place(x=200,y=80) 

    def SubmitDeleteApplicant(self):
        try: 
            cursor.execute("DELETE FROM Applicant WHERE ap_id = ?", self.apid.get())
            conn.commit()
            messagebox.showinfo("Record Deleted", "Record Deleted Succesfully" )
            print(cursor.rowcount, "record Deleted.")
        except:
            messagebox.showerror("Record Not Deleted", "Error Deleting Record" )

    def UpdateApplicant(self):
        newWindow = Toplevel(root)
        newWindow.title("Update Applicant")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Update Applicant", font=50).pack()

        Label(newWindow, text="Applicant ID:").place(x=100, y=20)
        Label(newWindow, text="Name:").place(x=100, y=60)
        Label(newWindow, text="CNIC:").place(x=100, y=100)
        Label(newWindow, text="Contact:").place(x=100, y=140)
        Label(newWindow, text="Email:").place(x=100, y=180)
        Label(newWindow, text="Qualification:").place(x=100, y=220)
        Label(newWindow, text="City:").place(x=100, y=260)
        Label(newWindow, text="Address:").place(x=100, y=300)
        Label(newWindow, text="Sex:").place(x=100, y=340)
        Label(newWindow, text="Submission Date:").place(x=100, y=380)

        api = Entry(newWindow, textvariable=self.apid)
        nam = Entry(newWindow, textvariable=self.name)
        cni = Entry(newWindow, textvariable=self.cnic)
        cont = Entry(newWindow, textvariable=self.contact)
        em = Entry(newWindow, textvariable=self.email)
        qualif = Entry(newWindow, textvariable=self.qual)
        cit = Entry(newWindow, textvariable=self.city)
        add = Entry(newWindow, textvariable=self.address)
        se = Entry(newWindow, textvariable=self.sex)

        api.place(x=200, y=20)
        nam.place(x=200, y=60)
        cni.place(x=200, y=100)
        cont.place(x=200, y=140)
        em.place(x=200, y=180)
        qualif.place(x=200, y=220)
        cit.place(x=200, y=260)
        add.place(x=200, y=300)
        se.place(x=200, y=340)
        
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitUpdatedApplicant)
        submit.place(x=200,y=420) 

    def SubmitUpdatedApplicant(self):
        try: 
            today = date.today()
            cursor.execute("UPDATE Applicant SET Name = ?, CNIC = ?, Contact = ?, email = ?, Qualification = ?, City = ?, Address = ?, Sex = ?, submission_date = ? WHERE ap_id = ?", self.name.get(), self.cnic.get(), self.contact.get(), self.email.get(),self.qual.get(), self.city.get(), self.address.get(), self.sex.get(), today.strftime("%Y/%m/%d"), self.apid.get())
            conn.commit()
            messagebox.showinfo("Record Updated", "Record Updated Succesfully" )
            print(cursor.rowcount, "record Updated.")
        except:
            messagebox.showerror("Record Not Updated", "Error Updating Record" )


class Attendance(object):
    def ViewAttendance(self):
        newWindow = Toplevel(root)
        newWindow.title("View Attendance")
        newWindow.geometry("1100x550")
        Label(newWindow, text ="View Attendance", font=50).pack()
        
        tree = ttk.Treeview(newWindow, column=("c1", "c2", "c3", "c4", "c5"), show='headings')

        tree.column("#1", anchor=tk.CENTER)

        tree.heading("#1", text="Attendance ID")

        tree.column("#2", anchor=tk.CENTER)

        tree.heading("#2", text="Date")

        tree.column("#3", anchor=tk.CENTER)

        tree.heading("#3", text="Employee ID")

        tree.column("#4", anchor=tk.CENTER)

        tree.heading("#4", text="Status")

        tree.column("#5", anchor=tk.CENTER)

        tree.heading("#5", text="Absents")
        tree.pack()
        scroll_bar = Scrollbar(newWindow)
  
        scroll_bar.pack(side = RIGHT,fill = Y)

        cursor.execute("SELECT * FROM Attendence")
        
        rows = cursor.fetchall()    

        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)
            scroll_bar.config( command = tree.yview )

    def __init__(self):
        self.atid = StringVar()
        self.etid = StringVar()
        self.status = StringVar()
        self.absents = StringVar()

    def AddAttendance(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Attendance")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Add Attendance", font=50).pack()
        
        Label(newWindow, text="Attendance ID:").place(x=100, y=20)
        Label(newWindow, text="Employee ID:").place(x=100, y=60)
        Label(newWindow, text="Status:").place(x=100, y=100)
        Label(newWindow, text="Absents:").place(x=100, y=140)
        
        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)
        absents = Entry(newWindow, textvariable=self.absents)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        absents.place(x=200, y=140)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitAttendance)
        submit.place(x=200,y=200) 

    def SubmitAttendance(self):
        try: 
            today = date.today()
            cursor.execute("INSERT INTO Attendence(at_id, Date, emp_id, Status, Absents) values (?,?,?,?,?)", self.atid.get(), today.strftime("%Y/%m/%d"),self.etid.get(), self.status.get(), self.absents.get())
            conn.commit()
            messagebox.showinfo("Record Inserted", "Record inserted Succesfully" )
            print(cursor.rowcount, "record inserted.")
        except:
            messagebox.showerror("Record Not Inserted", "Error inserting Record" )

    def DeleteAttendance(self):
        newWindow = Toplevel(root)
        newWindow.title("Delete Attendance")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Delete Attendance", font=50).pack()

        Label(newWindow, text="Attendance ID:").place(x=100, y=40)
        
        aid = Entry(newWindow, textvariable=self.atid)
        aid.place(x=200, y=40)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitDeleteAttendance)
        submit.place(x=200,y=80) 

    def SubmitDeleteAttendance(self):
        try: 
            cursor.execute("DELETE FROM Attendence WHERE at_id = ?", self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Deleted", "Record Deleted Succesfully" )
            print(cursor.rowcount, "record Deleted.")
        except:
            messagebox.showerror("Record Not Deleted", "Error Deleting Record" )

    def UpdateAttendance(self):
        newWindow = Toplevel(root)
        newWindow.title("Update Attendance")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Update Attendance", font=50).pack()

        Label(newWindow, text="Attendance ID:").place(x=100, y=20)
        Label(newWindow, text="Employee ID:").place(x=100, y=60)
        Label(newWindow, text="Status:").place(x=100, y=100)
        Label(newWindow, text="Absents:").place(x=100, y=140)
        
        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)
        absents = Entry(newWindow, textvariable=self.absents)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        absents.place(x=200, y=140)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitUpdatedAttendance)
        submit.place(x=200,y=200) 

    def SubmitUpdatedAttendance(self):
        try: 
            today = date.today()
            cursor.execute("UPDATE Attendence SET Date = ?, emp_id = ?, Status = ?, Absents = ? WHERE at_id = ?", today.strftime("%Y/%m/%d"),self.etid.get(), self.status.get(), self.absents.get(),self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Updated", "Record Updated Succesfully" )
            print(cursor.rowcount, "record Updated.")
        except:
            messagebox.showerror("Record Not Updated", "Error Updating Record" )


class Employee(object):
    def ViewEmployee(self):
        newWindow = Toplevel(root)
        newWindow.title("View Employee")
        newWindow.geometry("1100x550")
        Label(newWindow, text ="View Employee", font=50).pack()
        
        tree = ttk.Treeview(newWindow, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"), show='headings')

        tree.column("#1", anchor=tk.CENTER, width=30)

        tree.heading("#1", text="ID")

        tree.column("#2", anchor=tk.CENTER, width=80)

        tree.heading("#2", text="Name")

        tree.column("#3", anchor=tk.CENTER, width=80)

        tree.heading("#3", text="CNIC")

        tree.column("#4", anchor=tk.CENTER, width=80)

        tree.heading("#4", text="Designation")

        tree.column("#5", anchor=tk.CENTER, width=80)

        tree.heading("#5", text="Join Date")

        tree.column("#6", anchor=tk.CENTER, width=80)

        tree.heading("#6", text="Birth Date")

        tree.column("#7", anchor=tk.CENTER, width=80)

        tree.heading("#7", text="City")

        tree.column("#8", anchor=tk.CENTER, width=80)

        tree.heading("#8", text="Sex")

        tree.column("#9", anchor=tk.CENTER, width=80)

        tree.heading("#9", text="Sal ID")

        tree.column("#10", anchor=tk.CENTER, width=80)

        tree.heading("#10", text="Vac ID")

        tree.pack()
        scroll_bar = Scrollbar(newWindow)
  
        scroll_bar.pack(side = RIGHT,fill = Y)

        cursor.execute("SELECT emp_id, Name, CNIC, Designation, Join_Date, Birth_Date, City, Sex, salary_id, vac_id FROM Employee")
        
        rows = cursor.fetchall()    

        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)
            scroll_bar.config( command = tree.yview )

    def __init__(self):
        self.eid = StringVar()
        self.name = StringVar()
        self.cnic = StringVar()
        self.contact = StringVar()
        self.design = StringVar()
        self.jdate = StringVar()
        self.bdate = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.sex = StringVar()
        self.sid = StringVar()
        self.vid = StringVar()

    def AddEmployee(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Employee")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Add Employee", font=50).pack()
        Label(newWindow, text="Employee ID:").place(x=100, y=20)
        Label(newWindow, text="Name:").place(x=100, y=60)
        Label(newWindow, text="CNIC:").place(x=100, y=100)
        Label(newWindow, text="Contact:").place(x=100, y=140)
        Label(newWindow, text="Designation:").place(x=100, y=180)
        Label(newWindow, text="Join Date:").place(x=100, y=220)
        Label(newWindow, text="Birth Date:").place(x=100, y=260)
        Label(newWindow, text="Address:").place(x=100, y=300)
        Label(newWindow, text="City:").place(x=100, y=340)
        Label(newWindow, text="Sex:").place(x=100, y=380)
        Label(newWindow, text="Salary ID:").place(x=100, y=420)
        Label(newWindow, text="Vac ID:").place(x=100, y=460)

        ei = Entry(newWindow, textvariable=self.eid)
        nam = Entry(newWindow, textvariable=self.name)
        cni = Entry(newWindow, textvariable=self.cnic)
        cont = Entry(newWindow, textvariable=self.contact)
        des = Entry(newWindow, textvariable=self.design)
        jd = Entry(newWindow, textvariable=self.jdate)
        bd = Entry(newWindow, textvariable=self.bdate)
        add = Entry(newWindow, textvariable=self.address)
        cit = Entry(newWindow, textvariable=self.city)
        se = Entry(newWindow, textvariable=self.sex)
        sd = Entry(newWindow, textvariable=self.sid)
        vd = Entry(newWindow, textvariable=self.vid)

        ei.place(x=200, y=20)
        nam.place(x=200, y=60)
        cni.place(x=200, y=100)
        cont.place(x=200, y=140)
        des.place(x=200, y=180)
        jd.place(x=200, y=220)
        bd.place(x=200, y=260)
        add.place(x=200, y=300)
        cit.place(x=200, y=340)
        se.place(x=200, y=380)
        sd.place(x=200, y=420)
        vd.place(x=200, y=460)
        
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitEmployee)
        submit.place(x=200,y=500) 

    def SubmitEmployee(self):
        try: 
            today = date.today()
            cursor.execute("INSERT INTO Employee(emp_id, Name, CNIC, Contact, Designation, Join_Date, Birth_Date, Address, City, Sex, salary_id, vac_id) values (?,?,?,?,?,?,?,?,?,?,?,?)", self.eid.get(), self.name.get(), self.cnic.get(), self.contact.get(), self.design.get(), self.jdate.get(), self.bdate.get(), self.address.get(), self.city.get(), self.sex.get(), self.sid.get(), self.vid.get())
            conn.commit()
            messagebox.showinfo("Record Inserted", "Record inserted Succesfully" )
            print(cursor.rowcount, "record inserted.")
        except:
            messagebox.showerror("Record Not Inserted", "Error inserting Record" )

    def DeleteEmployee(self):
        newWindow = Toplevel(root)
        newWindow.title("Delete Employee")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Delete Employee", font=50).pack()

        Label(newWindow, text="Employee ID:").place(x=100, y=40)
        
        aid = Entry(newWindow, textvariable=self.eid)
        aid.place(x=200, y=40)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitDeleteEmployee)
        submit.place(x=200,y=80) 

    def SubmitDeleteEmployee(self):
        try: 
            cursor.execute("DELETE FROM Employee WHERE emp_id = ?", self.eid.get())
            conn.commit()
            messagebox.showinfo("Record Deleted", "Record Deleted Succesfully" )
            print(cursor.rowcount, "record Deleted.")
        except:
            messagebox.showerror("Record Not Deleted", "Error Deleting Record" )

    def UpdateEmployee(self):
        newWindow = Toplevel(root)
        newWindow.title("Update Employee")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Update Employee", font=50).pack()

        Label(newWindow, text="Employee ID:").place(x=100, y=20)
        Label(newWindow, text="Name:").place(x=100, y=60)
        Label(newWindow, text="CNIC:").place(x=100, y=100)
        Label(newWindow, text="Contact:").place(x=100, y=140)
        Label(newWindow, text="Designation:").place(x=100, y=180)
        Label(newWindow, text="Join Date:").place(x=100, y=220)
        Label(newWindow, text="Birth Date:").place(x=100, y=260)
        Label(newWindow, text="Address:").place(x=100, y=300)
        Label(newWindow, text="City:").place(x=100, y=340)
        Label(newWindow, text="Sex:").place(x=100, y=380)
        Label(newWindow, text="Salary ID:").place(x=100, y=420)
        Label(newWindow, text="Vac ID:").place(x=100, y=460)

        ei = Entry(newWindow, textvariable=self.eid)
        nam = Entry(newWindow, textvariable=self.name)
        cni = Entry(newWindow, textvariable=self.cnic)
        cont = Entry(newWindow, textvariable=self.contact)
        des = Entry(newWindow, textvariable=self.design)
        jd = Entry(newWindow, textvariable=self.jdate)
        bd = Entry(newWindow, textvariable=self.bdate)
        add = Entry(newWindow, textvariable=self.address)
        cit = Entry(newWindow, textvariable=self.city)
        se = Entry(newWindow, textvariable=self.sex)
        sd = Entry(newWindow, textvariable=self.sid)
        vd = Entry(newWindow, textvariable=self.vid)

        ei.place(x=200, y=20)
        nam.place(x=200, y=60)
        cni.place(x=200, y=100)
        cont.place(x=200, y=140)
        des.place(x=200, y=180)
        jd.place(x=200, y=220)
        bd.place(x=200, y=260)
        add.place(x=200, y=300)
        cit.place(x=200, y=340)
        se.place(x=200, y=380)
        sd.place(x=200, y=420)
        vd.place(x=200, y=460)
        
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitUpdatedEmployee)
        submit.place(x=200,y=500) 

    def SubmitUpdatedEmployee(self):
        try: 
            today = date.today()
            cursor.execute("UPDATE Employee SET emp_id = ?, Name = ?, CNIC = ?, Contact = ?, Designation = ?, Join_Date = ?, Birth_Date = ?, Address = ?, City = ?, Sex = ?, salary_id = ?, vac_id = ? WHERE emp_id = ?", self.name.get(), self.cnic.get(), self.contact.get(), self.design.get(), self.jdate.get(), self.bdate.get(), self.address.get(), self.city.get(), self.sex.get(), self.sid.get(), self.vid.get(), self.eid.get())
            conn.commit()
            messagebox.showinfo("Record Updated", "Record Updated Succesfully" )
            print(cursor.rowcount, "record Updated.")
        except:
            messagebox.showerror("Record Not Updated", "Error Updating Record" )

class Interview(object):
    def ViewInterview(self):
        newWindow = Toplevel(root)
        newWindow.title("View Interview")
        newWindow.geometry("1100x550")
        Label(newWindow, text ="View Interview", font=50).pack()
        
        tree = ttk.Treeview(newWindow, column=("c1", "c2", "c3", "c4", "c5"), show='headings')

        tree.column("#1", anchor=tk.CENTER, width=30)

        tree.heading("#1", text="ID")

        tree.column("#2", anchor=tk.CENTER, width=80)

        tree.heading("#2", text="Selection Round")

        tree.column("#3", anchor=tk.CENTER, width=80)

        tree.heading("#3", text="Status")

        tree.column("#4", anchor=tk.CENTER, width=80)

        tree.heading("#4", text="Date")

        tree.column("#5", anchor=tk.CENTER, width=80)

        tree.heading("#5", text="Vac ID")

        tree.pack()
        scroll_bar = Scrollbar(newWindow)
  
        scroll_bar.pack(side = RIGHT,fill = Y)

        cursor.execute("SELECT * FROM Interview")
        
        rows = cursor.fetchall()    

        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)
            scroll_bar.config( command = tree.yview )

    def __init__(self):
        self.eid = StringVar()
        self.name = StringVar()
        self.cnic = StringVar()
        self.contact = StringVar()
       

    def AddInterview(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Interview")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Add Interview", font=50).pack()

        Label(newWindow, text="Interview ID:").place(x=100, y=20)
        Label(newWindow, text="Selection Round:").place(x=100, y=60)
        Label(newWindow, text="Status:").place(x=100, y=100)
        Label(newWindow, text="Vac ID:").place(x=100, y=140)
        
        ei = Entry(newWindow, textvariable=self.eid)
        nam = Entry(newWindow, textvariable=self.name)
        cni = Entry(newWindow, textvariable=self.cnic)
        cont = Entry(newWindow, textvariable=self.contact)

        ei.place(x=200, y=20)
        nam.place(x=200, y=60)
        cni.place(x=200, y=100)
        cont.place(x=200, y=140)
       
        submit = Button(newWindow, text = 'Submit', command = self.SubmitInterview)
        submit.place(x=200,y=180) 

    def SubmitInterview(self):
        try: 
            today = date.today()
            cursor.execute("INSERT INTO Interview(Interview_id, selectionround, status, date, vac_id) values (?,?,?,?,?)", self.eid.get(), self.name.get(), self.cnic.get(), today.strftime("%Y/%m/%d"), self.contact.get())
            conn.commit()
            messagebox.showinfo("Record Inserted", "Record inserted Succesfully" )
            print(cursor.rowcount, "record inserted.")
        except:
            messagebox.showerror("Record Not Inserted", "Error inserting Record" )

    def DeleteInterview(self):
        newWindow = Toplevel(root)
        newWindow.title("Delete Interview")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Delete Interview", font=50).pack()

        Label(newWindow, text="Interview ID:").place(x=100, y=40)
        
        aid = Entry(newWindow, textvariable=self.eid)
        aid.place(x=200, y=40)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitDeleteInterview)
        submit.place(x=200,y=80) 

    def SubmitDeleteInterview(self):
        try: 
            cursor.execute("DELETE FROM Interview WHERE Interview_id = ?", self.eid.get())
            conn.commit()
            messagebox.showinfo("Record Deleted", "Record Deleted Succesfully" )
            print(cursor.rowcount, "record Deleted.")
        except:
            messagebox.showerror("Record Not Deleted", "Error Deleting Record" )

    def UpdateInterview(self):
        newWindow = Toplevel(root)
        newWindow.title("Update Interview")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Update Interview", font=50).pack()

       
        Label(newWindow, text="Interview ID:").place(x=100, y=20)
        Label(newWindow, text="Selection Round:").place(x=100, y=60)
        Label(newWindow, text="Status:").place(x=100, y=100)
        Label(newWindow, text="Vac ID:").place(x=100, y=140)
        
        ei = Entry(newWindow, textvariable=self.eid)
        nam = Entry(newWindow, textvariable=self.name)
        cni = Entry(newWindow, textvariable=self.cnic)
        cont = Entry(newWindow, textvariable=self.contact)

        ei.place(x=200, y=20)
        nam.place(x=200, y=60)
        cni.place(x=200, y=100)
        cont.place(x=200, y=140)
        
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitUpdatedInterview)
        submit.place(x=200,y=180) 

    def SubmitUpdatedInterview(self):
        try: 
            today = date.today()
            cursor.execute("UPDATE Interview SET selectionround = ?, status = ?, date = ?, vac_id = ? where Interview_id = ?", self.name.get(), self.cnic.get(), today.strftime("%Y/%m/%d"), self.contact.get(), self.eid.get())
            conn.commit()
            messagebox.showinfo("Record Updated", "Record Updated Succesfully" )
            print(cursor.rowcount, "record Updated.")
        except:
            messagebox.showerror("Record Not Updated", "Error Updating Record" )



class Project(object):
    def ViewProject(self):
        newWindow = Toplevel(root)
        newWindow.title("View Project")
        newWindow.geometry("1100x550")
        Label(newWindow, text ="View Project", font=50).pack()
        
        tree = ttk.Treeview(newWindow, column=("c1", "c2", "c3", "c4", "c5"), show='headings')

        tree.column("#1", anchor=tk.CENTER)

        tree.heading("#1", text="Project ID")

        tree.column("#2", anchor=tk.CENTER)

        tree.heading("#2", text="Title")

        tree.column("#3", anchor=tk.CENTER)

        tree.heading("#3", text="Start Date")

        tree.column("#4", anchor=tk.CENTER)

        tree.heading("#4", text="End Date")

        tree.column("#5", anchor=tk.CENTER)

        tree.heading("#5", text="Employee ID")
        tree.pack()
        scroll_bar = Scrollbar(newWindow)
  
        scroll_bar.pack(side = RIGHT,fill = Y)

        cursor.execute("SELECT * FROM Project")
        
        rows = cursor.fetchall()    

        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)
            scroll_bar.config( command = tree.yview )

    def __init__(self):
        self.atid = StringVar()
        self.etid = StringVar()
        self.status = StringVar()
        self.absents = StringVar()
        self.emp = StringVar()

    def AddProject(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Project")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Add Project", font=50).pack()
        
        Label(newWindow, text="Attendance ID:").place(x=100, y=20)
        Label(newWindow, text="Employee ID:").place(x=100, y=60)
        Label(newWindow, text="Status:").place(x=100, y=100)
        Label(newWindow, text="Absents:").place(x=100, y=140)
        Label(newWindow, text="Absents:").place(x=100, y=180)

        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)
        absents = Entry(newWindow, textvariable=self.absents)
        empid = Entry(newWindow, textvariable=self.emp)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        absents.place(x=200, y=140)
        empid.place(x=200, y=180)

        submit = Button(newWindow, text = 'Submit', command = self.SubmitProject)
        submit.place(x=200,y=220) 

    def SubmitProject(self):
        try: 
            today = date.today()
            cursor.execute("INSERT INTO Project(project_id, title, start_date, end_date, emp_id) values (?,?,?,?,?)", self.atid.get(),self.etid.get(), self.status.get(), self.absents.get(), self.emp.get())
            conn.commit()
            messagebox.showinfo("Record Inserted", "Record inserted Succesfully" )
            print(cursor.rowcount, "record inserted.")
        except:
            messagebox.showerror("Record Not Inserted", "Error inserting Record" )

    def DeleteProject(self):
        newWindow = Toplevel(root)
        newWindow.title("Delete Project")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Delete Project", font=50).pack()

        Label(newWindow, text="Project ID:").place(x=100, y=40)
        
        aid = Entry(newWindow, textvariable=self.atid)
        aid.place(x=200, y=40)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitDeleteProject)
        submit.place(x=200,y=80) 

    def SubmitDeleteProject(self):
        try: 
            cursor.execute("DELETE FROM Project WHERE project_id = ?", self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Deleted", "Record Deleted Succesfully" )
            print(cursor.rowcount, "record Deleted.")
        except:
            messagebox.showerror("Record Not Deleted", "Error Deleting Record" )

    def UpdateProject(self):
        newWindow = Toplevel(root)
        newWindow.title("Update Project")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Update Project", font=50).pack()

        Label(newWindow, text="Attendance ID:").place(x=100, y=20)
        Label(newWindow, text="Employee ID:").place(x=100, y=60)
        Label(newWindow, text="Status:").place(x=100, y=100)
        Label(newWindow, text="Absents:").place(x=100, y=140)
        Label(newWindow, text="Absents:").place(x=100, y=180)

        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)
        absents = Entry(newWindow, textvariable=self.absents)
        empid = Entry(newWindow, textvariable=self.emp)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        absents.place(x=200, y=140)
        empid.place(x=200, y=180)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitUpdatedProject)
        submit.place(x=200,y=220) 

    def SubmitUpdatedProject(self):
        try: 
            today = date.today()
            cursor.execute("UPDATE Project SET title = ?, start_date = ?, end_date = ?, emp_id = ? WHERE project_id = ?", self.etid.get(), self.status.get(), self.absents.get(), self.emp.get(), self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Updated", "Record Updated Succesfully" )
            print(cursor.rowcount, "record Updated.")
        except:
            messagebox.showerror("Record Not Updated", "Error Updating Record" )

class ProjectStatus(object):
    def ViewProjectStatus(self):
        newWindow = Toplevel(root)
        newWindow.title("View Project Status")
        newWindow.geometry("1100x550")
        Label(newWindow, text ="View Project Status", font=50).pack()
        
        tree = ttk.Treeview(newWindow, column=("c1", "c2", "c3"), show='headings')

        tree.column("#1", anchor=tk.CENTER)

        tree.heading("#1", text="Project ID")

        tree.column("#2", anchor=tk.CENTER)

        tree.heading("#2", text="Status")

        tree.column("#3", anchor=tk.CENTER)

        tree.heading("#3", text="Expected Completion Date")

        tree.pack()
        scroll_bar = Scrollbar(newWindow)
  
        scroll_bar.pack(side = RIGHT,fill = Y)

        cursor.execute("SELECT * FROM Project_status")
        
        rows = cursor.fetchall()    

        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)
            scroll_bar.config( command = tree.yview )

    def __init__(self):
        self.atid = StringVar()
        self.etid = StringVar()
        self.status = StringVar()

    def AddProjectStatus(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Project Status")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Add Project Status", font=50).pack()
        
        Label(newWindow, text="Project ID:").place(x=100, y=20)
        Label(newWindow, text="Status:").place(x=100, y=60)
        Label(newWindow, text="Expected Completion Date:").place(x=100, y=100)
        
        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitProjectStatus)
        submit.place(x=200,y=140) 

    def SubmitProjectStatus(self):
        try: 
            today = date.today()
            cursor.execute("INSERT INTO Attendence(project_id, Status, Expected_Completion_date) values (?,?,?)", self.atid.get(), self.etid.get(), self.status.get())
            conn.commit()
            messagebox.showinfo("Record Inserted", "Record inserted Succesfully" )
            print(cursor.rowcount, "record inserted.")
        except:
            messagebox.showerror("Record Not Inserted", "Error inserting Record" )

    def DeleteProjectStatus(self):
        newWindow = Toplevel(root)
        newWindow.title("Delete Project Status")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Delete Project Status", font=50).pack()

        Label(newWindow, text="Project ID:").place(x=100, y=40)
        
        aid = Entry(newWindow, textvariable=self.atid)
        aid.place(x=200, y=40)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitDeleteProjectStatus)
        submit.place(x=200,y=80) 

    def SubmitDeleteProjectStatus(self):
        try: 
            cursor.execute("DELETE FROM Project_status WHERE project_id = ?", self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Deleted", "Record Deleted Succesfully" )
            print(cursor.rowcount, "record Deleted.")
        except:
            messagebox.showerror("Record Not Deleted", "Error Deleting Record" )

    def UpdateProjectStatus(self):
        newWindow = Toplevel(root)
        newWindow.title("Update Project Status")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Update Project Status", font=50).pack()

        Label(newWindow, text="Project ID:").place(x=100, y=20)
        Label(newWindow, text="Status:").place(x=100, y=60)
        Label(newWindow, text="Expected Completion Date:").place(x=100, y=100)
        
        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitUpdatedProjectStatus)
        submit.place(x=200,y=140) 

    def SubmitUpdatedProjectStatus(self):
        try: 
            today = date.today()
            cursor.execute("UPDATE Project_status SET Status = ?, Expected_Completion_date = ? WHERE project_id = ?", self.etid.get(), self.status.get(), self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Updated", "Record Updated Succesfully" )
            print(cursor.rowcount, "record Updated.")
        except:
            messagebox.showerror("Record Not Updated", "Error Updating Record" )


class Salary(object):
    def ViewSalary(self):
        newWindow = Toplevel(root)
        newWindow.title("View Salary")
        newWindow.geometry("1100x550")
        Label(newWindow, text ="View Salary", font=50).pack()
        
        tree = ttk.Treeview(newWindow, column=("c1", "c2", "c3"), show='headings')

        tree.column("#1", anchor=tk.CENTER)

        tree.heading("#1", text="Salary ID")

        tree.column("#2", anchor=tk.CENTER)

        tree.heading("#2", text="Basic Pay")

        tree.column("#3", anchor=tk.CENTER)

        tree.heading("#3", text="Allowance")

        tree.pack()
        scroll_bar = Scrollbar(newWindow)
  
        scroll_bar.pack(side = RIGHT,fill = Y)

        cursor.execute("SELECT * FROM Salary")
        
        rows = cursor.fetchall()    

        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)
            scroll_bar.config( command = tree.yview )

    def __init__(self):
        self.atid = StringVar()
        self.etid = StringVar()
        self.status = StringVar()

    def AddSalary(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Salary")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Add Salary", font=50).pack()
        
        Label(newWindow, text="Salary ID:").place(x=100, y=20)
        Label(newWindow, text="Basic Pay:").place(x=100, y=60)
        Label(newWindow, text="Allowance:").place(x=100, y=100)
        
        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitSalary)
        submit.place(x=200,y=140) 

    def SubmitSalary(self):
        try: 
            today = date.today()
            cursor.execute("INSERT INTO Salary(salary_id, basic_pay, allowances) values (?,?,?)", self.atid.get(), self.etid.get(), self.status.get())
            conn.commit()
            messagebox.showinfo("Record Inserted", "Record inserted Succesfully" )
            print(cursor.rowcount, "record inserted.")
        except:
            messagebox.showerror("Record Not Inserted", "Error inserting Record" )

    def DeleteSalary(self):
        newWindow = Toplevel(root)
        newWindow.title("Delete Salary")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Delete Salary", font=50).pack()

        Label(newWindow, text="Salary ID:").place(x=100, y=40)
        
        aid = Entry(newWindow, textvariable=self.atid)
        aid.place(x=200, y=40)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitDeleteSalary)
        submit.place(x=200,y=80) 

    def SubmitDeleteSalary(self):
        try: 
            cursor.execute("DELETE FROM Salary WHERE salary_id = ?", self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Deleted", "Record Deleted Succesfully" )
            print(cursor.rowcount, "record Deleted.")
        except:
            messagebox.showerror("Record Not Deleted", "Error Deleting Record" )

    def UpdateSalary(self):
        newWindow = Toplevel(root)
        newWindow.title("Update Salary")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Update Salary", font=50).pack()

        Label(newWindow, text="Salary ID:").place(x=100, y=20)
        Label(newWindow, text="Basic Pay:").place(x=100, y=60)
        Label(newWindow, text="Allowance:").place(x=100, y=100)
        
        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitSalary)
        submit.place(x=200,y=140) 

    def SubmitUpdatedSalary(self):
        try: 
            today = date.today()
            cursor.execute("UPDATE Salary SET  basic_pay = ?, allowances= ? WHERE salary_id = ?", self.etid.get(), self.status.get(), self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Updated", "Record Updated Succesfully" )
            print(cursor.rowcount, "record Updated.")
        except:
            messagebox.showerror("Record Not Updated", "Error Updating Record" )


class Vacancies(object):
    def ViewVacancies(self):
        newWindow = Toplevel(root)
        newWindow.title("View Vacancies")
        newWindow.geometry("1100x550")
        Label(newWindow, text ="View Vacancies", font=50).pack()
        
        tree = ttk.Treeview(newWindow, column=("c1", "c2", "c3", "c4", "c5"), show='headings')

        tree.column("#1", anchor=tk.CENTER)

        tree.heading("#1", text="Vacancies ID")

        tree.column("#2", anchor=tk.CENTER)

        tree.heading("#2", text="Criteria")

        tree.column("#3", anchor=tk.CENTER)

        tree.heading("#3", text="Qualification")

        tree.column("#4", anchor=tk.CENTER)

        tree.heading("#4", text="Vacancy")

        tree.column("#5", anchor=tk.CENTER)

        tree.heading("#5", text="Deadline")
        tree.pack()
        scroll_bar = Scrollbar(newWindow)
  
        scroll_bar.pack(side = RIGHT,fill = Y)

        cursor.execute("SELECT * FROM Vacancies")
        
        rows = cursor.fetchall()    

        for row in rows:
            print(row) 
            tree.insert("", tk.END, values=row)
            scroll_bar.config( command = tree.yview )

    def __init__(self):
        self.atid = StringVar()
        self.etid = StringVar()
        self.status = StringVar()
        self.absents = StringVar()
        self.emp = StringVar()

    def AddVacancies(self):
        newWindow = Toplevel(root)
        newWindow.title("Add Vacancies")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Add Vacancies", font=50).pack()
        
        Label(newWindow, text="Vacancy ID:").place(x=100, y=20)
        Label(newWindow, text="Criteria:").place(x=100, y=60)
        Label(newWindow, text="Qualification:").place(x=100, y=100)
        Label(newWindow, text="Vacancy:").place(x=100, y=140)
        Label(newWindow, text="Deadline:").place(x=100, y=180)

        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)
        absents = Entry(newWindow, textvariable=self.absents)
        empid = Entry(newWindow, textvariable=self.emp)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        absents.place(x=200, y=140)
        empid.place(x=200, y=180)

        submit = Button(newWindow, text = 'Submit', command = self.SubmitVacancies)
        submit.place(x=200,y=220) 

    def SubmitVacancies(self):
        try: 
            today = date.today()
            cursor.execute("INSERT INTO Vacancies(vac_id, criteria, qualification, vacany, deadline) values (?,?,?,?,?)", self.atid.get(),self.etid.get(), self.status.get(), self.absents.get(), self.emp.get())
            conn.commit()
            messagebox.showinfo("Record Inserted", "Record inserted Succesfully" )
            print(cursor.rowcount, "record inserted.")
        except:
            messagebox.showerror("Record Not Inserted", "Error inserting Record" )

    def DeleteVacancies(self):
        newWindow = Toplevel(root)
        newWindow.title("Delete Vacancies")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Delete Vacancies", font=50).pack()

        Label(newWindow, text="Project ID:").place(x=100, y=40)
        
        aid = Entry(newWindow, textvariable=self.atid)
        aid.place(x=200, y=40)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitDeleteVacancies)
        submit.place(x=200,y=80) 

    def SubmitDeleteVacancies(self):
        try: 
            cursor.execute("DELETE FROM Vacancies WHERE vac_id = ?", self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Deleted", "Record Deleted Succesfully" )
            print(cursor.rowcount, "record Deleted.")
        except:
            messagebox.showerror("Record Not Deleted", "Error Deleting Record" )

    def UpdateVacancies(self):
        newWindow = Toplevel(root)
        newWindow.title("Update Vacancies")
        newWindow.geometry("1000x550")
        Label(newWindow, text ="Update Vacancies", font=50).pack()

        Label(newWindow, text="Vacancy ID:").place(x=100, y=20)
        Label(newWindow, text="Criteria:").place(x=100, y=60)
        Label(newWindow, text="Qualification:").place(x=100, y=100)
        Label(newWindow, text="Vacancy:").place(x=100, y=140)
        Label(newWindow, text="Deadline:").place(x=100, y=180)

        aid = Entry(newWindow, textvariable=self.atid)
        eid = Entry(newWindow, textvariable=self.etid)
        status = Entry(newWindow, textvariable=self.status)
        absents = Entry(newWindow, textvariable=self.absents)
        empid = Entry(newWindow, textvariable=self.emp)

        aid.place(x=200, y=20)
        eid.place(x=200, y=60)
        status.place(x=200, y=100)
        absents.place(x=200, y=140)
        empid.place(x=200, y=180)
        
        submit = Button(newWindow, text = 'Submit', command = self.SubmitUpdatedVacancies)
        submit.place(x=200,y=220) 

    def SubmitUpdatedVacancies(self):
        try: 
            today = date.today()
            cursor.execute("UPDATE Project SET criteria = ?, qualification = ?, vacany = ?, deadline = ? WHERE vac_id = ?", self.etid.get(), self.status.get(), self.absents.get(), self.emp.get(), self.atid.get())
            conn.commit()
            messagebox.showinfo("Record Updated", "Record Updated Succesfully" )
            print(cursor.rowcount, "record Updated.")
        except:
            messagebox.showerror("Record Not Updated", "Error Updating Record" )

#___________________________________________________________________________________________________________________________________________________

Label(root, text ="Attendance Module", font=20).place(x=50, y=40)

a = Attendance()
vattendance = Button(root, text="View Attendance", padx=10, pady=5,  bg="#263D42", fg='white', command=a.ViewAttendance)
vattendance.place(x=50, y=80)

Addattendance = Button(root, text="Add Attendance", padx=10, pady=5, bg="#263D42", fg='white', command=a.AddAttendance)
Addattendance.place(x=50, y=120)

Deleteattendance = Button(root, text="Delete Attendance", padx=10, pady=5, bg="#263D42", fg='white', command=a.DeleteAttendance)
Deleteattendance.place(x=50, y=160)

Updateattendance = Button(root, text="Update Attendance", padx=10, pady=5, bg="#263D42", fg='white', command=a.UpdateAttendance)
Updateattendance.place(x=50, y=200)

#___________________________________________________________________________________________________________________________________________________

Label(root, text ="Applicants Module", font=20).place(x=250, y=40)

a = Applicant()
vattendance = Button(root, text="View Applicants", padx=10, pady=5,  bg="#263D42", fg='white', command=a.ViewApplicant)
vattendance.place(x=250, y=80)

Addattendance = Button(root, text="Add Applicant", padx=10, pady=5, bg="#263D42", fg='white', command=a.AddApplicant)
Addattendance.place(x=250, y=120)

Deleteattendance = Button(root, text="Delete Applicant", padx=10, pady=5, bg="#263D42", fg='white', command=a.DeleteApplicant)
Deleteattendance.place(x=250, y=160)

Updateattendance = Button(root, text="Update Applicant", padx=10, pady=5, bg="#263D42", fg='white', command=a.UpdateApplicant)
Updateattendance.place(x=250, y=200)

#___________________________________________________________________________________________________________________________________________________

Label(root, text ="Employee Module", font=20).place(x=450, y=40)

a = Employee()
vattendance = Button(root, text="View Employees", padx=10, pady=5,  bg="#263D42", fg='white', command=a.ViewEmployee)
vattendance.place(x=450, y=80)

Addattendance = Button(root, text="Add Employees", padx=10, pady=5, bg="#263D42", fg='white', command=a.AddEmployee)
Addattendance.place(x=450, y=120)

Deleteattendance = Button(root, text="Delete Employees", padx=10, pady=5, bg="#263D42", fg='white', command=a.DeleteEmployee)
Deleteattendance.place(x=450, y=160)

Updateattendance = Button(root, text="Update Employees", padx=10, pady=5, bg="#263D42", fg='white', command=a.UpdateEmployee)
Updateattendance.place(x=450, y=200)

#___________________________________________________________________________________________________________________________________________________

Label(root, text ="Interview Module", font=20).place(x=650, y=40)

a = Interview()
vattendance = Button(root, text="View Interviews", padx=10, pady=5,  bg="#263D42", fg='white', command=a.ViewInterview)
vattendance.place(x=650, y=80)

Addattendance = Button(root, text="Add Interview", padx=10, pady=5, bg="#263D42", fg='white', command=a.AddInterview)
Addattendance.place(x=650, y=120)

Deleteattendance = Button(root, text="Delete Interview", padx=10, pady=5, bg="#263D42", fg='white', command=a.DeleteInterview)
Deleteattendance.place(x=650, y=160)

Updateattendance = Button(root, text="Update Interview", padx=10, pady=5, bg="#263D42", fg='white', command=a.UpdateInterview)
Updateattendance.place(x=650, y=200)

#___________________________________________________________________________________________________________________________________________________
# Row 2
Label(root, text ="Project Module", font=20).place(x=50, y=260)

a = Project()
vattendance = Button(root, text="View Projects", padx=10, pady=5,  bg="#263D42", fg='white', command=a.ViewProject)
vattendance.place(x=50, y=300)

Addattendance = Button(root, text="Add Project", padx=10, pady=5, bg="#263D42", fg='white', command=a.AddProject)
Addattendance.place(x=50, y=340)

Deleteattendance = Button(root, text="Delete Project", padx=10, pady=5, bg="#263D42", fg='white', command=a.DeleteProject)
Deleteattendance.place(x=50, y=380)

Updateattendance = Button(root, text="Update Project", padx=10, pady=5, bg="#263D42", fg='white', command=a.UpdateProject)
Updateattendance.place(x=50, y=420)

#___________________________________________________________________________________________________________________________________________________

Label(root, text ="Project Status Module", font=20).place(x=250, y=260)

a = ProjectStatus()
vattendance = Button(root, text="View Project Status", padx=10, pady=5,  bg="#263D42", fg='white', command=a.ViewProjectStatus)
vattendance.place(x=250, y=300)

Addattendance = Button(root, text="Add Project Status", padx=10, pady=5, bg="#263D42", fg='white', command=a.AddProjectStatus)
Addattendance.place(x=250, y=340)

Deleteattendance = Button(root, text="Delete Project Status", padx=10, pady=5, bg="#263D42", fg='white', command=a.DeleteProjectStatus)
Deleteattendance.place(x=250, y=380)

Updateattendance = Button(root, text="Update Project Status", padx=10, pady=5, bg="#263D42", fg='white', command=a.UpdateProjectStatus)
Updateattendance.place(x=250, y=420)

#___________________________________________________________________________________________________________________________________________________

Label(root, text ="Salary Module", font=20).place(x=450, y=260)

a = Salary()
vattendance = Button(root, text="View Salary", padx=10, pady=5,  bg="#263D42", fg='white', command=a.ViewSalary)
vattendance.place(x=450, y=300)

Addattendance = Button(root, text="Add Salary", padx=10, pady=5, bg="#263D42", fg='white', command=a.AddSalary)
Addattendance.place(x=450, y=340)

Deleteattendance = Button(root, text="Delete Salary", padx=10, pady=5, bg="#263D42", fg='white', command=a.DeleteSalary)
Deleteattendance.place(x=450, y=380)

Updateattendance = Button(root, text="Update Salary", padx=10, pady=5, bg="#263D42", fg='white', command=a.UpdateSalary)
Updateattendance.place(x=450, y=420)

#___________________________________________________________________________________________________________________________________________________

Label(root, text ="Vacancies Module", font=20).place(x=650, y=260)

a = Vacancies()
vattendance = Button(root, text="View Vacancies", padx=10, pady=5,  bg="#263D42", fg='white', command=a.ViewVacancies)
vattendance.place(x=650, y=300)

Addattendance = Button(root, text="Add Vacancies", padx=10, pady=5, bg="#263D42", fg='white', command=a.AddVacancies)
Addattendance.place(x=650, y=340)

Deleteattendance = Button(root, text="Delete Vacancies", padx=10, pady=5, bg="#263D42", fg='white', command=a.DeleteVacancies)
Deleteattendance.place(x=650, y=380)

Updateattendance = Button(root, text="Update Vacancies", padx=10, pady=5, bg="#263D42", fg='white', command=a.UpdateVacancies)
Updateattendance.place(x=650, y=420)

root.mainloop()
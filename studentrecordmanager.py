from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:
    def __init__(self,root):
        self.root=root
        titlespace=" "
        self.root.title(102 * titlespace + "Table Updater")
        self.root.geometry("800x625+300+0")
        self.root.resizable(width=False,height=False)

        MainFrame=Frame(self.root,bd=10,width=770,height=700,relief=RIDGE,bg="cadet blue")
        MainFrame.grid()


        TitleFrame=Frame(MainFrame,bd=7,width=770,height=100,relief=RIDGE)
        TitleFrame.grid(row=0,column=0)
        TopFrame3=Frame(MainFrame,bd=5,width=770,height=500,relief=RIDGE)
        TopFrame3.grid(row=1,column=0)
       
       
        LeftFrame=Frame(TopFrame3,bd=5,width=770,height=400,padx=2,bg="Cadet blue",relief=RIDGE)
        LeftFrame.pack(side=LEFT)
        LeftFrame1=Frame(LeftFrame,bd=5,width=600,height=180,padx=12,pady=9 ,relief=RIDGE)
        LeftFrame1.pack(side=TOP)
        
        
        RightFrame1=Frame(TopFrame3,bd=5,width=100,height=400,padx=2,bg="Cadet blue",relief=RIDGE)
        RightFrame1.pack(side=RIGHT)
        RightFrame1a=Frame(RightFrame1,bd=5,width=90,height=300,padx=2,pady=2,relief=RIDGE)
        RightFrame1a.pack(side=TOP)


        #----------------------------------    variables   --------------------------------------------------------------------
       
        studentID=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Gender=StringVar()
        Mobile=StringVar()
 
        #----------------------------------  function definition   --------------------------------------------------------------
        def iExit():
            iExit=tkinter.messagebox.askyesno("Table Updater","Confirm if you want to exit") 
            if iExit>0:
                root.destroy()
                return

        def Reset():
            self.entstudentID.delete(0,END)
            self.entFirstName.delete(0,END)
            self.entSurName.delete(0,END)
            self.entAddress.delete(0,END)
            Gender.set("")
            self.entMobile.delete(0,END)

        def Insert():
            if studentID.get()=="" or Firstname.get()=="" or Surname.get()=="":
                tkinter.messagebox.showerror("Table Updater","Enter correct details")
            else:
                sqlCon=pymysql.connect(host="localhost",user="root",password="02122000",database="student")
                cur=sqlCon.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s)",
                (studentID.get(),Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get()))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Table Updater","Record entered successfully")
        
        def DisplayData():
            sqlCon=pymysql.connect(host="localhost",user="root",password="02122000",database="student")
            cur=sqlCon.cursor()
            cur.execute("select * from student")
            result=cur.fetchall()
            if len(result) != 0 :
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('',END,values=row)
            
            sqlCon.commit()
            sqlCon.close()


        def studentinfo(ev):
            viewInfo=self.student_records.focus()
            learnerData=self.student_records.item(viewInfo)
            row=learnerData['values']
            studentID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            Gender.set(row[4])
            Mobile.set(row[5])

        def update():
            sqlCon=pymysql.connect(host="localhost",user="root",password="02122000",database="student")
            cur=sqlCon.cursor()
            cur.execute("update student set Firstname=%s,Surname=%s,Address=%s,Gender=%s,Mobile=%s where stdid=%s",
            (Firstname.get(),Surname.get(),Address.get(),Gender.get(),Mobile.get(),studentID.get()))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Table Updater","Record updated successfully")
        
        
        def deleteDB():
            sqlCon=pymysql.connect(host="localhost",user="root",password="02122000",database="student")
            cur=sqlCon.cursor()
            cur.execute("delete from student where stdid=%s",studentID.get())
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Table Updater","Record Deleted successfully")
            Reset()
        
        
        def searchDB():
            try:
                sqlCon=pymysql.connect(host="localhost",user="root",password="02122000",database="student")
                cur=sqlCon.cursor()
                cur.execute("select *from student where stdid=%s",studentID.get())

                row =cur.fetchone()
                
                studentID.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                Gender.set(row[4])
                Mobile.set(row[5])
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Table Updater","No record found")
                Reset()
                sqlCon.close()

        #---------------------------------- front app layout------------------------------------------------------------------------

        self.lbltitle=Label(TitleFrame,font=('arial',31,'bold'),text="Student Record Manager",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=132)

        #for student Id
        
        self.lblstudentID=Label(LeftFrame1,font=('arial',12,'bold'),text="Student ID",bd=7)
        self.lblstudentID.grid(row=0,column=0,sticky=W,padx=5)
        self.entstudentID=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=studentID)
        self.entstudentID.grid(row=0,column=1,sticky=W,padx=5)
       
        #for First name
        self.lblFirstName=Label(LeftFrame1,font=('arial',12,'bold'),text="First Name",bd=7)
        self.lblFirstName.grid(row=1,column=0,sticky=W,padx=5)
        self.entFirstName=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=Firstname)
        self.entFirstName.grid(row=1,column=1,sticky=W,padx=5)
        
        #for surname
        self.lblSurName=Label(LeftFrame1,font=('arial',12,'bold'),text="Surname",bd=7)
        self.lblSurName.grid(row=2,column=0,sticky=W,padx=5)
        self.entSurName=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=Surname)
        self.entSurName.grid(row=2,column=1,sticky=W,padx=5)

        
        #for Address
        
        self.lblAddress=Label(LeftFrame1,font=('arial',12,'bold'),text="Address",bd=7, )
        self.lblAddress.grid(row=3,column=0,sticky=W,padx=5)
        self.entAddress=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=Address)
        self.entAddress.grid(row=3,column=1)
       
        #for Gender 
        self.lblGender=Label(LeftFrame1,font=('arial',12,'bold'),text="Gender ",bd=5, )
        self.lblGender.grid(row=4,column=0,sticky=W,padx=5)
        self.cboGender=ttk.Combobox(LeftFrame1,font=('arial',12,'bold'),width=43,state='readonly',textvariable=Gender)
        self.cboGender['values']=(' ','Male','Female','Transgender')
        self.cboGender.current(0) 
        self.cboGender.grid(row=4,column=1)
        
        #for mobile no:-
        self.lblMobile=Label(LeftFrame1,font=('arial',12,'bold'),text="Mobile",bd=7)
        self.lblMobile.grid(row=5,column=0,sticky=W,padx=5)
        self.entMobile=Entry(LeftFrame1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=Mobile)
        self.entMobile.grid(row=5,column=1,sticky=W,padx=5)





#-------------------------------------------Table tree view -------------------------------------------------------------------------
        scroll_y=Scrollbar(LeftFrame,orient=VERTICAL)
        self.student_records=ttk.Treeview(LeftFrame,height=12 ,column=("stdid","First Name","Surname","Address","Gender","Mobile"),yscrollcommand=scroll_y.set )

        scroll_y.pack(side=RIGHT,fill=Y)

        self.student_records.heading("stdid",text="Student ID")
        self.student_records.heading("First Name",text="First Name")
        self.student_records.heading("Surname",text="Surname")
        self.student_records.heading("Address",text="Address")
        self.student_records.heading("Gender",text="Gender")
        self.student_records.heading("Mobile",text="Mobile")
        
        self.student_records['show']='headings'

        self.student_records.column("stdid",width=70)
        self.student_records.column("First Name",width=100) 
        self.student_records.column("Surname",width=100)
        self.student_records.column("Address",width=100)
        self.student_records.column("Gender",width=70)
        self.student_records.column("Mobile",width=70)
        self.student_records.pack(fill=BOTH,expand=1)
        self.student_records.bind("<ButtonRelease-1>",studentinfo)


#---------------------------------------------buttons add----------------------------------------------------------------------------
        self.btnAddNew=Button(RightFrame1a,font=('arial',16,'bold'),text="Insert",bd=4,pady=1,padx=24,width=8,height=2,command=Insert).grid(row=0,column=0,padx=1)
        self.btnDisplay=Button(RightFrame1a,font=('arial',16,'bold'),text="Display",bd=4,pady=1,padx=24,width=8,height=2,command=DisplayData).grid(row=1,column=0,padx=1)
        self.btnUpdate=Button(RightFrame1a,font=('arial',16,'bold'),text="Update",bd=4,pady=1,padx=24,width=8,height=2,command=update).grid(row=2,column=0,padx=1)
        self.btnDelete=Button(RightFrame1a,font=('arial',16,'bold'),text="Delete",bd=4,pady=1,padx=24,width=8,height=2,command=deleteDB).grid(row=3,column=0,padx=1)
        self.btnSearch=Button(RightFrame1a,font=('arial',16,'bold'),text="Search",bd=4,pady=1,padx=24,width=8,height=2,command=searchDB).grid(row=4,column=0,padx=1)
        self.btnReset=Button(RightFrame1a,font=('arial',16,'bold'),text="Reset",bd=4,pady=1,padx=24,width=8,height=2,command=Reset).grid(row=5,column=0,padx=1)
        self.btnExit=Button(RightFrame1a,font=('arial',16,'bold'),text="Exit",bd=4,pady=1,padx=24,width=8,height=2,command=iExit).grid(row=6,column=0,padx=1)
#-------------------------------------------------------------------------------------------------------------------------------------
if __name__=='__main__':
    root=Tk()
    application=ConnectorDB(root)
    root.mainloop()



 
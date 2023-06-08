from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import date

import pymysql

root = Tk()


class employee:
    remark_history = ''
    today = str(date.today())

    def __init__(self, root):
        self.root = root
        self.root.title("Know Your BA")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Know Your BA", bd=6, relief=GROOVE, font=("times new roman", 35, "bold"),
                      bg="#27374D", fg="#9DB2BF")
        title.pack(side=TOP, fill=X)

        # ==========Variable=========
        self.Emp_no_var = StringVar()
        self.name_var = StringVar()
        self.agency_var = StringVar()
        self.category_var = StringVar()
        self.location_var = StringVar()
        self.experience_var = StringVar()
        self.competency_var = StringVar()
        self.final_rating_var = StringVar()
        self.team_var = StringVar()

        self.search = StringVar()
        self.search_txt = StringVar()

        self.r1 = StringVar()
        self.r2 = StringVar()
        self.r3 = StringVar()
        self.r4 = StringVar()
        self.r5 = StringVar()
        # =======Manage Frame=======

        M_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#526D82")
        M_Frame.place(x=20, y=80, width=470, height=590)

        m_title = Label(M_Frame, text="Manage Employee", bg="#526D82", fg="#27374D",
                        font=("times new roman", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_emp_num = Label(M_Frame, text="Employee No", bg="#526D82", fg="white",
                            font=("times new roman", 14, "bold"))
        lbl_emp_num.grid(row=1, column=0, pady=5, padx=30, sticky="w")

        txt_emp_num = Entry(M_Frame, textvariable=self.Emp_no_var, font=("times new roman", 13, "bold"), bd=3,
                            relief=RIDGE)
        txt_emp_num.grid(row=1, column=1, pady=5, padx=30, sticky="W")

        lbl_emp_name = Label(M_Frame, text="Employee Name", bg="#526D82", fg="white",
                             font=("times new roman", 14, "bold"))
        lbl_emp_name.grid(row=2, column=0, pady=5, padx=30, sticky="W")

        txt_emp_name = Entry(M_Frame, textvariable=self.name_var, font=("times new roman", 13, "bold"), bd=3,
                             relief=RIDGE)
        txt_emp_name.grid(row=2, column=1, pady=5, padx=30, sticky="W")

        lbl_emp_agency = Label(M_Frame, text="BA Agency", bg="#526D82", fg="white",
                               font=("times new roman", 14, "bold"))
        lbl_emp_agency.grid(row=3, column=0, pady=5, padx=30, sticky="W")

        combo_agency = ttk.Combobox(M_Frame, textvariable=self.agency_var, font=("times new roman", 13, "bold"),
                                    state='readonly')
        combo_agency['values'] = ('D&B', 'GVE', 'Impelco', 'Empire', 'N.K', 'Vision India', 'Trident')
        combo_agency.grid(row=3, column=1, pady=10, padx=25)

        lbl_emp_category = Label(M_Frame, text="Category", bg="#526D82", fg="white",
                                 font=("times new roman", 14, "bold"))
        lbl_emp_category.grid(row=4, column=0, pady=5, padx=30, sticky="W")

        combo_category = ttk.Combobox(M_Frame, textvariable=self.category_var, font=("times new roman", 13, "bold"),
                                      state='readonly')
        combo_category['values'] = ('Supervisor', 'Lineman', 'Meter Installer')
        combo_category.grid(row=4, column=1, pady=10, padx=25)

        lbl_emp_location = Label(M_Frame, text="Location", bg="#526D82", fg="white",
                                 font=("times new roman", 14, "bold"))
        lbl_emp_location.grid(row=5, column=0, pady=5, padx=30, sticky="W")

        Combo_location = ttk.Combobox(M_Frame, textvariable=self.location_var, font=("times new roman", 13, "bold"),
                                      state='readonly')
        Combo_location['values'] = ('Dheerpur', 'Keshavpuram', 'Rohini', 'Bawana')
        Combo_location.grid(row=5, column=1, pady=10, padx=25)

        lbl_emp_competency = Label(M_Frame, text="Competency", bg="#526D82", fg="white",
                                   font=("times new roman", 14, "bold"))
        lbl_emp_competency.grid(row=6, column=0, pady=5, padx=30, sticky="W")

        combo_competency = ttk.Combobox(M_Frame, textvariable=self.competency_var, font=("times new roman", 13, "bold"),
                                        state='readonly')
        combo_competency['values'] = ('Diamond', 'Gold', 'Silver', 'Bronze')
        combo_competency.grid(row=6, column=1, pady=10, padx=25)

        lbl_emp_exp = Label(M_Frame, text="Experience(Years)", bg="#526D82", fg="white",
                            font=("times new roman", 14, "bold"))
        lbl_emp_exp.grid(row=7, column=0, pady=5, padx=25, sticky="W")

        txt_emp_exp = Entry(M_Frame, textvariable=self.experience_var, font=("times new roman", 13, "bold"), bd=3,
                            relief=RIDGE)
        txt_emp_exp.grid(row=7, column=1, pady=5, padx=30, sticky="W")

        lbl_emp_remark = Label(M_Frame, text="Remark", bg="#526D82", fg="white", font=("times new roman", 14, "bold"))
        lbl_emp_remark.grid(row=8, column=0, pady=5, padx=30, sticky="w")

        self.txt_add = Text(M_Frame, width=30, height=4, font=('', 10))
        self.txt_add.grid(row=8, column=1, pady=5, padx=25, sticky='w')

        lbl_emp_team = Label(M_Frame, text="Team", bg="#526D82", fg="white", font=("times new roman", 14, "bold"))
        lbl_emp_team.grid(row=9, column=0, pady=5, padx=30, sticky="w")

        txt_emp_team = Entry(M_Frame, textvariable=self.team_var, font=("times new roman", 13, "bold"), bd=3,
                             relief=RIDGE)
        txt_emp_team.grid(row=9, column=1, pady=5, padx=30, sticky="W")

        # ======Button========
        btn_Frame = Frame(M_Frame, bd=4, relief=RIDGE, bg="#526D82")
        btn_Frame.place(x=15, y=510, width=420)

        Button(btn_Frame, text="ADD", width=10, command=self.add_employee).grid(row=0, column=0, padx=10,
                                                                                pady=10)
        Button(btn_Frame, text="UPDATE", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                  pady=10)
        Button(btn_Frame, text="DELETE", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                  pady=10)
        Button(btn_Frame, text="CLEAR", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        # ======Detail=======

        d_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#526D82")
        d_Frame.place(x=500, y=80, width=800, height=590)

        lbl_search = Label(d_Frame, text="Search", bg="#526D82", fg="#B0DFE5", font=("times new roman", 19, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(d_Frame, textvariable=self.search, width=10, font=("times new roman", 13, "bold"),
                                    state='readonly')
        combo_search['values'] = ('Emp_No', 'Name', 'Team', 'Category', 'Location')
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(d_Frame, textvariable=self.search_txt, width=15, font=("times new roman", 14, "bold"), bd=3,
                           relief=RIDGE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="W")

        Button(d_Frame, text="SEARCH", width=10, command=self.search_data, pady=5).grid(row=0, column=3,
                                                                                        padx=10, pady=10)
        Button(d_Frame, text="SHOW ALL", width=10, command=self.fetch_data, pady=5).grid(row=0, column=4,
                                                                                         padx=10, pady=10)

        # ========table Frame=======
        Table_Frame = Frame(d_Frame, bd=4, relief=RIDGE, bg="#0E4D92")
        Table_Frame.place(x=10, y=70, width=770, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(Table_Frame, columns=(
            "Employee Number", "Name", "BA Agency", "Category", "Location", "Experience", "Competency", "Remark",
            "Rating", "Team"),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading("Employee Number", text="Employee No")
        self.employee_table.heading("Name", text="Name")
        self.employee_table.heading("BA Agency", text="BA Agency")
        self.employee_table.heading("Category", text="Category")
        self.employee_table.heading("Location", text="Location")
        self.employee_table.heading("Experience", text="Experience")
        self.employee_table.heading("Competency", text="Competency")
        self.employee_table.heading("Remark", text="Remark")
        self.employee_table.heading("Rating", text="Rating")
        self.employee_table.heading("Team", text="Team")
        self.employee_table['show'] = 'headings'
        self.employee_table.column("Employee Number", width=65)
        self.employee_table.column("Name", width=85)
        self.employee_table.column("BA Agency", width=75)
        self.employee_table.column("Category", width=75)
        self.employee_table.column("Location", width=65)
        self.employee_table.column("Experience", width=65)
        self.employee_table.column("Competency", width=75)
        self.employee_table.column("Remark", width=75)
        self.employee_table.column("Rating", width=65)
        self.employee_table.column("Team", width=50)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.employee_table.bind("<ButtonRelease-3>", self.view_data)
        self.fetch_data()

    def add_employee(self):
        if self.Emp_no_var.get() == "" or self.name_var.get() == "" or self.agency_var.get() == "" or self.location_var.get() == 0 or self.competency_var.get() == "":
            messagebox.showerror("Error", "All fields are Required!!!")
        else:
            conn = pymysql.connect(host="localhost", user="root", password="Dob@1996", database="employee_prj")
            cur = conn.cursor()
            cur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.Emp_no_var.get(),
                                                                                       self.name_var.get(),
                                                                                       self.agency_var.get(),
                                                                                       self.category_var.get(),
                                                                                       self.location_var.get(),
                                                                                       self.experience_var.get(),
                                                                                       self.competency_var.get(),
                                                                                       self.today + "\n" + self.txt_add.get(
                                                                                           '1.0', END),
                                                                                       self.final_rating_var.get(),
                                                                                       self.team_var.get()

                                                                                       ))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted.")

    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="Dob@1996", database="employee_prj")
        cur = conn.cursor()
        cur.execute("select * from employee")
        rows = cur.fetchall()
        if rows != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.Emp_no_var.set("")
        self.name_var.set("")
        self.agency_var.set("")
        self.category_var.set("")
        self.location_var.set("")
        self.experience_var.set("")
        self.competency_var.set("")
        self.txt_add.delete("1.0", END)
        self.team_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        row = content['values']
        self.Emp_no_var.set(row[0])
        self.name_var.set(row[1])
        self.agency_var.set(row[2])
        self.category_var.set(row[3])
        self.location_var.set(row[4])
        self.experience_var.set(row[5])
        self.competency_var.set(row[6])
        self.txt_add.delete("1.0", END, )
        self.remark_history = row[7]
        self.team_var.set(row[9])

    def update_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="Dob@1996", database="employee_prj")
        cur = conn.cursor()
        cur.execute(
            "update employee set name=%s,Agency=%s,category=%s,location=%s,experience=%s,competency=%s,remark=%s,team=%s where emp_no=%s",
            (
                self.name_var.get(),
                self.agency_var.get(),
                self.category_var.get(),
                self.location_var.get(),
                self.experience_var.get(),
                self.competency_var.get(),
                self.today + "\n" + self.txt_add.get('1.0', END) + "\n" + self.remark_history,
                self.team_var.get(),
                self.Emp_no_var.get()
            ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()

    def delete_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="Dob@1996", database="employee_prj")
        cur = conn.cursor()
        cur.execute("delete from employee where emp_no=" + self.Emp_no_var.get())
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="Dob@1996", database="employee_prj")
        cur = conn.cursor()
        cur.execute(
            "select * from employee where " + str(self.search.get()) + " Like '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
            conn.commit()
        conn.close()

    def view_data(self, ev):

        cursor_row = self.employee_table.focus()
        content = self.employee_table.item(cursor_row)
        row = content['values']
        emp_no = row[0]
        emp_name = row[1]
        ba_agency = row[2]
        category = row[3]
        location = row[4]
        emp_exp = row[5]
        emp_comp = row[6]
        emp_team = row[9]
        top = Toplevel(root, background="#526D82")
        top.geometry("750x750")
        top.title("BA Details")
        lbl_emp_name = Label(top, text=emp_name + " (Team " + emp_team + ")", font=("times new roman", 24, "bold"), background="#526D82",
                             fg="#27374D")
        lbl_emp_name.grid(row=0, column=0, columnspan=2, pady=20, padx=220)

        lbl_emp_no = Label(top, text="Employee No", font=("times new roman", 14, "bold"), background="#526D82",
                           fg="white")
        lbl_emp_no.grid(row=1, column=0, padx=50)

        txt_emp_no = Label(top, text=emp_no, font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        txt_emp_no.grid(row=1, column=1)

        lbl_agency = Label(top, text="BA Agency", font=("times new roman", 14, "bold"), background="#526D82",
                           fg="white")
        lbl_agency.grid(row=3, column=0)

        txt_agency = Label(top, text=ba_agency, font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        txt_agency.grid(row=3, column=1)

        lbl_category = Label(top, text="Category", font=("times new roman", 14, "bold"), background="#526D82",
                             fg="white")
        lbl_category.grid(row=4, column=0)

        txt_category = Label(top, text=category, font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        txt_category.grid(row=4, column=1)

        lbl_location = Label(top, text="Location", font=("times new roman", 14, "bold"), background="#526D82",
                             fg="white")
        lbl_location.grid(row=5, column=0)

        txt_location = Label(top, text=location, font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        txt_location.grid(row=5, column=1)

        lbl_experience = Label(top, text="Experience", font=("times new roman", 14, "bold"), background="#526D82",
                               fg="white")
        lbl_experience.grid(row=6, column=0)

        txt_experience = Label(top, text=str(emp_exp) + " Years", font=("times new roman", 14, "bold"), background="#526D82",
                               fg="white")
        txt_experience.grid(row=6, column=1)

        lbl_competency = Label(top, text="Competency", font=("times new roman", 14, "bold"), background="#526D82",
                               fg="white")
        lbl_competency.grid(row=7, column=0)

        txt_competency = Label(top, text=emp_comp, font=("times new roman", 14, "bold"), background="#526D82",
                               fg="white")
        txt_competency.grid(row=7, column=1)

        lbl_r1 = Label(top, text="R1", font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        lbl_r1.grid(row=8, column=0)

        combo_r1 = ttk.Combobox(top, textvariable=self.r1, font=("times new roman", 13, "bold"),
                                state='readonly', background="#526D82")
        combo_r1['values'] = ('1', '2', '3', '4', '5')
        combo_r1.grid(row=8, column=1, pady=10, padx=25)

        lbl_r2 = Label(top, text="R2", font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        lbl_r2.grid(row=9, column=0)

        combo_r2 = ttk.Combobox(top, textvariable=self.r2, font=("times new roman", 13, "bold"),
                                state='readonly', background="#526D82")
        combo_r2['values'] = ('1', '2', '3', '4', '5')
        combo_r2.grid(row=9, column=1, pady=10, padx=25)

        lbl_r3 = Label(top, text="R3", font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        lbl_r3.grid(row=10, column=0)

        combo_r3 = ttk.Combobox(top, textvariable=self.r3, font=("times new roman", 13, "bold"),
                                state='readonly', background="#526D82")
        combo_r3['values'] = ('1', '2', '3', '4', '5')
        combo_r3.grid(row=10, column=1, pady=10, padx=25)

        lbl_r4 = Label(top, text="R4", font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        lbl_r4.grid(row=11, column=0)

        combo_r4 = ttk.Combobox(top, textvariable=self.r4, font=("times new roman", 13, "bold"),
                                state='readonly', background="#526D82")
        combo_r4['values'] = ('1', '2', '3', '4', '5')
        combo_r4.grid(row=11, column=1, pady=10, padx=25)

        lbl_r5 = Label(top, text="R5", font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        lbl_r5.grid(row=12, column=0)

        combo_r5 = ttk.Combobox(top, textvariable=self.r5, font=("times new roman", 13, "bold"),
                                state='readonly', background="#526D82")
        combo_r5['values'] = ('1', '2', '3', '4', '5')
        combo_r5.grid(row=12, column=1, pady=10, padx=25)

        Button(top, text="UPDATE", width=10, command=self.update_rating, pady=5).grid(row=13, column=0,
                                                                                      columnspan=2,
                                                                                      padx=10, pady=10)

        lbl_remark = Label(top, text="Remark", font=("times new roman", 14, "bold"), background="#526D82", fg="white")
        lbl_remark.grid(row=14, column=0)

        scroll_y = Scrollbar(top, orient=VERTICAL)
        txt_remark = Text(top, font=("times new roman", 14, "bold"), width=30, height=4, yscrollcommand=scroll_y.set)
        txt_remark.grid(row=14, column=1)
        txt_remark.insert(END, self.remark_history)
        self.r1.set("")
        self.r2.set("")
        self.r3.set("")
        self.r4.set("")
        self.r5.set("")

    def update_rating(self):

        avg_rating = float((int(self.r1.get()) +
                            int(self.r2.get()) +
                            int(self.r3.get()) +
                            int(self.r4.get()) +
                            int(self.r5.get())) / 5)

        conn = pymysql.connect(host="localhost", user="root", password="Dob@1996", database="employee_prj")
        cur = conn.cursor()

        cur.execute(
            "update rating set r1=%s,r2=%s,r3=%s,r4=%s,r5=%s where emp_no=%s",
            (
                self.r1.get(),
                self.r2.get(),
                self.r3.get(),
                self.r4.get(),
                self.r5.get(),
                self.Emp_no_var.get()
            ))

        cur.execute(
            "update employee set final_rating=%s where emp_no=%s",
            (

                avg_rating,
                self.Emp_no_var.get()
            ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()


root.configure(bg="white")
ob = employee(root)
root.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("Data Entry Form")

frame = Frame(window)
frame.pack()

#Function
def enter_data():

    status = terms_status.get()

    if status == "Accepted" :
    
        #User Info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname : 
            prefix = prefix_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            num_courses = courses_num_spinbox.get()
            num_semester = semester_num_spinbox.get()
            registration_status = reg_status.get()

            print("User Information")
            print("First Name : ",firstname, " Last Name : ",lastname)
            print("Prefix : ",prefix, " Age : " , age, " Nationality : ",nationality)

            print("------------------------------")

            print("Course Information")
            print("Registration Status : ",registration_status)
            print("Number of courses completed : ",num_courses)
            print("Number of semester completed : ",num_semester)

            print("------------------------------")

        else :
            messagebox.showwarning(title="Invalid Input",message = "First Name and Last Name are required")

    else :
        messagebox.showwarning(title="Warning",message = "You have not accepted the terms and conditions")

#USER INFORMATION
user_info_frame = LabelFrame(frame,text = "User Information")
user_info_frame.grid(row = 0 , column = 0 ,padx = 20 , pady = 20)

first_name_label = Label(user_info_frame,text = "First Name")
first_name_label.grid(row = 0 ,column = 0)

first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row = 1 ,column = 0)

last_name_label = Label(user_info_frame,text = "Last Name")
last_name_label.grid(row = 0 ,column = 1)

last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row = 1 ,column = 1)

prefix_label = Label(user_info_frame,text = "Prefix")
prefix_label.grid(row = 0, column = 2)

prefix_combobox = ttk.Combobox(user_info_frame,values = ["Mr." , "Ms." , "Dr."])
prefix_combobox.grid(row = 1 ,column = 2)

age_label = Label(user_info_frame,text = "Age")
age_label.grid(row = 2 ,column = 0)

age_spinbox = Spinbox(user_info_frame,from_=18 ,to=60)
age_spinbox.grid(row = 3, column = 0)

nationality_label = Label(user_info_frame,text = "Nationality")
nationality_label.grid(row = 2 ,column = 1)

nationality_combobox = ttk.Combobox(user_info_frame,values = ["India","America","Africa","Europe"])
nationality_combobox.grid(row = 3 , column = 1)

for widget in user_info_frame.winfo_children() :
    widget.grid_configure(padx = 10 , pady = 10)

#COURSE INFORMATION
course_info_frame = LabelFrame(frame, text = "Course Information")
course_info_frame.grid(row = 1,column = 0, sticky = "news" ,padx = 20 , pady = 20)

registered_label = Label(course_info_frame,text = "Registration Status")
registered_label.grid(row = 0, column = 0)

reg_status = StringVar(value = "Registered")
registered_checked = Checkbutton(course_info_frame,text = "Currently Registered",variable = reg_status,onvalue = "Registered", offvalue = "Not Registered")
registered_checked.grid(row = 1 ,column =0)

courses_num_label = Label(course_info_frame,text = "Completed Courses")
courses_num_label.grid(row = 0 ,column = 1)

courses_num_spinbox = Spinbox(course_info_frame,from_=1 ,to="infinity")
courses_num_spinbox.grid(row = 1, column = 1)

semester_num_label = Label(course_info_frame,text = "Semester Courses")
semester_num_label.grid(row = 0 ,column = 2)

semester_num_spinbox = Spinbox(course_info_frame,from_=1 ,to="infinity")
semester_num_spinbox.grid(row = 1, column = 2)

for widget in course_info_frame.winfo_children() :
    widget.grid_configure(padx = 10 , pady = 10)

#TERMS&CONDITIONS
terms_frame = LabelFrame(frame,text = "Terms & Conditions")
terms_frame.grid(row = 2 ,column = 0 , sticky = "news" , padx = 20, pady = 20)

terms_status = StringVar(value = "Not Accepted")
terms_check = Checkbutton(terms_frame,text = "I accept the terms and conditions.",variable = terms_status,onvalue = "Accepted", offvalue = "Not Accepted")
terms_check.grid(row = 0 ,column = 0)

#Button
button = Button(frame,text = "Enter Data",command = enter_data)
button.grid(row = 3 , column = 0 , sticky = "news" , padx = 20, pady = 20)

window.mainloop()

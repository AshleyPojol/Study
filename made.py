import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pymysql
from tkinter import messagebox
from tkinter import IntVar
from ttkbootstrap.scrolled import ScrolledFrame
from PIL import Image, ImageTk


def show_login_interface():
    hide_all_interfaces()
    login_frame.pack()


def show_register_interface():
    hide_all_interfaces()
    register_frame.pack()


def show_subject_interface():
    hide_all_interfaces()
    subject_frame.pack()


def show_topicdc_interface():
    hide_all_interfaces()
    topicdc_frame.pack()


def show_topicic_interface():
    hide_all_interfaces()
    topicic_frame.pack()


def show_topiceda_interface():
    hide_all_interfaces()
    topiceda_frame.pack()


def show_topicde_interface():
    hide_all_interfaces()
    topicde_frame.pack()


def show_topicmmw_interface():
    hide_all_interfaces()
    topicmmw_frame.pack()


def show_main_interface():
    hide_all_interfaces()
    main_frame.pack()


def hide_all_interfaces():
    # Main Frames
    login_frame.pack_forget()
    register_frame.pack_forget()
    subject_frame.pack_forget()
    topicdc_frame.pack_forget()
    topicic_frame.pack_forget()
    topiceda_frame.pack_forget()
    topicde_frame.pack_forget()
    topicmmw_frame.pack_forget()
    main_frame.pack_forget()

    # Frame Topics (Differential Calculus)

    limits_frame.pack_forget()
    increment_frame.pack_forget()
    trigo_frame.pack_forget()
    inverse_frame.pack_forget()
    exponent_frame.pack_forget()
    logar_frame.pack_forget()

    # Frame Topics (Integral Calculus)
    integration_frame.pack_forget()
    exponential_frame.pack_forget()
    trigonometric_frame.pack_forget()
    inversetrigo_frame.pack_forget()
    hyperbolic_frame.pack_forget()
    power_frame.pack_forget()

 # Frame Topics (Engineering Data Analysis)
    permutation_frame.pack_forget()
    combination_frame.pack_forget()
    mathematical_frame.pack_forget()
    odds_frame.pack_forget()
    mutually_frame.pack_forget()
    independent_frame.pack_forget()

    # Frame Topics (Differential Equations)
    differential_frame.pack_forget()
    seperation_frame.pack_forget()
    arbitrary_frame.pack_forget()
    homogeneous_frame.pack_forget()
    exact_frame.pack_forget()
    nonexact_frame.pack_forget()

    # Frame Topics (Mathematics in the Modern World)
    fibonacci_frame.pack_forget()
    operations_frame.pack_forget()
    simple_frame.pack_forget()
    means_frame.pack_forget()
    ttest_frame.pack_forget()
    pearson_frame.pack_forget()


registered_username = None
registered_password = None


def submit_register():
    username = entry_register_username.get()
    password = entry_register_password.get()
    show_login_interface()
    login(username, password)


def login():
    username = entry_login_username.get()
    password = entry_login_password.get()

    try:
        con = pymysql.connect(host='localhost', user='root', password='root', database='userdata')
        my_cursor = con.cursor()

        # Check if the 'data' table exists
        my_cursor.execute("SHOW TABLES LIKE 'data'")
        result = my_cursor.fetchone()

        if not result:
            messagebox.showerror('Error', 'Please register first.')
            return

        # Check if the entered credentials exist in the 'data' table
        query = 'SELECT * FROM data WHERE username = %s AND password = %s'
        my_cursor.execute(query, (username, password))
        result = my_cursor.fetchone()

        if result:
            messagebox.showinfo('Success', 'Login Successful')
            show_subject_interface()
        else:
            messagebox.showerror('Error', 'Invalid Username or Password')

    except pymysql.Error as e:
        messagebox.showerror('Error', f'Database Error: {e}')
    finally:
        con.close()


def register():
    username = entry_register_username.get()
    password = entry_register_password.get()


def clear():
    entry_register_username.delete(0, END)
    entry_register_password.delete(0, END)
    entry_register_confirmpassword.delete(0, END)


def connect_database():
    if entry_register_username.get() == '' or entry_register_password.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    elif entry_register_password.get() != entry_register_confirmpassword.get():
        messagebox.showerror('Error', 'Password does not Match')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept the Terms and Condition.')
    elif cinput.get() == 0:
        messagebox.showerror('Error', 'Please Accept that you Inputted all the Details Correctly.')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='root', database='userdata')
            my_cursor = con.cursor()

            # Check if the 'data' table exists
            my_cursor.execute("SHOW TABLES LIKE 'data'")
            result = my_cursor.fetchone()

            if not result:
                # If the 'data' table doesn't exist, create it
                query = 'CREATE TABLE data (id int auto_increment primary key, username varchar(50), password varchar(50))'
                my_cursor.execute(query)

            # Insert user data into the 'data' table
            query = 'INSERT INTO data (username, password) VALUES (%s, %s)'
            my_cursor.execute(query, (entry_register_username.get(), entry_register_password.get()))

            con.commit()
            messagebox.showinfo('Success', 'Account Created Successfully')
            clear()

        except pymysql.Error as e:
            messagebox.showerror('Error', f'Database Error: {e}')
        finally:
            con.close()


def quizDifferential():
    subject_frame.pack()
    global quizDC, vars

    quizDC = tk.Toplevel(root)
    quizDC.title("Differential Calculus Quiz")
    quizDC.geometry('750x500')

    differential_questions = [
        ["Find the derivative of y = Arccos ⅔ x",
         "A. 4/√1-16x²",
         "B. 4/√1+16x²",
         "C. -4/√1+16x²"],
        ["Find the derivative of y = ln²x",
         "A. ln(x)/x",
         "B. 2 ln(x)/x",
         "C. x/(3 ln(x))"],
        ["Given y = 1/√x-1, find y’",
         "A. -1/(2(x-1)^(3/2))",
         "B. 1/((x-1)^(3/2))",
         "C. -1/(2(x+1)^(3/2))"]
    ]

    correct_answers_differential = [1, 2, 1]

    vars = []
    for i, question in enumerate(differential_questions):
        label = ttk.Label(quizDC, text=f"Q{i + 1}: {question[0]}", font=("Helvetica", 12), anchor='w')
        label.pack(pady=5)

        var = IntVar()
        vars.append(var)

        options = question[1:]
        for j, option in enumerate(options, start=1):
            radio_button = ttk.Radiobutton(quizDC, text=option, variable=var, value=j)
            radio_button.pack(pady=2, padx=20)

    def calculateScore():
        score = 0
        for i, var in enumerate(vars):
            selected_answer = var.get()
            if selected_answer == correct_answers_differential[i]:
                score += 1
        messagebox.showinfo("Quiz Result", f"Your score is: {score}/{len(differential_questions)}")
        

    submit_button = ttk.Button(quizDC, text="Submit", command=calculateScore)
    submit_button.pack(pady=15)

    back_button = ttk.Button(quizDC, text="Back to Subjects", command=subject_frame.pack)
    back_button.pack(pady=15)


def quizIntegral():
    global quizIC, vars

    quizIC = tk.Toplevel(root)
    quizIC.title("Integral Calculus Quiz")
    quizIC.geometry('750x500')

    integral_questions = [
        ["Integrate the function, ∫cos(tan z)sec**2 zdz.",
         "A. -sin(tan z)+C",
         "B. tan(sin z)+C",
         "C. sin(tan z)+C"],
        ["Using the power reduction integration technique, integrate ∫sin**4 (1/3)tdt",
         "A. 3/8t-3/4sin 2/3t+3/32sin 4/3t+C",
         "B. 4/3t+3/32sin t+C",
         "C. 1/8t+3/32sin 2/3t+C"],
        ["Integrate 02x cosh x**2 dx by substitution.",
         "A. - sinh 4x",
         "B. 1/4sinh 2 ",
         "C.1/2sinh 4 "]
    ]
    correct_answers_integral = [3, 1, 3]

    vars = []
    for i, question in enumerate(integral_questions):
        label = ttk.Label(quizIC, text=f"Q{i + 1}: {question[0]}", font=("Helvetica", 12), anchor='w')
        label.pack(pady=5)

        var = IntVar()
        vars.append(var)

        options = question[1:]
        for j, option in enumerate(options, start=1):
            radio_button = ttk.Radiobutton(quizIC, text=option, variable=var, value=j)
            radio_button.pack(pady=2, padx=20)

    def calculateScore():
        score = 0
        for i, var in enumerate(vars):
            selected_answer = var.get()
            if selected_answer == correct_answers_integral[i]:
                score += 1
        messagebox.showinfo("Quiz Result", f"Your score is: {score}/{len(integral_questions)}")
        show_subject_interface()

    submit_button = ttk.Button(quizIC, text="Submit", command=calculateScore)
    submit_button.pack(pady=15)

    back_button = ttk.Button(quizIC, text="Back to Subjects", command=show_subject_interface)
    back_button.pack(pady=15)


def quizEngineering():
    global quizEDA, vars

    quizEDA = tk.Toplevel(root)
    quizEDA.title("Engineering Data Analysis Quiz")
    quizEDA.geometry('750x500')

    engineering_questions = [
        [
            "There are four balls of four different colors. Two balls are taken at a time and arranged in a definite order. For example, if a white and a red balls are taken, one definite arrangement is white first, red second, and other arrangement is red first, white second. How many such arrangements are possible?",
            "A. 20",
            "B. 2",
            "C. 15"],
        [
            "An urn contains 6 red marbles and 4 black marbles. Two marbles are drawn in succession with replacement from the urn. What is the probability that the 1st marble is red and the 2nd marble is black?",
            "A. 6/25",
            "B. 5/50",
            "C. 3/35"],
        [
            "A committee is composed of six Democrats and five Republicans. Three of the Democrats are men, and 3 of the Republicans are men. If a man is selected for chairman, what is the probability that he is a Republican?",
            "A. 3/5",
            "B. 1/2",
            "C. 3/4"]
    ]
    correct_answers_engineering = [2, 1, 2]

    vars = []
    for i, question in enumerate(engineering_questions):
        label = ttk.Label(quizEDA, text=f"Q{i + 1}: {question[0]}", font=("Helvetica", 12), anchor='w')
        label.pack(pady=5)

        var = IntVar()
        vars.append(var)

        options = question[1:]
        for j, option in enumerate(options, start=1):
            radio_button = ttk.Radiobutton(quizEDA, text=option, variable=var, value=j)
            radio_button.pack(pady=2, padx=20)

    def calculateScore():
        score = 0
        for i, var in enumerate(vars):
            selected_answer = var.get()
            if selected_answer == correct_answers_engineering[i]:
                score += 1
        messagebox.showinfo("Quiz Result", f"Your score is: {score}/{len(engineering_questions)}")
        show_subject_interface()

    submit_button = ttk.Button(quizEDA, text="Submit", command=calculateScore)
    submit_button.pack(pady=15)

    back_button = ttk.Button(quizEDA, text="Back to Subjects", command=show_subject_interface)
    back_button.pack(pady=15)


def quizDEquation():
    global quizDE, vars

    quizDE = tk.Toplevel(root)
    quizDE.title("Differential Equations Quiz")
    quizDE.geometry('750x500')

    de_questions = [
        ["Eliminate the arbitrary constant: y = ax2+bx+c",
         "A. y''' = 0",
         "B. y'' + y''' = 0",
         "C. y' +y'' + y''' = 0"],
        ["Find the derivative of y = ln²x",
         "A. 12y^3",
         "B. 4y^2",
         "C. x^2"],
        ["Given y = 1/√x-1, find y’",
         "A. tan-1yx=log y + C",
         "B. tan-1yx=log x + C",
         "C. tan-1xy=log x + C"]
    ]
    correct_answers_de = [1, 3, 2]

    vars = []
    for i, question in enumerate(de_questions):
        label = ttk.Label(quizDE, text=f"Q{i + 1}: {question[0]}", font=("Helvetica", 12), anchor='w')
        label.pack(pady=5)

        var = IntVar()
        vars.append(var)

        options = question[1:]
        for j, option in enumerate(options, start=1):
            radio_button = ttk.Radiobutton(quizDE, text=option, variable=var, value=j)
            radio_button.pack(pady=2, padx=20)

    def calculateScore():
        score = 0
        for i, var in enumerate(vars):
            selected_answer = var.get()
            if selected_answer == correct_answers_de[i]:
                score += 1
        messagebox.showinfo("Quiz Result", f"Your score is: {score}/{len(de_questions)}")
        show_subject_interface()

    submit_button = ttk.Button(quizDE, text="Submit", command=calculateScore)
    submit_button.pack(pady=15)

    back_button = ttk.Button(quizDE, text="Back to Subjects", command=show_subject_interface)
    back_button.pack(pady=15)


def quizMmw():
    global quizMmw, vars

    quizMmw = tk.Toplevel(root)
    quizMmw.title("Mathematics in the Modern World Quiz")
    quizMmw.geometry('750x500')

    mmw_questions = [
        ["Which number is next in the Fibonacci sequence of numbers: 1, 1, 2, 3, 5, 8, 13, 21 . .?",
         "A. 55",
         "B. 34",
         "C. 8"],
        [" g(x) = − x + 5 ; f(x) = 2x − 3. Find (g ◦ f)(x).",
         "A. − 2x + 8",
         "B. - 4x + 2",
         "C. − 8x + 2"],
        [
            " In Spearman rank correlation coefficient rs = 1- 6∑d^2/n(n^2-1), the maximum value of ∑d^2 in case of untied rank is: ",
            "A. 1/2 (n^2 - 1)",
            "B. 1/4n(n^2 - 1)",
            "C. 1/3n(n^2 - 1)"]
    ]
    correct_answers_mmw = [2, 1, 3]

    vars = []
    for i, question in enumerate(mmw_questions):
        label = ttk.Label(quizMmw, text=f"Q{i + 1}: {question[0]}", font=("Helvetica", 12), anchor='w')
        label.pack(pady=5)

        var = IntVar()
        vars.append(var)

        options = question[1:]
        for j, option in enumerate(options, start=1):
            radio_button = ttk.Radiobutton(quizMmw, text=option, variable=var, value=j)
            radio_button.pack(pady=2, padx=20)

    def calculateScore():
        score = 0
        for i, var in enumerate(vars):
            selected_answer = var.get()
            if selected_answer == correct_answers_mmw[i]:
                score += 1
        messagebox.showinfo("Quiz Result", f"Your score is: {score}/{len(mmw_questions)}")
        show_subject_interface()

    submit_button = ttk.Button(quizMmw, text="Submit", command=calculateScore)
    submit_button.pack(pady=15)

    back_button = ttk.Button(quizMmw, text="Back to Subjects", command=show_subject_interface)
    back_button.pack(pady=15)


# Differential Calculus
def show_limit_topic():
    hide_all_interfaces()
    limits_frame.pack()


def show_increment_topic():
    hide_all_interfaces()
    increment_frame.pack(expand=True, fill="both")


def show_trigo_topic():
    hide_all_interfaces()
    trigo_frame.pack(expand=True, fill="both")


def show_inverse_topic():
    hide_all_interfaces()
    inverse_frame.pack()
    inverse_frame.pack(expand=True, fill="both")


def show_exponent_topic():
    hide_all_interfaces()
    exponent_frame.pack()
    exponent_frame.pack(expand=True, fill="both")


def show_logar_topic():
    hide_all_interfaces()
    logar_frame.pack()
    logar_frame.pack(expand=True, fill="both")


# Integral Calculus
def show_integration_topic():
    hide_all_interfaces()
    integration_frame.pack()
    integration_frame.pack(expand=True, fill="both")


def show_exponential_topic():
    hide_all_interfaces()
    exponential_frame.pack()
    exponential_frame.pack(expand=True, fill="both")


def show_trigonometric_topic():
    hide_all_interfaces()
    trigonometric_frame.pack()
    trigonometric_frame.pack(expand=True, fill="both")


def show_inversetrigo_topic():
    hide_all_interfaces()
    inversetrigo_frame.pack()
    inversetrigo_frame.pack(expand=True, fill="both")


def show_hyperbolic_topic():
    hide_all_interfaces()
    hyperbolic_frame.pack()
    hyperbolic_frame.pack(expand=True, fill="both")


def show_power_topic():
    hide_all_interfaces()
    power_frame.pack()
    power_frame.pack(expand=True, fill="both")


# Engineering Data Analysis

def show_permutation_topic():
    hide_all_interfaces()
    permutation_frame.pack()
    permutation_frame.pack(expand=True, fill="both")


def show_combination_topic():
    hide_all_interfaces()
    combination_frame.pack()
    combination_frame.pack(expand=True, fill="both")


def show_mathematical_topic():
    hide_all_interfaces()
    mathematical_frame.pack()
    mathematical_frame.pack(expand=True, fill="both")


def show_odds_topic():
    hide_all_interfaces()
    odds_frame.pack()
    odds_frame.pack(expand=True, fill="both")


def show_mutually_topic():
    hide_all_interfaces()
    mutually_frame.pack()
    mutually_frame.pack(expand=True, fill="both")


def show_independent_topic():
    hide_all_interfaces()
    independent_frame.pack()
    independent_frame.pack(expand=True, fill="both")


# Differential Equations
def show_differential_topic():
    hide_all_interfaces()
    differential_frame.pack()
    differential_frame.pack(expand=True, fill="both")


def show_seperation_topic():
    hide_all_interfaces()
    seperation_frame.pack()
    seperation_frame.pack(expand=True, fill="both")


def show_arbitrary_topic():
    hide_all_interfaces()
    arbitrary_frame.pack()
    arbitrary_frame.pack(expand=True, fill="both")


def show_homogeneous_topic():
    hide_all_interfaces()
    homogeneous_frame.pack()
    homogeneous_frame.pack(expand=True, fill="both")


def show_exact_topic():
    hide_all_interfaces()
    exact_frame.pack()
    exact_frame.pack(expand=True, fill="both")


def show_nonexact_topic():
    hide_all_interfaces()
    nonexact_frame.pack()
    nonexact_frame.pack(expand=True, fill="both")


# Mathematics in the Modern World

def show_fibonacci_topic():
    hide_all_interfaces()
    fibonacci_frame.pack()
    fibonacci_frame.pack(expand=True, fill="both")


def show_operations_topic():
    hide_all_interfaces()
    operations_frame.pack()
    operations_frame.pack(expand=True, fill="both")


def show_simple_topic():
    hide_all_interfaces()
    simple_frame.pack()
    simple_frame.pack(expand=True, fill="both")


def show_means_topic():
    hide_all_interfaces()
    means_frame.pack()
    means_frame.pack(expand=True, fill="both")


def show_ttest_topic():
    hide_all_interfaces()
    ttest_frame.pack()
    ttest_frame.pack(expand=True, fill="both")


def show_pearson_topic():
    hide_all_interfaces()
    pearson_frame.pack()
    pearson_frame.pack(expand=True, fill="both")


root = tk.Tk()
style = ttk.Style("morph")

root.title("Course Helper")
root.geometry('750x500')

# MAIN FRAMES
main_frame = tk.Frame(root)
login_frame = tk.Frame(root)
register_frame = tk.Frame(root)
subject_frame = tk.Frame(root)
topicdc_frame = tk.Frame(root)
topicic_frame = tk.Frame(root)
topiceda_frame = tk.Frame(root)
topicde_frame = tk.Frame(root)
topicmmw_frame = tk.Frame(root)
quiz_frame = tk.Frame(root)

# TOPICS FRAME
# Differential Calculus
limits_frame = tk.Frame(root)
increment_frame = ScrolledFrame(root)
trigo_frame = ScrolledFrame(root)
inverse_frame = ScrolledFrame(root)
exponent_frame = ScrolledFrame(root)
logar_frame = ScrolledFrame(root)

# IC
integration_frame = ScrolledFrame(root)
exponential_frame = ScrolledFrame(root)
trigonometric_frame = ScrolledFrame(root)
inversetrigo_frame = ScrolledFrame(root)
hyperbolic_frame = ScrolledFrame(root)
power_frame = ScrolledFrame(root)

# EDA
permutation_frame = ScrolledFrame(root)
mathematical_frame = ScrolledFrame(root)
combination_frame = ScrolledFrame(root)
odds_frame = ScrolledFrame(root)
mutually_frame = ScrolledFrame(root)
independent_frame = ScrolledFrame(root)

# DE
differential_frame = ScrolledFrame(root)
seperation_frame = ScrolledFrame(root)
arbitrary_frame = ScrolledFrame(root)
homogeneous_frame = ScrolledFrame(root)
exact_frame = ScrolledFrame(root)
nonexact_frame = ScrolledFrame(root)

# MMW
fibonacci_frame = ScrolledFrame(root)
operations_frame = ScrolledFrame(root)
simple_frame = ScrolledFrame(root)
means_frame = ScrolledFrame(root)
ttest_frame = ScrolledFrame(root)
pearson_frame = ScrolledFrame(root)

# Login Interface

login_lbl = ttk.Label(login_frame, text="Login", style="default", font=("Calibri Light", 20))
login_lbl.pack(pady=15)

username_lbl_login = ttk.Label(login_frame, text="Username", style="default", font=("Calibri Light", 12))
username_lbl_login.pack(pady=0)
entry_login_username = ttk.Entry(login_frame)
entry_login_username.pack(pady=10)

password_lbl_login = ttk.Label(login_frame, text="Password", style="default", font=("Calibri Light", 12))
password_lbl_login.pack(pady=0)
entry_login_password = ttk.Entry(login_frame)
entry_login_password.pack(pady=15)

login_btn = ttk.Button(login_frame, text="Login", style="primary-outline", command=login, width=10)
login_btn.pack(pady=10)

register_btn = ttk.Button(login_frame, text="Register", style="primary-outline", command=show_register_interface,
                          width=10)
register_btn.pack(pady=10)

# Register Interface

register_lbl = ttk.Label(register_frame, text="Register", style="default", font=("Calibri Light", 20))
register_lbl.pack(pady=15)

username_lbl_register = ttk.Label(register_frame, text="Username", style="default", font=("Calibri Light", 12))
username_lbl_register.pack(pady=0)
entry_register_username = ttk.Entry(register_frame)
entry_register_username.pack(pady=10)

password_lbl_register = ttk.Label(register_frame, text="Password", style="default", font=("Calibri Light", 12))
password_lbl_register.pack(pady=0)
entry_register_password = ttk.Entry(register_frame)
entry_register_password.pack(pady=15)

cpassword_lbl_register = ttk.Label(register_frame, text=" Confirm Password", style="default",
                                   font=("Calibri Light", 12))
cpassword_lbl_register.pack(pady=0)
entry_register_confirmpassword = ttk.Entry(register_frame)
entry_register_confirmpassword.pack(pady=15)

register_submit_btn = ttk.Button(register_frame, text="Submit", style="primary-outline", command=connect_database,
                                 width=10)
register_submit_btn.pack(pady=15)

check = IntVar()
cinput = IntVar()
terms_checkbtn = ttk.Checkbutton(register_frame, text="I agree to have read the Terms and Condition", width=40,
                                 variable=check)
terms_checkbtn.pack(pady=10)
input_checkbtn = ttk.Checkbutton(register_frame, text="I agree to have inputted the correct details", width=40,
                                 variable=cinput)
input_checkbtn.pack(pady=10)
backlogin_submit_btn = ttk.Button(register_frame, text="Back to Login", style="primary-outline",
                                  command=show_login_interface, width=25)
backlogin_submit_btn.pack(pady=15)

# Subject Interface
subject_lbl = ttk.Label(subject_frame, text="Please Choose a Subject Below", style="default")
subject_lbl.pack(pady=15)

ttk.Button(subject_frame, text="Differential Calculus", style="success-outline",
           command=show_topicdc_interface,
           width=30).pack(pady=15)
ttk.Button(subject_frame, text="Integral Calculus", style="success-outline",
           command=show_topicic_interface,
           width=30).pack(pady=15)
ttk.Button(subject_frame, text="Engineering Data Analysis", style="success-outline",
           command=show_topiceda_interface,
           width=30).pack(pady=15)
ttk.Button(subject_frame, text="Differential Equations", style="success-outline",
           command=show_topicde_interface,
           width=30).pack(pady=15)
ttk.Button(subject_frame, text="Mathematics in the Modern World", style="success-outline",
           command=show_topicmmw_interface, width=30).pack(pady=15)
ttk.Button(subject_frame, text="Logout", style="danger-outline", width=15).pack(pady=20)

# Topic Differential Calculus
ttk.Button(topicdc_frame, text="Topic 1: Limits", style="success-outline",
           command=show_limit_topic, width=50).pack(pady=15)
ttk.Button(topicdc_frame, text="Topic 2: Increment Method", style="success-outline",
           command=show_increment_topic,
           width=50).pack(pady=15)
ttk.Button(topicdc_frame, text="Topic 3: Trigonometric Functions", style="success-outline", command=show_trigo_topic,
           width=50).pack(pady=15)
ttk.Button(topicdc_frame, text="Topic 4: Inverse Trigonometric Functions", style="success-outline",
           command=show_inverse_topic, width=50).pack(pady=15)
ttk.Button(topicdc_frame, text="Topic 5: Exponential Functions", style="success-outline",
           command=show_exponent_topic,
           width=50).pack(pady=15)
ttk.Button(topicdc_frame, text="Topic 6: Logarithmic", style="success-outline",
           command=show_logar_topic,
           width=50).pack(pady=15)
ttk.Button(topicdc_frame, text="Quiz", style="danger-outline",
           command=quizDifferential, width=25).pack(pady=15)
ttk.Button(topicdc_frame, text="Back to Subjects", style="danger-outline",
           command=show_subject_interface,
           width=25).pack(pady=15)

# Topic Integral Calculus
ttk.Button(topicic_frame, text="Topic 1: Integration by Substitution", style="success-outline",
           command=show_integration_topic, width=50).pack(pady=15)
ttk.Button(topicic_frame, text="Topic 2: Exponential Function", style="success-outline",
           command=show_exponential_topic, width=50).pack(pady=15)
ttk.Button(topicic_frame, text="Topic 3: Trigonometric Function", style="success-outline",
           command=show_trigonometric_topic, width=50).pack(pady=15)
ttk.Button(topicic_frame, text="Topic 4: Inverse Trigonometric Functions", style="success-outline",
           command=show_inversetrigo_topic, width=50).pack(pady=15)
ttk.Button(topicic_frame, text="Topic 5: Hyperbolic Functions", style="success-outline",
           command=show_hyperbolic_topic, width=50).pack(pady=15)
ttk.Button(topicic_frame, text="Topic 6: Power Reduction", style="success-outline",
           command=show_power_topic, width=50).pack(pady=15)
ttk.Button(topicic_frame, text="Quiz", style="danger-outline", command=quizIntegral, width=25).pack(pady=15)
ttk.Button(topicic_frame, text="Back to Subjects", style="danger-outline", command=show_subject_interface,
           width=25).pack(pady=15)

# Topic Engineering Data Analysis
ttk.Button(topiceda_frame, text="Topic 1: Permutation", style="success-outline",
           command=show_permutation_topic, width=50).pack(pady=15)
ttk.Button(topiceda_frame, text="Topic 2: Combination", style="success-outline",
           command=show_combination_topic, width=50).pack(pady=15)
ttk.Button(topiceda_frame, text="Topic 3: Mathematical Expectation", style="success-outline",
           command=show_mathematical_topic, width=50).pack(pady=15)
ttk.Button(topiceda_frame, text="Topic 4: Odds", style="success-outline",
           command=show_odds_topic, width=50).pack(pady=15)
ttk.Button(topiceda_frame, text="Topic 5: Probability of Mutually Exclusive Events", style="success-outline",
           command=show_mutually_topic, width=50).pack(pady=15)
ttk.Button(topiceda_frame, text="Topic 6: Probability of Independent Events", style="success-outline",
           command=show_independent_topic, width=50).pack(pady=15)
ttk.Button(topiceda_frame, text="Quiz", style="danger-outline", command=quizEngineering, width=25).pack(pady=15)
ttk.Button(topiceda_frame, text="Back to Subjects", style="danger-outline", command=show_subject_interface,
           width=25).pack(pady=15)

# Topic Differential Equations
ttk.Button(topicde_frame, text="Topic 1: Solution  Differential Equation", style="success-outline",
           command=show_differential_topic, width=50).pack(pady=15)
ttk.Button(topicde_frame, text="Topic 2: Separation of Variables", style="success-outline",
           command=show_seperation_topic, width=50).pack(pady=15)
ttk.Button(topicde_frame, text="Topic 3: Eliminating Arbitrary Constant", style="success-outline",
           command=show_arbitrary_topic, width=50).pack(pady=15)
ttk.Button(topicde_frame, text="Topic 4: Homogeneous Differential Equation", style="success-outline",
           command=show_homogeneous_topic, width=50).pack(pady=15)
ttk.Button(topicde_frame, text="Topic 5: Exact Differential Equation", style="success-outline",
           command=show_exact_topic, width=50).pack(pady=15)
ttk.Button(topicde_frame, text="Topic 6: Non-Exact Differential Equation", style="success-outline",
           command=show_nonexact_topic, width=50).pack(pady=15)
ttk.Button(topicde_frame, text="Quiz", style="danger-outline", command=quizDEquation, width=25).pack(pady=15)
ttk.Button(topicde_frame, text="Back to Subjects", style="danger-outline", command=show_subject_interface,
           width=25).pack(pady=15)

# Topic Mathematics in Modern World
ttk.Button(topicmmw_frame, text="Topic 1: Fibonacci Sequence", style="success-outline",
           command=show_fibonacci_topic, width=50).pack(pady=15)
ttk.Button(topicmmw_frame, text="Topic 2: Operations on Functions", style="success-outline",
           command=show_operations_topic, width=50).pack(pady=15)
ttk.Button(topicmmw_frame, text="Topic 3: Simple Interest Formula", style="success-outline",
           command=show_simple_topic, width=50).pack(pady=15)
ttk.Button(topicmmw_frame, text="Topic 4: Tests Concerning Means", style="success-outline",
           command=show_means_topic, width=50).pack(pady=15)
ttk.Button(topicmmw_frame, text="Topic 5: T-Test between Population Mean and Sample Mean",
           style="success-outline",
           command=show_ttest_topic, width=50).pack(pady=15)
ttk.Button(topicmmw_frame, text="Topic 6: Pearson Correlation Coefficient", style="success-outline",
           command=show_pearson_topic, width=50).pack(pady=15)
ttk.Button(topicmmw_frame, text="Quiz", style="danger-outline", command=quizMmw, width=25).pack(pady=15)
ttk.Button(topicmmw_frame, text="Back to Subjects", style="danger-outline", command=show_subject_interface,
           width=25).pack(pady=15)

# DF: LIMITS
limits_lbl = ttk.Label(limits_frame, text="Limits", style="default", font=("Calibri Light", 20))
limits_lbl.pack(pady=15)
desc_lbl = ttk.Label(limits_frame,
                     text="Limits Formula", style="default",
                     font=("Calibri Light", 20), wraplength=400)
desc_lbl.pack(pady=15)
image_path = "images/limits.png"
img = tk.PhotoImage(file=image_path)
limits_lbl = ttk.Label(limits_frame, image=img)
limits_lbl.image = img
limits_lbl.pack(pady=15)
limits_lbl = ttk.Label(limits_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))
limits_lbl.pack(pady=15)
image_path = "images/limits_e.png"
img = tk.PhotoImage(file=image_path)
limits_lbl = ttk.Label(limits_frame, image=img)
limits_lbl.image = img
limits_lbl.pack(pady=15)

back_btn = ttk.Button(limits_frame, text="Back", style="primary-outline",
                      command=show_topicdc_interface, width=25)
back_btn.pack(pady=15)

# DF : INCREMENT METHOD
increment_lbl = ttk.Label(increment_frame, text="Increment Method", style="default", font=("Calibri Light", 20))
increment_lbl.pack(pady=15)
desc_lbl = ttk.Label(increment_frame,
                     text="Increment Method Formula",
                     style="default", font=("Calibri Light", 20), wraplength=400)
desc_lbl.pack(pady=15)
image_path = "images/incremen.png"
img = tk.PhotoImage(file=image_path)
limits_lbl = ttk.Label(increment_frame, image=img)
limits_lbl.image = img
limits_lbl.pack(pady=15)
limits_lbl = ttk.Label(increment_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))
limits_lbl.pack(pady=15)
image_path = "images/incremen_e.png"
img = tk.PhotoImage(file=image_path)
limits_lbl = ttk.Label(increment_frame, image=img)
limits_lbl.image = img
limits_lbl.pack(pady=15)
back_btn = ttk.Button(increment_frame, text="Back", style="primary-outline",
                      command=show_topicdc_interface, width=25)
back_btn.pack(pady=15)

# DF : TRIGONOMETRIC FUNCTIONS
trigo_lbl = ttk.Label(trigo_frame, text="Trigonometric Function", style="default", font=("Calibri Light", 20))
trigo_lbl.pack(pady=15)

desc_lbl = ttk.Label(trigo_frame,
                     text="Trigonometric Function Formula",
                     style="default", font=("Calibri Light", 20), wraplength=400)
desc_lbl.pack(pady=15)
image_path = "images/Trigo.png"
img = tk.PhotoImage(file=image_path)
limits_lbl = ttk.Label(trigo_frame, image=img)
limits_lbl.image = img
limits_lbl.pack(pady=15)
limits_lbl = ttk.Label(trigo_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))
limits_lbl.pack(pady=15)
image_path = "images/Trigo_e.png"
img = tk.PhotoImage(file=image_path)
limits_lbl = ttk.Label(trigo_frame, image=img)
limits_lbl.image = img
limits_lbl.pack(pady=15)

back_btn = ttk.Button(trigo_frame, text="Back to Login", style="primary-outline",
                      command=show_topicdc_interface, width=25)
back_btn.pack(pady=15)

# DF : INVERSE TRIGONOMETRIC FUNCTIONS
inverse_lbl = ttk.Label(inverse_frame, text="Inverse Trigonometric Function", style="default",
                        font=("Calibri Light", 20))
inverse_lbl.pack(pady=15)

desc_lbl = ttk.Label(inverse_frame,
                     text="Inverse Trigonometric Formula",
                     style="default", font=("Calibri Light", 20), wraplength=400)
desc_lbl.pack(pady=15)

image_path = "images/inverse.png"
img = tk.PhotoImage(file=image_path)
inverse_lbl = ttk.Label(inverse_frame, image=img)
inverse_lbl.image = img
inverse_lbl.pack(pady=15)
inverse_lbl = ttk.Label(inverse_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))
inverse_lbl.pack(pady=15)
image_path = "images/inverse_e.png"
img = tk.PhotoImage(file=image_path)
inverse_lbl = ttk.Label(inverse_frame, image=img)
inverse_lbl.image = img
inverse_lbl.pack(pady=15)

back_btn = ttk.Button(inverse_frame, text="Back to Login", style="primary-outline",
                      command=show_topicdc_interface, width=25)
back_btn.pack(pady=15)
# DF : EXPONENTIAL FUNCTIONS
exponent_lbl = ttk.Label(exponent_frame, text="Exponential Functions", style="default", font=("Calibri Light", 20))
exponent_lbl.pack(pady=15)

desc_lbl = ttk.Label(exponent_frame,
                     text="Exponential Functions Formula",
                     style="default", font=("Calibri Light", 20), wraplength=400)
desc_lbl.pack(pady=15)

image_path = "images/exponent.png"
img = tk.PhotoImage(file=image_path)
exponent_lbl = ttk.Label(exponent_frame, image=img)
exponent_lbl.image = img
exponent_lbl.pack(pady=15)
exponent_lbl = ttk.Label(exponent_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))
exponent_lbl.pack(pady=15)
image_path = "images/exponent_e.png"
img = tk.PhotoImage(file=image_path)
exponent_lbl = ttk.Label(exponent_frame, image=img)
exponent_lbl.image = img
exponent_lbl.pack(pady=15)

back_btn = ttk.Button(exponent_frame, text="Back to Login", style="primary-outline",
                      command=show_topicdc_interface, width=25)
back_btn.pack(pady=15)

# DF : LOGARITHMIC
logar_lbl = ttk.Label(logar_frame, text="Logarithmic Functions", style="default", font=("Calibri Light", 20))
logar_lbl.pack(pady=15)

desc_lbl = ttk.Label(logar_frame, text="Logarithmic Functions Formula",
                     style="default", font=("Calibri Light", 20), wraplength=400)
desc_lbl.pack(pady=15)

image_path = "images/logar.png"
img = tk.PhotoImage(file=image_path)
logar_lbl = ttk.Label(logar_frame, image=img)
logar_lbl.image = img
logar_lbl.pack(pady=15)
logar_lbl = ttk.Label(logar_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))
logar_lbl.pack(pady=15)
image_path = "images/logar_e.png"
img = tk.PhotoImage(file=image_path)
logar_lbl = ttk.Label(logar_frame, image=img)
logar_lbl.image = img
logar_lbl.pack(pady=15)

back_btn = ttk.Button(logar_frame, text="Back to Login", style="primary-outline",
                      command=show_topicdc_interface, width=25)
back_btn.pack(pady=15)

# IC : Integration by Substitution
integration_lbl = ttk.Label(integration_frame, text="Integration by Substitution", style="default",
                            font=("Calibri Light", 20))
integration_lbl.pack(pady=15)

integration_lbl = ttk.Label(integration_frame,
                            text="Integration by Substitution Formula",
                            style="default", font=("Calibri Light", 20), wraplength=400)
integration_lbl.pack(pady=15)

image_path = "images/integrals1.png"
img = tk.PhotoImage(file=image_path)
integration_lbl = ttk.Label(integration_frame, image=img)
integration_lbl.image = img
integration_lbl.pack(pady=15)

integration_lbl = ttk.Label(integration_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))

image_path = "images/integrals2.png"
img = tk.PhotoImage(file=image_path)
integration_lbl = ttk.Label(integration_frame, image=img)
integration_lbl.image = img
integration_lbl.pack(pady=15)

integration_lbl.pack(pady=15)
image_path = "images/integrals3.png"
img = tk.PhotoImage(file=image_path)
integration_lbl = ttk.Label(integration_frame, image=img)
integration_lbl.image = img
integration_lbl.pack(pady=15)

back_btn = ttk.Button(integration_frame, text="Back to Login", style="primary-outline", command=show_topicic_interface, width=25)
back_btn.pack(pady=15)

# IC : Exponential Function

exponential_lbl = ttk.Label(exponential_frame, text="Exponential Function", style="default", font=("Calibri Light", 20))
exponential_lbl.pack(pady=15)

exponential_lbl = ttk.Label(exponential_frame, text="Exponential Function Formula", style="default", font=("Calibri Light", 20), wraplength=400)
exponential_lbl.pack(pady=15)

image_path = "images/ex.png"
img = tk.PhotoImage(file=image_path)
tri_lbl = ttk.Label(exponential_frame, image=img)
tri_lbl.image = img
tri_lbl.pack(pady=15)

exponential_lbl = ttk.Label(exponential_frame, text="Sample Problem", style="default", font=("Calibri Light", 20), wraplength=400)
exponential_lbl.pack(pady=15)

image_path = "images/ex1.png"
img = tk.PhotoImage(file=image_path)
tri_lbl = ttk.Label(exponential_frame, image=img)
tri_lbl.image = img
tri_lbl.pack(pady=15)

image_path = "images/ex2.png"
img = tk.PhotoImage(file=image_path)
tri_lbl = ttk.Label(exponential_frame, image=img)
tri_lbl.image = img
tri_lbl.pack(pady=15)

image_path = "images/ex3.png"
img = tk.PhotoImage(file=image_path)
tri_lbl = ttk.Label(exponential_frame, image=img)
tri_lbl.image = img
tri_lbl.pack(pady=15)

back_btn = ttk.Button(exponential_frame, text="Back to Login", style="primary-outline", command=show_topicic_interface, width=25)
back_btn.pack(pady=15)

# IC : Trigonometric Function
tri_lbl = ttk.Label(trigonometric_frame, text="Trigonometric Functions", style="default", font=("Calibri Light", 20))
tri_lbl.pack(pady=15)

tri_lbl = ttk.Label(trigonometric_frame, text="Trigonometric Functions Formula", style="default", font=("Calibri Light", 20), wraplength=400)
tri_lbl.pack(pady=15)

image_path = "images/tf.png"
img = tk.PhotoImage(file=image_path)
tri_lbl = ttk.Label(trigonometric_frame, image=img)
tri_lbl.image = img
tri_lbl.pack(pady=15)

tri_lbl = ttk.Label(trigonometric_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))
tri_lbl.pack(pady=15)

image_path = "images/tf1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(trigonometric_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/tf2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(trigonometric_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/tf3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(trigonometric_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/tf4.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(trigonometric_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

back_btn = ttk.Button(trigonometric_frame, text="Back to Login", style="primary-outline", command=show_topicic_interface, width=25)
back_btn.pack(pady=15)

# IC : Inverse Trigonometric Functions

iTri_lbl = ttk.Label(inversetrigo_frame, text="Inverse Trigonometric", style="default", font=("Calibri Light", 20))
iTri_lbl.pack(pady=15)

iTri_lbl = ttk.Label(inversetrigo_frame, text="Inverse Trigonometric Formula", style="default", font=("Calibri Light", 20),wraplength=400)
iTri_lbl.pack(pady=15)

image_path = "images/if.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(inversetrigo_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

iTri_lbl = ttk.Label(inversetrigo_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
iTri_lbl.pack(pady=15)

image_path = "images/if1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(inversetrigo_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/if2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(inversetrigo_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/if3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(inversetrigo_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

back_btn = ttk.Button(inversetrigo_frame, text="Back to Login", style="primary-outline", command=show_topicic_interface, width=25)
back_btn.pack(pady=15)

# IC : Hyperbolic Functions

hyper_lbl = ttk.Label(hyperbolic_frame, text="Hyperbolic Functions", style="default", font=("Calibri Light", 20))
hyper_lbl.pack(pady=15)

hyper_lbl = ttk.Label(hyperbolic_frame, text="Hyperbolic Functions Formula", style="default", font=("Calibri Light", 20),wraplength=400)
hyper_lbl.pack(pady=15)

image_path = "images/h1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(hyperbolic_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)


hyper_lbl = ttk.Label(hyperbolic_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
hyper_lbl.pack(pady=15)

image_path = "images/h2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(hyperbolic_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

back_btn = ttk.Button(hyperbolic_frame, text="Back to Login", style="primary-outline", command=show_topicic_interface, width=25)
back_btn.pack(pady=15)

# IC : Power Reduction
power_lbl = ttk.Label(power_frame, text="Power Reduction Functions", style="default", font=("Calibri Light", 20))
power_lbl.pack(pady=15)

power_lbl = ttk.Label(power_frame, text="Power Reduction Formula", style="default", font=("Calibri Light", 20),wraplength=400)
power_lbl.pack(pady=15)

image_path = "images/p1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(power_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/p2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(power_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

power_lbl = ttk.Label(power_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
power_lbl.pack(pady=15)

image_path = "images/p3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(power_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/p4.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(power_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/p5.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(power_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

back_btn = ttk.Button(power_frame, text="Back to Login", style="primary-outline", command=show_topicic_interface, width=25)
back_btn.pack(pady=15)

# EDA : Permutation

perm_lbl = ttk.Label(permutation_frame, text="Permutation", style="default", font=("Calibri Light", 20))
perm_lbl.pack(pady=15)

perm_lbl = ttk.Label(permutation_frame, text="Permutation Formula", style="default", font=("Calibri Light", 20),wraplength=400)
perm_lbl.pack(pady=15)

image_path = "images/q.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(permutation_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

perm_lbl = ttk.Label(permutation_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
perm_lbl.pack(pady=15)

image_path = "images/q1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(permutation_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

perm_lbl = ttk.Button(permutation_frame, text="Back to Login", style="primary-outline", command=show_topiceda_interface, width=25)
perm_lbl.pack(pady=15)

# EDA : Combination

comb_lbl = ttk.Label(combination_frame, text="Combination", style="default", font=("Calibri Light", 20))
comb_lbl.pack(pady=15)

comb_lbl = ttk.Label(combination_frame, text="Combination Formula", style="default", font=("Calibri Light", 20),wraplength=400)
comb_lbl.pack(pady=15)

image_path = "images/w.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(combination_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

comb_lbl = ttk.Label(combination_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
comb_lbl.pack(pady=15)

image_path = "images/w1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(combination_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

comb_lbl = ttk.Button(combination_frame, text="Back to Login", style="primary-outline", command=show_topiceda_interface, width=25)
comb_lbl.pack(pady=15)

# EDA : Mathematical Expectation

math_lbl = ttk.Label(mathematical_frame, text="Mathematical Expectation", style="default", font=("Calibri Light", 20))
math_lbl.pack(pady=15)

math_lbl = ttk.Label(mathematical_frame, text="Mathematical Expectation Formula", style="default", font=("Calibri Light", 20),wraplength=400)
math_lbl.pack(pady=15)

image_path = "images/e.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(mathematical_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

math_lbl = ttk.Label(mathematical_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
math_lbl.pack(pady=15)

image_path = "images/e2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(mathematical_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

math_lbl = ttk.Button(mathematical_frame, text="Back to Login", style="primary-outline", command=show_topiceda_interface, width=25)
math_lbl.pack(pady=15)

# EDA : Odds

odd_lbl = ttk.Label(odds_frame, text="Odds", style="default", font=("Calibri Light", 20))
odd_lbl.pack(pady=15)

odd_lbl = ttk.Label(odds_frame, text="Odds Formula", style="default", font=("Calibri Light", 20),wraplength=400)
odd_lbl.pack(pady=15)

image_path = "images/o.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(odds_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

odd_lbl = ttk.Label(odds_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
odd_lbl.pack(pady=15)

image_path = "images/o2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(odds_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/o3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(odds_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

odd_lbl = ttk.Button(odds_frame, text="Back to Login", style="primary-outline", command=show_topiceda_interface, width=25)
odd_lbl.pack(pady=15)

# EDA : Probability of Mutually Exclusive Events

mut_lbl = ttk.Label(mutually_frame, text="Probability of Mutually Exclusive Events", style="default", font=("Calibri Light", 20))
mut_lbl.pack(pady=15)

mut_lbl = ttk.Label(mutually_frame, text="Probability of Mutually Exclusive Events Formula", style="default", font=("Calibri Light", 20),wraplength=400)
mut_lbl.pack(pady=15)

image_path = "images/mut.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(mutually_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

mut_lbl = ttk.Label(mutually_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
mut_lbl.pack(pady=15)

image_path = "images/mut2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(mutually_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

mut_lbl = ttk.Button(mutually_frame, text="Back to Login", style="primary-outline", command=show_topiceda_interface, width=25)
mut_lbl.pack(pady=15)

# EDA : Probability of Independent Events

indeut_lbl = ttk.Label(independent_frame, text="Probability of Independent Events", style="default", font=("Calibri Light", 20))
indeut_lbl.pack(pady=15)

indeut_lbl = ttk.Label(independent_frame, text="Probability of Independent Events Formula", style="default", font=("Calibri Light", 20),wraplength=400)
indeut_lbl.pack(pady=15)

image_path = "images/ind.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(independent_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

indeut_lbl = ttk.Label(independent_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
indeut_lbl.pack(pady=15)

image_path = "images/ind1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(independent_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)


indeut_lbl = ttk.Button(independent_frame, text="Back to Login", style="primary-outline", command=show_topiceda_interface, width=25)
indeut_lbl.pack(pady=15)

# DE : Solution  Differential Equation

solution_lbl = ttk.Label(differential_frame, text="Solution  Differential Equation", style="default", font=("Calibri Light", 20))
solution_lbl.pack(pady=15)

solution_lbl = ttk.Label(differential_frame, text="Solution  Differential Equation Formula", style="default", font=("Calibri Light", 20),wraplength=400)
solution_lbl.pack(pady=15)

image_path = "images/l.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(differential_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

solution_lbl = ttk.Label(differential_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
solution_lbl.pack(pady=15)

image_path = "images/l2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(differential_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

solution_lbl = ttk.Button(differential_frame, text="Back to Login", style="primary-outline", command=show_topicde_interface, width=25)
solution_lbl.pack(pady=15)

# DE : Separation of Variables

seperation_lbl = ttk.Label(seperation_frame, text="Separation of Variables", style="default", font=("Calibri Light", 20))
seperation_lbl.pack(pady=15)

seperation_lbl = ttk.Label(seperation_frame, text="Separation of Variables Formula", style="default", font=("Calibri Light", 20),wraplength=400)
seperation_lbl.pack(pady=15)

image_path = "images/m.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(seperation_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

seperation_lbl = ttk.Label(seperation_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
seperation_lbl.pack(pady=15)

image_path = "images/m1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(seperation_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/m2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(seperation_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

seperation_lbl = ttk.Button(seperation_frame, text="Back to Login", style="primary-outline", command=show_topicde_interface, width=25)
seperation_lbl.pack(pady=15)

# DE : Eliminating Arbitrary Constant

arbit_lbl = ttk.Label(arbitrary_frame, text="Eliminating Arbitrary Constant", style="default", font=("Calibri Light", 20))
arbit_lbl.pack(pady=15)

arbit_lbl = ttk.Label(arbitrary_frame, text="Eliminating Arbitrary Constant Formula", style="default", font=("Calibri Light", 20),wraplength=400)
arbit_lbl.pack(pady=15)

image_path = "images/ar.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(arbitrary_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

arbit_lbl = ttk.Label(arbitrary_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
arbit_lbl.pack(pady=15)

image_path = "images/ar2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(arbitrary_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

arbit_lbl = ttk.Button(arbitrary_frame, text="Back to Login", style="primary-outline", command=show_topicde_interface, width=25)
arbit_lbl.pack(pady=15)

# DE : Homogeneous Differential Equation

homo_lbl = ttk.Label(homogeneous_frame, text="Homogeneous Differential Equation", style="default", font=("Calibri Light", 20))
homo_lbl.pack(pady=15)

homo_lbl = ttk.Label(homogeneous_frame, text="Homogeneous Differential Equation Formula", style="default", font=("Calibri Light", 20),wraplength=400)
homo_lbl.pack(pady=15)

image_path = "images/hom2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(homogeneous_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

homo_lbl = ttk.Label(homogeneous_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
homo_lbl.pack(pady=15)

image_path = "images/hom3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(homogeneous_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

homo_lbl = ttk.Button(homogeneous_frame, text="Back to Login", style="primary-outline", command=show_topicde_interface, width=25)
homo_lbl.pack(pady=15)

# DE : Exact Differential Equation

exact_lbl = ttk.Label(exact_frame, text="Exact Differential Equation", style="default", font=("Calibri Light", 20))
exact_lbl.pack(pady=15)

exact_lbl = ttk.Label(exact_frame, text="Exact Differential Equation Formula", style="default", font=("Calibri Light", 20),wraplength=400)
exact_lbl.pack(pady=15)

image_path = "images/g.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(exact_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

exact_lbl = ttk.Label(exact_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
exact_lbl.pack(pady=15)

image_path = "images/g2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(exact_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

exact_lbl = ttk.Button(exact_frame, text="Back to Login", style="primary-outline", command=show_topicde_interface, width=25)
exact_lbl.pack(pady=15)

# DE : Non-Exact Differential Equation

non_lbl = ttk.Label(nonexact_frame, text="Non-Exact Differential Equation", style="default", font=("Calibri Light", 20))
non_lbl.pack(pady=15)

non_lbl = ttk.Label(nonexact_frame, text="Non-Exact Differential Equation Formula", style="default", font=("Calibri Light", 20),wraplength=400)
non_lbl.pack(pady=15)

image_path = "images/f1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(nonexact_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

non_lbl = ttk.Label(nonexact_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
non_lbl.pack(pady=15)

image_path = "images/f2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(nonexact_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/f3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(nonexact_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/f4.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(nonexact_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/f5.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(nonexact_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

non_lbl = ttk.Button(nonexact_frame, text="Back to Login", style="primary-outline", command=show_topicde_interface, width=25)
non_lbl.pack(pady=15)

# MMW : Fibonacci Sequence

mmw_lbl = ttk.Label(fibonacci_frame, text="Fibonacci Sequence", style="default", font=("Calibri Light", 20))
mmw_lbl.pack(pady=15)

mmw_lbl = ttk.Label(fibonacci_frame, text="Fibonacci Sequence Formula", style="default", font=("Calibri Light", 20),wraplength=400)
mmw_lbl.pack(pady=15)

image_path = "images/v.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(fibonacci_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

mmw_lbl = ttk.Label(fibonacci_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
mmw_lbl.pack(pady=15)

image_path = "images/v2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(fibonacci_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/v3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(fibonacci_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

mmw_lbl = ttk.Button(fibonacci_frame, text="Back to Login", style="primary-outline", command=show_topicmmw_interface, width=25)
mmw_lbl.pack(pady=15)

# MMW : Operations on Functions

func_lbl = ttk.Label(operations_frame, text="Operations on Functions", style="default", font=("Calibri Light", 20))
func_lbl.pack(pady=15)

func_lbl = ttk.Label(operations_frame, text="Operations on Functions Formula", style="default", font=("Calibri Light", 20),wraplength=400)
func_lbl.pack(pady=15)

image_path = "images/k1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(operations_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

func_lbl = ttk.Label(operations_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
func_lbl.pack(pady=15)

image_path = "images/k2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(operations_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/k3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(operations_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/k4.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(operations_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/k5.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(operations_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/k6.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(operations_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/k7.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(operations_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)


func_lbl = ttk.Button(operations_frame, text="Back to Login", style="primary-outline", command=show_topicmmw_interface, width=25)
func_lbl.pack(pady=15)

# MMW : Simple Interest Formula

simple_lbl = ttk.Label(simple_frame, text="Simple Interest Formula", style="default", font=("Calibri Light", 20))
simple_lbl.pack(pady=15)

simple_lbl = ttk.Label(simple_frame, text="Simple Interest Formula Formula", style="default", font=("Calibri Light", 20),wraplength=400)
simple_lbl.pack(pady=15)

image_path = "images/z1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(simple_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

simple_lbl = ttk.Label(simple_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
simple_lbl.pack(pady=15)

image_path = "images/z2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(simple_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/z3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(simple_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/z4.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(simple_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/z5.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(simple_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)


simple_lbl = ttk.Button(simple_frame, text="Back to Login", style="primary-outline", command=show_topicmmw_interface, width=25)
simple_lbl.pack(pady=15)

# MMW : Tests Concerning Means

mean_lbl = ttk.Label(means_frame, text="Tests Concerning Means", style="default", font=("Calibri Light", 20))
mean_lbl.pack(pady=15)

mean_lbl = ttk.Label(means_frame, text="Tests Concerning Means Formula", style="default", font=("Calibri Light", 20),wraplength=400)
mean_lbl.pack(pady=15)

image_path = "images/b1.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(means_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

mean_lbl = ttk.Label(means_frame, text="Sample Problem", style="default", font=("Calibri Light", 20),wraplength=400)
mean_lbl.pack(pady=15)

image_path = "images/b2.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(means_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/b3.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(means_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

image_path = "images/b4.png"
img = tk.PhotoImage(file=image_path)
iTri_lbl = ttk.Label(means_frame, image=img)
iTri_lbl.image = img
iTri_lbl.pack(pady=15)

mean_lbl = ttk.Button(means_frame, text="Back to Login", style="primary-outline", command=show_topicmmw_interface, width=25)
mean_lbl.pack(pady=15)

# MMW : T-Test Comparison between Population Mean and Sample Mean
ttest_lbl = ttk.Label(ttest_frame, text="T-Test between Population Mean and Sample Mean", style="default",
                      font=("Calibri Light", 20))
ttest_lbl.pack(pady=15)

ttest_lbl = ttk.Label(ttest_frame,
                      text=" T-Test between Population Mean and Sample Mean Formula",
                      style="default", font=("Calibri Light", 20), wraplength=400)
ttest_lbl.pack(pady=15)

image_path = "images/ttest.png"
img = tk.PhotoImage(file=image_path)
ttest_lbl = ttk.Label(ttest_frame, image=img)
ttest_lbl.image = img
ttest_lbl.pack(pady=15)

ttest_lbl = ttk.Label(ttest_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))

image_path = "images/ttest2.png"
img = tk.PhotoImage(file=image_path)
ttest_lbl = ttk.Label(ttest_frame, image=img)
ttest_lbl.image = img
ttest_lbl.pack(pady=15)

ttest_lbl.pack(pady=15)
image_path = "images/pearson3.png"
img = tk.PhotoImage(file=image_path)
ttest_lbl = ttk.Label(ttest_frame, image=img)
ttest_lbl.image = img
ttest_lbl.pack(pady=15)

back_btn = ttk.Button(ttest_frame, text="Back to Login", style="primary-outline", command=show_topicmmw_interface,width=25)
back_btn.pack(pady=15)

# MMW : Pearson Product-Moment Correlation Coefficient
Pearson_lbl = ttk.Label(pearson_frame, text="Pearson Correlation Coefficient", style="default",font=("Calibri Light", 20))
Pearson_lbl.pack(pady=15)

Pearson_lbl = ttk.Label(pearson_frame,
                            text="Pearson Correlation Coefficient Formula",
                            style="default", font=("Calibri Light", 20), wraplength=400)
image_path = "images/pearson.png"
img = tk.PhotoImage(file=image_path)
Pearson_lbl = ttk.Label(pearson_frame, image=img)
Pearson_lbl.image = img
Pearson_lbl.pack(pady=15)

Pearson_lbl = ttk.Label(pearson_frame, text="Sample Problem", style="default", font=("Calibri Light", 20))

image_path = "images/pearson2.png"
img = tk.PhotoImage(file=image_path)
Pearson_lbl = ttk.Label(pearson_frame, image=img)
Pearson_lbl.image = img
Pearson_lbl.pack(pady=15)

Pearson_lbl.pack(pady=15)
image_path = "images/pearson3.png"
img = tk.PhotoImage(file=image_path)
Pearson_lbl = ttk.Label(pearson_frame, image=img)
Pearson_lbl.image = img
Pearson_lbl.pack(pady=15)

back_btn = ttk.Button(pearson_frame, text="Back to Login", style="primary-outline", command=show_topicmmw_interface, width=25)
back_btn.pack(pady=15)

show_login_interface()
root.mainloop()

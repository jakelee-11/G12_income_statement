import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
import calendar as cd
import time

# fonts
font = ("monaco", 12)
font_tk = ("monaco", 14)


class start(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.title('Jake\'s household account')
        self.geometry("1300x700")

        for Pages in (StartPage, QuickLook, Budgets, Calendar, Notes):
            frame = Pages(container, self)

            # Display Pages
            self.frames[Pages] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Intro
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background='mediumslateblue')

        homelabel = tk.Label(self, text='Welcome To Jake\'s Household Account!')
        homelabel.pack(padx=5, pady=5)
        homelabel.config(bg='black', fg='white', font=('consolas', 50), height=2, width=50)

        self.homeimg = ImageTk.PhotoImage(Image.open('steak.png'))
        self.img = tk.Label(self, image=self.homeimg)
        self.homeimg.image = self.homeimg
        self.img.pack()

        # Restart Button
        buttonRe = tk.Button(self, text='Restart')

        def restart():
            python = sys.executable
            os.execl(python, python, *sys.argv)
        buttonRe.config(command=restart)
        buttonRe.pack(side=tk.BOTTOM, pady=3)

        # Quit Button
        buttonQuit = tk.Button(self, text='Quit')

        def quit():
            self.quit()
        buttonQuit.config(command=quit)
        buttonQuit.pack(side=tk.BOTTOM, pady=3)

        # Click Continue to continue
        buttonQuickLook = tk.Button(self, text="Continue", command=lambda: controller.show_frame(QuickLook))
        buttonQuickLook.pack(side=tk.BOTTOM, pady=3)


class QuickLook(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background='paleturquoise')
        # Main home_label
        homeL= tk.Label(self, text='Welcome To Jake\'s Household Account!?!')
        homeL.pack(padx=5, pady=5)
        homeL.config(bg='black', fg='white', font=('consolas', 50), height=1, width=50)

        titleL = tk.Label(self, text='This is QuickLook page.', bg='black', fg='white', font=font, height=2, width=30)
        titleL.pack()

        # Image of Warren Buffett
        self.homeimg = ImageTk.PhotoImage(Image.open('warren_buffett.png'))
        self.img = tk.Label(self, image=self.homeimg)
        self.homeimg.image = self.homeimg
        self.img.pack(pady=15)

        pagesL = tk.Label(self, text='List of Windows', font=font, height=1)
        pagesL.place(x=10, y=100)

        # Buttons to direct to menu_windows
        # main_menus = ['Account', 'QuickLook', 'Budgets', 'Calendar', 'Charts&Report', 'Notes', 'Setting']

        quicklookB = tk.Button(self, text='QuickLook', width=10, command=lambda: controller.show_frame(QuickLook))
        quicklookB.place(x=1, y=150)

        budgetB = tk.Button(self, text='Budgets', width=10, command=lambda: controller.show_frame(Budgets))
        budgetB.place(x=1, y=300)

        calendarB = tk.Button(self, text="Calendar", width=10, command=lambda: controller.show_frame(Calendar))
        calendarB.place(x=1, y=450)

        notesB = tk.Button(self, text='Notes', width=10, command=lambda: controller.show_frame(Notes))
        notesB.place(x=1, y=600)

        # Quit Button
        def logout():
            self.quit()

        logoutB = tk.Button(self, text='Log-out', width=10, command=logout)
        logoutB.pack(side=tk.RIGHT)

        buttonRe = tk.Button(self, text='Restart')

        # Restart Button
        def restart():
            python = sys.executable
            os.execl(python, python, *sys.argv)

        buttonRe.config(command=restart, width=10)
        buttonRe.pack(side=tk.RIGHT)


class Budgets(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        homeL = tk.Label(self, text='Welcome To Jake\'s Household Account!?!')
        homeL.pack(padx=5, pady=5)
        homeL.config(bg='black', fg='white', font=('consolas', 50), height=1, width=50)

        titleL = tk.Label(self, text='This is Budgets page.', bg='black', fg='white', font=font, height=2, width=30)
        titleL.pack()

        button1 = tk.Button(self, text="Back to Quicklook", command=lambda: controller.show_frame(QuickLook))
        button1.pack()

        expense_recommended = tk.Label(self, text='Recommended Expense = Transportation, Bills, Clothing, Food, Health Care, Housing, Leisure, Travel, Loans, Others',
                                       fg='deepskyblue', font=('monaco', 13))
        expense_recommended.pack(pady=7)

        income_recommended = tk.Label(self, text='Recommended Income = Child Support, Investments, Rental, Salary & Wages, Social Security, Others',
                                      fg='mediumvioletred', font=('monaco', 13))
        income_recommended.pack()


        # Balance
        frame_bottom = tk.LabelFrame(self, text='Balance', relief=tk.GROOVE)

        option = tk.Label(frame_bottom, text="Click to display option", bg='black', fg='white', width=20, height=1)
        option.pack(side=tk.BOTTOM, padx=10, pady=15)

        # Middle Frame
        middle_frame = tk.Frame(self)
        middle_frame.pack(side=tk.TOP)

        i = self

        # Expense
        def expense():
            category_name = tk.Label(middle_frame, text="What is the tax & interest?")
            category_name.pack()

            categoryE = tk.Entry(middle_frame)
            categoryE.pack()

            amount_income = tk.Label(middle_frame, text="What is amount of expense?")
            amount_income.pack()

            amountE = tk.Entry(middle_frame)
            amountE.pack()

            li = []
            name_list = []
            money_list = []

            def get_data():
                # li.append(categoryE.get())
                # li.append(amountE.get())

                # for data in li:
                #     if len(data) % 2 == 0:
                #         string_categories = data
                #         name_list.append(string_categories)
                #
                #     if len(data) % 2 == 1:
                #         number_money = data
                #         money_list.append(number_money)
                name_list.append(categoryE.get())
                money_list.append(amountE.get())

            get_data = tk.button = tk.Button(self, text="get data", command=get_data)
            get_data.pack(side=tk.TOP)

            # Graphs
            def graph_window():
                # count = 0
                top = tk.Toplevel(i)
                top.wm_title("Graph")  # % self.counter)
                label = tk.Label(top, text="This is Chart")  # #%s")# % self.counter)
                label.pack()  # side="top", fill="both", expand=True, padx=100, pady=100)

                figure = Figure(figsize=(5, 5), dpi=100)
                plots = figure.add_subplot(111)

                plots.plot(name_list, money_list)
                canvas = FigureCanvasTkAgg(figure, top)
                canvas.show()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            graph = tk.button = tk.Button(self, text="Graph", command=graph_window)
            graph.pack(side=tk.TOP)

        # Income
        def income():
            category_name = tk.Label(middle_frame, text="What is the category's name?")
            category_name.pack()

            categoryE = tk.Entry(middle_frame)
            categoryE.pack()

            amount_income = tk.Label(middle_frame, text="What is amount of income?")
            amount_income.pack()

            amountE = tk.Entry(middle_frame)
            amountE.pack()

            li = []
            name_list = []
            money_list = []

            def get_data():
                # li.append(categoryE.get())
                # li.append(amountE.get())
                #
                # for data in li:
                #     if len(data) % 2 == 0:
                #         string_categories = data
                #         name_list.append(string_categories)
                #
                #     if len(data) % 2 == 1:
                #         number_money = data
                #         money_list.append(number_money)
                name_list.append(categoryE.get())
                money_list.append(amountE.get())

            graph = tk.button = tk.Button(self, text="get data", command=get_data)
            graph.pack(side=tk.TOP)

            # Graphs
            def graph_window():
                # count = 0
                top = tk.Toplevel(i)
                top.wm_title("Graph")
                label = tk.Label(top, text="This is Chart")
                label.pack()

                figure = Figure(figsize=(5, 5), dpi=100)
                plots = figure.add_subplot(111)

                plots.plot(name_list, money_list)
                canvas = FigureCanvasTkAgg(figure, top)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                # graph.destroy()

            graph = tk.button = tk.Button(self, text="Graph", command=graph_window)
            graph.pack(side=tk.TOP)

        # create a menu
        popup = tk.Menu(self, tearoff=0)
        popup.add_command(label="Expense", command=expense)
        popup.add_separator()
        popup.add_command(label="Income", command=income)

        def do_popup(event):
            # try:
                popup.tk_popup(event.x_root, event.y_root, 0)
            # finally:
                popup.grab_release()

        option.bind("<Button-1>", do_popup)

        frame_bottom.place(x=200, y=574)


class Calendar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title of Calendar
        homeL = tk.Label(self, text='Welcome To Jake\'s Household Account!?!')
        homeL.pack(padx=5, pady=5)
        homeL.config(bg='black', fg='white', font=('consolas', 50), height=1, width=50)

        # Page Label
        titleL = tk.Label(self, text='This is Calendar page.', bg='black', fg='white', font=font, height=2, width=30)
        titleL.pack()

        # QuickLook Button
        quicklookB = tk.Button(self, text="Back to QuickLook", command=lambda: controller.show_frame(QuickLook))
        quicklookB.pack()

        # Today's calendar                                                                      # % H: % M, time.strftime("%Y-%m-%d")), font=("monaco", 13, 'bold'
        calendar_today = tk.Label(self, text='Today\'s date is {}'.format("%Y-%m-%d"))
        calendar_today.pack(padx=7, pady=7)

        group = tk.LabelFrame(self, text="Calendar", padx=5, pady=5)
        group.pack(padx=10, pady=10)

        # Year
        year_label = tk.Label(group, text='which year?')
        year_label.pack()

        yearE = tk.Entry(group)
        yearE.pack()

        # Month
        month_label = tk.Label(group, text='which month?')
        month_label.pack()

        monthE = tk.Entry(group)
        monthE.pack()

        # Calendar
        def calendar_button():
            calendar = cd.month(int(yearE.get()), int(monthE.get()))
            calendar_display = tk.Label(self, text=calendar, font=("monaco", 25), bg='lightskyblue')
            calendar_display.pack()

            # Remove calendar entries
            def calendar_destroy():
                calendar_display.destroy()
                calendar_remove.destroy()
                yearE.delete(0, tk.END)
                monthE.delete(0, tk.END)

            calendar_remove = tk.Button(self, text="Click to remove a calendar", command=calendar_destroy)
            calendar_remove.pack()

        calendar_getB = tk.Button(self, text='Click to see a calendar', command=calendar_button)
        calendar_getB.pack()


class Notes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Title and design of the page
        homeL = tk.Label(self, text='Welcome To Jake\'s Household Account!?!')
        homeL.pack(padx=5, pady=5)
        homeL.config(bg='black', fg='white', font=('consolas', 50), height=1, width=50)

        titleL = tk.Label(self, text='This is Notes page.', bg='black', fg='white', font=font, height=2, width=30)
        titleL.pack()

        quicklookB = tk.Button(self, text="Back to QuickLook", command=lambda: controller.show_frame(QuickLook))
        quicklookB.pack(padx=5, pady=5)

        # Click to make notes
        def make_notes():
            notesB = tk.Text(self, bg='lightsalmon', width=40, bd=5, height=5, font=font)
            notesB.pack()

            # Remove notes
            def remove_notes():
                notesB.destroy()
                remove_notesB.destroy()

            remove_notesB = tk.Button(self, text='Click to remove notes', command=remove_notes)
            remove_notesB.pack()

        # Button click to make notes
        make_notesB = tk.Button(self, text='Click to make notes', command=make_notes)
        make_notesB.pack(padx=5, pady=5)


app = start()
app.mainloop()

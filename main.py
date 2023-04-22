# This is a sample Python script.
count = 1
color = " "

# import libraries that are used
import pip
import time

# net connectivity;
print(
    "--------------------------------------------------------please follow the instruction-------------------------------------------------------")
print(
    "----------------------------if you are using the software for first time then please have activate internet connection---------------------")
time.sleep(5)

# auto install library code in python if not available requires internet if usinf first time
try:
    import customtkinter as ctk
    from tkinter import *
    import datetime
    import pyttsx3 as pt
    import threading
    import os

except:
    print("can't install ")
    pip.main(['install', 'customtkinter'])
    pip.main(['install', 'datetime'])
    pip.main(['install', 'tkinter'])
    pip.main(['install', 'pyttsx3'])
    pip.main(['install', 'threading'])
    from tkinter import *
    import customtkinter as ctk
    import datetime
    import pyttsx3 as pt
    import threading

def speak(text):
    engine=pt.init()
    engine.say(text)
    engine.runAndWait()

def check(check_v, dat, mon, hou, min):
    while (True):
        current = datetime.datetime.now()
        if check_v == 0:
            print("v==0")
            print("you have a reminder for this moment")
            pass
        elif check_v == 1:
            print("nice")
            if int(dat)==int(current.day) and int(current.month) == int(mon) and int(current.hour) == int(hou) and int(current.minute) == int(min):
                print("good")
                speak("you have a reminder for this moment")

        else:
            print("an internal,error occured sorry for this ")
            break


# to select the color from the given/mentioned set
def select_color():
    global count, color
    count = count + 1
    # color changing list with the hexcode of different colours
    if count == 1:
        color = "#d72631"
        return color
    elif count == 2:
        color = "#5c3c92"
        return color0
    elif count == 3:
        color = "#e52165"
        return color
    elif count == 4:
        color = "orange"
        return color
    elif count == 5:
        color = "yellow"
        return color
    elif count == 6:
        color = "#ff80ed"
        return color
    elif count == 7:
        color = "#40e0d0"
        return color
    elif count == 8:
        color = "#00ff00"
        return color
    elif count == 9:
        color = "#2acaea"
        return color
    elif count == 10:
        color = "#e75874"
        count = 0
        return color
    else:
        pass


def change_color(new_text_box):
    select_color()
    new_text_box.configure(fg_color=color)

def new_command():
    t2 = threading.Thread(target=new_sticky, args=())
    t2.start()

def new_sticky():
    new_window = ctk.CTk()
    new_window.geometry("300x300")
    new_window.maxsize(300, 300)
    new_window.minsize(300, 300)
    new_window.overrideredirect(True)


    # frames created
    new_frame1 = ctk.CTkFrame(new_window, fg_color="black")
    new_frame1.pack(padx=10, pady=10, fill='both', expand=True)
    # frame 2 created
    new_frame1_2 = ctk.CTkFrame(new_frame1, )
    new_frame1_2.pack(padx=10, pady=10, fill='both', expand=True)

    data_date = ctk.StringVar()
    data_date.set("Date")
    data_time_hour = ctk.StringVar()
    data_time_hour.set("Hours")
    data_month = ctk.StringVar()
    data_month.set("Months")
    data_time_minute = ctk.StringVar()
    data_time_minute.set("Minutes")

    #options to select time and date for the reminder
    ctk.CTkOptionMenu(new_frame1_2, variable=data_date, fg_color="pink", button_color="yellow",
                      values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                              "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"],
                      text_color="black", width=70, height=25, dropdown_hover_color="orange").place(x=5, y=0)
    ctk.CTkOptionMenu(new_frame1_2, variable=data_month, button_color="yellow", fg_color="pink",
                      values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], width=70, height=25,
                      dropdown_hover_color="orange", text_color="black").place(x=80, y=0)
    ctk.CTkOptionMenu(new_frame1_2, variable=data_time_minute, button_color="yellow", fg_color="pink",
                      values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                              "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                              "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45",
                              "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"],
                      width=70, text_color="black", dropdown_hover_color="orange").place(x=80, y=25)
    ctk.CTkOptionMenu(new_frame1_2, variable=data_time_hour, button_color="yellow", fg_color="pink",
                      values=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                              "16", "17", "18", "19", "20", "21", "22", "23", "24"], width=70, text_color="black",
                      dropdown_hover_color="orange").place(x=5, y=25)

    # try if now color at first then the change option to add color to background
    try:
        new_text_box = ctk.CTkTextbox(new_frame1_2, fg_color=color)
        new_text_box.pack(padx=5, pady=50, fill='both', expand=True)
    except:
        new_text_box = ctk.CTkTextbox(new_frame1_2)
        new_text_box.pack(padx=5, pady=50, fill='both', expand=True)

    # color changing option
    change_color_option = ctk.CTkButton(new_frame1_2, text="Change", hover_color="red", width=60, height=25,command=lambda: change_color(new_text_box))
    change_color_option.place(y=0, x=200)

    # textbox created
    #t4 = threading.Thread(target=check, args=(checkbox_voice.get(), data_date.get(), data_month.get(), data_time_hour.get(), data_time_minute.get()))

    # save button created
    save_button = ctk.CTkButton(new_frame1, text="SAVE", height=50, width=300, font=('calibre', 12, 'normal'),command=lambda: check(checkbox_voice.get(), data_date.get(), data_month.get(), data_time_hour.get(), data_time_minute.get()))
    save_button.place(x=0, y=230)
    new_window.mainloop()


# implementing thread for the clock that is displayed on the screen
def updated():
    global t1
    t1 = threading.Thread(target=time12, args=())
    t1.start()


# time updation according to current time
def time12():
    # frame for time showing
    frame1 = ctk.CTkFrame(windows, fg_color="yellow", bg_color="black", height=55, width=208)
    frame1.place(x=170, y=30)

    frame2 = ctk.CTkFrame(windows, fg_color="yellow", bg_color="black", height=55, width=160)
    frame2.place(x=170, y=90)
    # infinite looping for displaying time
    while (True):
        current_DT = datetime.datetime.now()
        timz = current_DT.time()
        datz = current_DT.date()
        empty_label = ctk.CTkLabel(frame1, text=timz, text_color="red", font=('calibre', 20, 'normal'),
                                   corner_radius=95, fg_color="black", bg_color="black", width=100, height=45)
        empty_label.place(y=5, x=5)
        empty_label1 = ctk.CTkLabel(frame2, text=datz, text_color="red", font=('calibre', 20, 'normal'),
                                    corner_radius=95, fg_color="black", bg_color="black", width=100, height=45)
        empty_label1.place(y=5, x=5)

        time.sleep(0.1)


# resetting the time in the pannel
def reset(t):
    t.join()


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

windows = ctk.CTk()

# calling th funtion update
updated()

# windows configuration
# title
windows.title("sticky notes")

# size of the window that appears
windows.geometry("500x300")
windows.minsize(500, 300)
windows.maxsize(500, 300)
windows.config(background="black")

# widgets of the window that we created
time_label = ctk.CTkLabel(windows, text="Time ", text_color="red", font=('calibre', 20, 'normal'), corner_radius=55,
                          fg_color="white", bg_color="black", width=105, height=55)
time_label.place(y=30, x=45)

date_label = ctk.CTkLabel(windows, text="Date", text_color="red", font=('calibre', 20, 'normal'), corner_radius=55,
                          fg_color="white", bg_color="black", width=105, height=55)
date_label.place(y=90, x=45)

# check box for voice output of the remainder
checkbox_voice = ctk.CTkCheckBox(windows, border_color='pink', bg_color='black', text_color="blue",
                                 text="do you want to use voice remainder", checkmark_color="yellow")
checkbox_voice.place(x=120, y=160)

new_button = ctk.CTkButton(windows, text="NEW", hover_color="#be1558", bg_color="black", width=70, height=40,
                           corner_radius=150, command=new_command)
new_button.place(x=225, y=210)
manage_button = ctk.CTkButton(windows, text="MANAGE", hover_color="#be1558", bg_color="black", width=50, height=50,
                              corner_radius=150, command=lambda: reset(t1))
manage_button.place(x=210, y=250)
windows.mainloop()

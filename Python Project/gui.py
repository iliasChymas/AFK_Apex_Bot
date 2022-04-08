from tkinter import Tk, Label, PhotoImage, Button
from threading import Thread
from bot_functions import *
from other_functions import *
from psutil import process_iter
import time
import os, sys

res_button_pressed = ""
mode_button_pressed = 0 # 4 = xp_grind, 3= kd lowering
start_pressed = 0

class Gui:
    def __init__(self):
        # CREATES WINDOW OBJECT
        self.root = Tk()
        self.running = False
        # GETS SCREEN DIMENSIONS
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # SETS WINDOW SIZE
        self.root.geometry(f"800x600+{screen_width//2-400}+{screen_height//2-300}")

        # DOES OTHER WINDOW SETUP
        self.root.title("AFK Apex Bot")
        self.root.iconbitmap("ApexPredators_Logo.ico")
        self.root.configure(background='white')

        # CREATES ALL THE LABELS AND ADDS THEM TO THE WINDOW
        self.title_label = Label(self.root, text="Apex AFK Bot", background="white", font=("Helvetica", 30, "bold"))
        self.label1 = Label(self.root, text="What is your resolution in Apex?", background="white", font=("Helvetica", 15, "bold"))
        self.label2 = Label(self.root, text="(defaults to your monitor's revolution)", background="white", font=("Helvetica", 15, "bold"))
        self.label3 = Label(self.root, text="What mode do you want to AFK in?", background="white", font=("Helvetica", 15, "bold"))
        self.label4 = Label(self.root, text="", background="white", foreground="#ff4c4c", font=("Helvetica", 15, "bold"))
        self.title_label.place(relx=.5, rely=.075, anchor="center")
        self.label1.place(relx=.5, rely=.225, anchor="center")
        self.label2.place(relx=.5, rely=.3, anchor="center")
        self.label3.place(relx=.5, rely=.6, anchor="center")
        self.label4.place(relx=.5, rely=.535, anchor="center")

        # GET ALL OF THE IMAGES FOR THE BUTTONS
        self.image1 = PhotoImage(file="GUI Assets/button1.png")
        self.image2 = PhotoImage(file="GUI Assets/button2.png")
        self.image3 = PhotoImage(file="GUI Assets/button3.png")
        self.image4 = PhotoImage(file="GUI Assets/button4.png")
        self.image5 = PhotoImage(file="GUI Assets/button5.png")
        self.image5_2 = PhotoImage(file="GUI Assets/button5_2.png")
        self.image1_pressed = PhotoImage(file="GUI Assets/button1_pressed.png")
        self.image2_pressed = PhotoImage(file="GUI Assets/button2_pressed.png")
        self.image3_pressed = PhotoImage(file="GUI Assets/button3_pressed.png")
        self.image4_pressed = PhotoImage(file="GUI Assets/button4_pressed.png")
        self.image5_pressed = PhotoImage(file="GUI Assets/button5_pressed.png")
        self.image5_2_pressed = PhotoImage(file="GUI Assets/button5_2_pressed.png")

        # CREATES TEXT FIELDS FOR KEYBINDS
        self.entry1 = create_custom_entry(root=self.root, placeholder_text="Enter your interact key (Defaults to E)")
        self.entry2 = create_custom_entry(root=self.root, placeholder_text="Enter your tactical key (Defaults to Q)")


        # CREATES ALL THE BUTTONS AND ADDS THEM TO THE WINDOW
        self.button1 = Button(self.root, image=self.image1, borderwidth=0, foreground="white", command=self.button1_pressed)
        self.button2 = Button(self.root, image=self.image2, borderwidth=0, foreground="white", command=self.button2_pressed)
        self.button3 = Button(self.root, image=self.image3, borderwidth=0, foreground="white", command=self.button3_pressed)
        self.button4 = Button(self.root, image=self.image4, borderwidth=0, foreground="white", command=self.button4_pressed)
        self.button5 = Button(self.root, image=self.image5, borderwidth=0, foreground="white", command=self.button5_pressed)
        self.button1.place(relx=.35, rely=.425, anchor="center")
        self.button2.place(relx=.65, rely=.425, anchor="center")
        self.button3.place(relx=.35, rely=.725, anchor="center")
        self.button4.place(relx=.65, rely=.725, anchor="center")
        self.button5.place(relx=.5, rely=.9, anchor="center")


        self.root.mainloop()



# DEFINES THE FUNCTIONS THAT DETERMINE WHAT HAPPENS WHEN A BUTTON IS PRESSED
# HEXCODE OF UNPRESSED BUTTON IS #ff4c4c
# HEXCODE OF PRESSED BUTTON IS #ff7e7e
    def button1_pressed(self):
        self.button1.configure(image=self.image1_pressed)
        self.button2.configure(image=self.image2)
        global res_button_pressed
        res_button_pressed = "HD"
        print("Resolution is set to 1080p")


    def button2_pressed(self):
        self.button2.configure(image=self.image2_pressed)
        self.button1.configure(image=self.image1)
        global res_button_pressed
        res_button_pressed = "2K"
        print("Resolution is set to 1440p")


    def button3_pressed(self):
        self.button3.configure(image=self.image3_pressed)
        self.button4.configure(image=self.image4)
        global mode_button_pressed
        mode_button_pressed = 3
        print("Mode is set to KD Lowering")
        self.entry1.place(relx=.5, rely=.75, anchor="center")
        self.entry2.place(relx=.5, rely=.8, anchor="center")
        self.label3.place(relx=.5, rely=.57, anchor="center")
        self.label4.place(relx=.5, rely=.515, anchor="center")
        self.button3.place(relx=.35, rely=.655, anchor="center")
        self.button4.place(relx=.65, rely=.655, anchor="center")


    def button4_pressed(self):
        self.button4.configure(image=self.image4_pressed)
        self.button3.configure(image=self.image3)
        global mode_button_pressed
        mode_button_pressed = 4
        print("Mode is set to XP Grinding")
        # RETURNS THE GUI TO DEFAULT - WON'T APPEAR DIFFERENT UNLESS BUTTON 3 WAS PRESSED BEFORE
        self.label1.place(relx=.5, rely=.225, anchor="center")
        self.label2.place(relx=.5, rely=.3, anchor="center")
        self.label3.place(relx=.5, rely=.6, anchor="center")
        self.label4.place(relx=.5, rely=.535, anchor="center")
        self.button1.place(relx=.35, rely=.425, anchor="center")
        self.button2.place(relx=.65, rely=.425, anchor="center")
        self.button3.place(relx=.35, rely=.725, anchor="center")
        self.button4.place(relx=.65, rely=.725, anchor="center")
        self.button5.place(relx=.5, rely=.9, anchor="center")
        self.entry1.place_forget()
        self.entry2.place_forget()


    
    def button5_pressed(self):
        self.running = not self.running
        if res_button_pressed == "" or mode_button_pressed == 0:
            self.label4.configure(text="You must select the mode and resolution.")
            self.running = False
        elif mode_button_pressed == 3 and (len(self.entry1.get()) > 1 and self.entry1.get() != self.entry1.placeholder) or (len(self.entry2.get()) > 1 and self.entry2.get() != self.entry2.placeholder):
            self.label4.configure(text="You can only enter one character.")
            self.running = not self.running
        elif self.running:
            self.label4.configure(text="")
            self.button5.configure(image=self.image5_pressed)
            self.root.update()
            print("Launching bot")
            self.root.after(1000, self.button5.configure(image=self.image5_2))
            self.root.update()
            t1 = Thread(target=self.gui_launch_bot)
            t1.start()
        else:
            self.button5.configure(image=self.image5_2_pressed)
            self.root.update()
            print("Closing bot")
            self.root.after(1000, self.button5.configure(image=self.image5))
            self.root.update()

    def gui_launch_bot(self):
        launched = False
        apex_bot = ApexBot(res_button_pressed)
        while True:
            if not self.running:
                break
            if "r5apex.exe" in [p.name() for p in process_iter()]:
                if launched and pyautogui.locateOnScreen("Game Assets/ready_buttonHD.png"):
                    intro_to_lobby()
                
                if mode_button_pressed == 4:
                    apex_bot.xp_grinding()
                else:
                    interact = self.entry1.get()
                    tactical = self.entry2.get()
                    if self.entry1.get() == self.entry1.placeholder:
                        interact = "e"
                    if self.entry2.get() == self.entry2.placeholder:
                        tactical = "q"
                    apex_bot.kd_lowering(interact_key=interact.lower(), tactical_key=tactical.lower())
            elif not launched:
                launch_game()
                launched = True
                time.sleep(30)


apex_uri = "steam://rungameid/1172470"
def launch_game():
    print("Launching ...")
    cmd = "explorer steam://rungameid/1172470"
    result = os.system(cmd)
    print(result)

# LAUNCH BOT

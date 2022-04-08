import os, sys
from bot_functions import *
from other_functions import *
from gui import launch_game, Gui

bot_modes = { "kd":3, "xp":4 }

def tui_launch_bot(mode_button_pressed, res_button):
    launched = False
    apex_bot = ApexBot(res_button)
    while True:
        if "r5apex.exe" in [p.name() for p in process_iter()]:
            if launched and pyautogui.locateOnScreen("Game Assets/ready_buttonHD.png"):
                intro_to_lobby()
            
            if mode_button_pressed == 4:
                apex_bot.xp_grinding()
            else:
                apex_bot.kd_lowering(interact_key='e', tactical_key='q')
        elif not launched:
            launch_game()
            launched = True
            time.sleep(30)


if len(sys.argv) == 4:
    if sys.argv[1] == "headless":
        res_button = sys.argv[2] if sys.argv[2] in ['HD', "2K"] else "HD"
        bot_mode = bot_modes[sys.argv[3]] if sys.argv[3] in ["xp", "kd"] else "xp"
        tui_launch_bot(bot_mode, res_button)
    else:
        print("Wrong args!\nType this command: 'afkbot.exe headless [HD or 2K] [XP or KD]'")
elif len(sys.argv) == 1:
    g = Gui()
    g.gui_launch_bot()
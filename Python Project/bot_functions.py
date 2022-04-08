import pyautogui
import pydirectinput
import time
from random import randint
from psutil import process_iter

# QUEUES FOR A MATCH FROM THE HOME SCREEN
def queue_into_game(resolution):
    try:
        if pyautogui.locateOnScreen(f"Game Assets/fill_teammates{resolution}.png", confidence=.7) is not None:
            fill_button_cords = pyautogui.center(pyautogui.locateOnScreen(f"Game Assets/fill_teammates{resolution}.png", confidence=.7))
            pydirectinput.click(fill_button_cords.x, fill_button_cords.y)
        time.sleep(1)
        
        ready_button_cords = pyautogui.center(pyautogui.locateOnScreen(f"Game Assets/ready_button{resolution}.png", confidence=.9))
        pydirectinput.click(ready_button_cords.x, ready_button_cords.y)
    except:
        print("Error in finding fill and or ready button and loading into game.")


# ENTERS CLICKS AND KEYSTROKES IN CORRECT ORDER TO GO FROM THE DEATH SCREEN TO THE LOBBY
def go_to_lobby(resolution):
    if resolution == "HD":
        pydirectinput.press("space")
        time.sleep(1)
        yes_button_cords = pyautogui.center(
            pyautogui.locateOnScreen(f"Game Assets/yes_button{resolution}.png", confidence=.8))
        pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
        time.sleep(7)
        pydirectinput.click(850, 716)
        pydirectinput.press("space")
        time.sleep(2)
        while pyautogui.locateOnScreen(f"Game Assets/ready_button{resolution}.png", confidence=.8) == None:
            pydirectinput.press("space")
            time.sleep(1)
        
    else:
        pydirectinput.press("space")
        time.sleep(1)
        yes_button_cords = pyautogui.center(
            pyautogui.locateOnScreen(f"Game Assets/yes_button{resolution}.png", confidence=.8))
        pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
        time.sleep(7)
        pydirectinput.click(1231, 955)
        pydirectinput.press("space")
        time.sleep(2)
        pydirectinput.press("space")
        time.sleep(1)
        pydirectinput.press("space")
        time.sleep(1)
        pydirectinput.press("space")
        time.sleep(1)
        pydirectinput.press("space")

def intro_to_lobby():
    if pyautogui.locateOnScreen("continue_button_hd.png", confidence=.9):
        pydirectinput.press('space')
        time.sleep(7)
        pydirectinput.press('esc')
        time.sleep(2)
        return True # it iz on main menu
    else:
        return False # it iz not on main menu


class ApexBot:
    def __init__(self, resolution):
        self.in_game = False
        self.resolution = resolution
        self.last_healed = 0
        self.q_healed = 0
        self.syringe = 0

    def xp_grinding(self):
        # CHECKS IF APEX IS CURRENTLY RUNNING
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        # It checkes if hp is full if none then it heals the player!
        elif self.in_game and pyautogui.locateOnScreen("Game Assets/not_full2{}.PNG".format(self.resolution), confidence=.90) != None: 
            print("Low hp")
            if time.time() - self.last_healed  > 5:
                print("pressed: to heal")
                if self.q_healed == 1 and self.syringe < 2:
                    pydirectinput.press('4')
                    self.syringe += 1
                elif self.syringe == 0 and self.q_healed == 0:
                    pydirectinput.press('q')
                    self.q_healed += 1
                elif self.syringe == 2:
                    self.q_healed += 1
                    pydirectinput.press('q')
                self.last_healed = time.time()
        # STOPS PLAYER FROM BEING KICKED FOR AFKING BY JUMPING
        elif pyautogui.locateOnScreen(f"Game Assets/in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            time.sleep(randint(0, 10))
        # STARTS QUEUING
        elif pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8) is not None:
            queue_into_game(self.resolution)
            self.in_game = False
        # GOES FROM DEATH SCREEN TO HOME SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            self.q_healed = 0
            self.syringe = 0
            go_to_lobby(self.resolution)
            self.in_game = False
        # CLICKS THE CONTINUE BUTTON THAT APPEARS WHEN APEX IS FIRST LAUNCHED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # PRESSES ESCAPE WHEN A POPUP IS ON SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/escape_close{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # GETS USER BACK INTO THE GAME WHEN AN ERROR HAPPENS E.G. BEING DISCONNECTED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        #pick lifeline in order to heal even more and last for longer periods of time TonyMorgana
        elif not self.in_game and pyautogui.locateOnScreen("Game Assets/lifeline{}.png".format(self.resolution), confidence=.9) != None:
            life_coords = pyautogui.center(pyautogui.locateOnScreen("Game Assets/lifeline{}.png".format(self.resolution), confidence=.9))
            pydirectinput.click(life_coords.x, life_coords.y)
        else:
            self.in_game = False
        
        

    def kd_lowering(self, interact_key, tactical_key):
        # CHECKS IF APEX IS CURRENTLY RUNNING
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        # STOPS PLAYER FROM BEING KICKED FOR AFKING BY JUMPING AND USES THEIR TACTICAL TO MAKE THEM MORE VISIBLE
        elif pyautogui.locateOnScreen(f"Game Assets/in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            time.sleep(randint(0, 10))
            pydirectinput.press(tactical_key)
        # STARTS QUEUING
        elif pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8) is not None:
            queue_into_game(self.resolution)
            self.in_game = False
        # TRIES TO SELECT HORIZON, THEN GIBBY
        elif pyautogui.locateOnScreen(f"Game Assets/horizon{self.resolution}.png", confidence=.7) is not None:
            try:
                button_cords = pyautogui.center(pyautogui.locateOnScreen(f"Game Assets/horizon{self.resolution}.png", confidence=.8))
                pydirectinput.click(button_cords.x, button_cords.y)
            except:
                print("Horizon cords were not found")
                if pyautogui.locateOnScreen(f"Game Assets/gibraltar{self.resolution}.png", confidence=.7) is not None:
                    try:
                        button_cords = pyautogui.center(pyautogui.locateOnScreen(f"Game Assets/gibraltar{self.resolution}.png", confidence=.8))
                        pydirectinput.click(button_cords.x, button_cords.y)
                    except:
                        print("Gibraltar cords were not found")
        # DROPS THE USER FROM THE LAUNCH SHIP IN AN AREA USUALLY DENSE WITH PLAYERS
        elif pyautogui.locateOnScreen(f"Game Assets/launch{self.resolution}.png", confidence=.7) is not None:
            time.sleep(3)
            pydirectinput.press(interact_key)
            pydirectinput.moveTo(990, 985, 0.5)
            pydirectinput.keyDown("w")
            time.sleep(15)
            pydirectinput.keyUp("w")
        # GOES FROM DEATH SCREEN TO HOME SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            go_to_lobby(self.resolution)
            self.in_game = False
        # CLICKS THE CONTINUE BUTTON THAT APPEARS WHEN APEX IS FIRST LAUNCHED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # PRESSES ESCAPE WHEN A POPUP IS ON SCREEN
        elif pyautogui.locateOnScreen(f"Game Assets/escape_close{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # GETS USER BACK INTO THE GAME WHEN AN ERROR HAPPENS E.G. BEING DISCONNECTED
        elif pyautogui.locateOnScreen(f"Game Assets/continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        else:
            self.in_game = False

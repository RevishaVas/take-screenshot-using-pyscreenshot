import pyautogui 
import tkinter as tk
from tkinter.filedialog import *

root=tk.Tk()
window=tk.Canvas(root,width=400,height=400)
window.pack()
def take_ss():
    screen_shot=pyautogui.screenshot()
    save_path=asksaveasfilename()
    screen_shot.save(save_path+"_screenshot.png")
ss_button=tk.Button(text="TAKE A SCREENSHOT",command=take_ss,font=15)
window.create_window(200,200,window=ss_button)
root.mainloop()



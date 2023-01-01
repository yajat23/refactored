from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("600x450")
clock_image = ImageTk.PhotoImage(Image.open("clock.jpg"))
#--------------------------INDIA-----------------------------
india_label = Label(root, text = "INDIA")
india_label.place(relx = 0.2, rely = 0.05, anchor = CENTER)


india_clock = label(root)
india_clock["image"] = clock_image
india_clock.place(relx = 0.2, rely = 0.35, anchor = CENTER)

                  
india_time = label(root)
india_time.place(relx = 0.2, rely = 0.65, anchor = CENTER)
#------------------------US---------------------------------
us_label = Label(root, text = "US")
us_label.place(relx = 0.7, rely = 0.05, anchor = CENTER)


us_clock = label(root)
us_clock["image"] = clock_image
us_clock.place(relx = 0.7, rely = 0.35, anchor = CENTER)

                  
us_time = label(root)
us_time.place(relx = 0.7, rely = 0.65, anchor = CENTER)


class India:
    
    def times(self):
        home = pytz.timezone('asia, kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "time :"+current_time
        india_time.after(200, self.times)
        
class US:
    
    def times(self):
        home = pytz.timezone('us, central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        us_time["text"] = "time :"+current_time
        us_time.after(200, self.times)
    
    
obj_india = INDIA()
obj_us = US()

india_btn = Button(root, text = "show time", command = obj_india_times)
india_btn.place(relx = 0.2, rely = 0.8, anchor = CENTER)
    
us_btn = Button(root, text = "show time", command = obj_us_times)
us_btn.place(relx = 0.2, rely = 0.8, anchor = CENTER)
    
root.mainloop()
    
    
    
    
    
    
    
    
    
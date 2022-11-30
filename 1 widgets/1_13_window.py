import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('More on the window')
# window.geometry('600x400+100+200')
window.iconbitmap('python.ico')

# exercise:
# start window in the middle of the screen 
window_width = 1400
window_height = 600
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

left = int(display_width / 2 - window_width / 2)
top = int(display_height / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{left}+{top}')

# window sizes 
window.minsize(200, 100)
# window.maxsize(800, 700)
# window.resizable(True,False)

# screen attributes 
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha', 1)
# window.attributes('-topmost', True)

# security event 
window.bind('<Escape>', lambda event: window.quit())

# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)


# title bar 
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')

# run
window.mainloop()
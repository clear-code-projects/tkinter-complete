import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Place')
window.geometry('400x600')

# widgets 
label1 = ttk.Label(window, text = 'Label 1', background = 'red')
label2 = ttk.Label(window, text = 'Label 2', background = 'blue')
label3 = ttk.Label(window, text = 'Label 3', background = 'green')
button = ttk.Button(window, text = 'Button')

# layout 
label1.place(x = 300, y = 100, width = 100, height = 200)
label2.place(relx = 0.2, rely = 0.1, relwidth = 0.4, relheight = 0.5)
label3.place(x = 80, y = 60, width = 160, height = 300)
button.place(relx = 1, rely = 1, anchor = 'se')

# frame 
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text = 'Frame label', background = 'yellow')
frame_button = ttk.Button(frame, text = 'Frame Button')

# frame layout
frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)
frame_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.5)
frame_button.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)

# exercise 
# create a label and place it right in the center of the window
# the label should be half as wide as the window and be 200px tall
exercise_label = ttk.Label(window, text = 'exercise label', background = 'orange')
exercise_label.place(x = 200, rely = 0.5, anchor = 'center', relwidth = 0.5, height = 200)

# run
window.mainloop()
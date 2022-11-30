import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')

# frame
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')

# master setting
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

button = ttk.Button(frame, text = 'button in a frame')
button.pack()

# example 
label2 = ttk.Label(window, text = 'Label outside frame')
label2.pack(side = 'left')

# exercise
# create another frame with a label, a button and an entry and place it to the right
# of the other widgets 

exercise_frame = ttk.Frame(window)
ttk.Label(exercise_frame, text = 'label in frame 2').pack()
ttk.Button(exercise_frame, text = 'button in frame 2').pack()
ttk.Entry(exercise_frame).pack()
exercise_frame.pack(side = 'left')

# run
window.mainloop()
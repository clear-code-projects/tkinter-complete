import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

# window
window = ttk.Window(themename = 'darkly')
window.title('extra widgets')

# scrollable frame 
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand = True, fill = 'both')

for i in range(100):
	frame = ttk.Frame(scroll_frame)
	ttk.Label(frame, text = f'Label: {i}').pack(fill = 'x', side = 'left')
	ttk.Button(frame, text = f'Button :{i}').pack(fill = 'x', side = 'left')
	frame.pack(fill = 'x', expand = True)

# toast
toast = ToastNotification(
	title = 'This is a message title', 
	message = 'This is the actual message',
	duration = 2000,
	bootstyle = 'dark',
	position = (50, 100, 'ne'))

ttk.Button(window, text = 'show toast', command = toast.show_toast).pack(pady = 10)

# tooltip
button = ttk.Button(window, text = 'tooltip button', bootstyle = 'warning')
button.pack(pady = 10)
ToolTip(button, text = 'This does something', bootstyle = 'danger-inverse')

# calendar 
calendar = DateEntry(window)
calendar.pack(pady = 10)

ttk.Button(window, text = 'get calendar date', command = lambda: print(calendar.entry.get())).pack()

# progress -> floodgauge
progress_int = tk.IntVar(value = 50)
progress = ttk.Floodgauge(
	window, 
	text = 'progress', 
	variable = progress_int,
	bootstyle = 'danger',
	mask = 'mask {}%')

progress.pack(pady = 10, fill = 'x')
ttk.Scale(window, from_ = 0, to = 100, variable = progress_int).pack()

# meter 
meter = ttk.Meter(
	window,
	amounttotal = 100,
	amountused = 10,
	interactive = True,
	metertype = 'semi',
	subtext = 'some other text',
	bootstyle = 'danger'
	)
meter.pack()

# run 
window.mainloop()
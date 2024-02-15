
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

apps = []

if os.path.isfile('save.txt'):
	with open('save.txt', 'r') as f:
		tempApps = f.read()
		tempApps = tempApps.split(',')
		apps = [x for x in tempApps if x.strip()]

def addApp():
	for widget in frame.winfo_children():
		widget.destroy()

	filename = filedialog.askopenfilename(initialdir='/', title = 'Select File', filetypes=(("executables", "*.exe"), ("all files", "*.*")))
	if filename!="":
		apps.append(filename)
	print(apps)
	for app in apps:
		label = tk.Label(frame, text=app, bg = "gray")
		label.pack()

def runApps():
	for app in apps:
		os.startfile(app)  

def clear():
	for widget in frame.winfo_children():
		widget.destroy()
	# with open('save.txt', 'w') as f:
	# 	f.write('')
	os.remove('save.txt')
	print("cleared")
	apps = []


canvas = tk.Canvas(root, height=500, width=500, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.05)

for app in apps:
		label = tk.Label(frame, text=app)
		label.pack()

openfile = tk.Button(root, text='Open File', padx = 10, pady = 5, fg = 'white', bg = '#263D42', command=addApp)
openfile.pack(side=tk.LEFT, ipadx=50, padx=5, pady=3)

runApps = tk.Button(root, text='Run Files', padx = 10, pady = 5, fg = 'white', bg = '#263D42', command=runApps)
runApps.pack(side=tk.RIGHT, ipadx=50, padx=5, pady=3)

clearApps = tk.Button(root, text='Clear Files', padx = 10, pady = 5, fg = 'white', bg = '#263D42', command=clear)
clearApps.pack(side=tk.BOTTOM, ipadx=10, pady=5)

root.mainloop()
print("exit ", apps)
with open('save.txt', 'w') as f:
	for app in apps:
		f.write(app + ',')

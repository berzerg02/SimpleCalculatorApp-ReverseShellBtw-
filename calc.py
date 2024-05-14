import tkinter as tk
import subprocess

def run_vbs_script():
    vbs_script = "CalculatorMatrix.vbs"
    try:
        subprocess.Popen(["wscript", vbs_script])
        result_label.config(text="VBScript running in the background.")
    except Exception as e:
        result_label.config(text="Error executing VBScript: " + str(e))

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)  # You might want to use a safer evaluation method
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def clear_entry():
    entry.delete(0, tk.END)

def on_closing():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Calculator App")

# Entry widget for user input
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=4)

# Buttons for calculator operations
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('C', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=10, command=clear_entry)
    else:
        button = tk.Button(root, text=text, width=10, command=lambda t=text: entry.insert(tk.END, t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Quit button
quit_button = tk.Button(root, text='Quit', width=10, command=on_closing)
quit_button.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Start the main event loop
root.mainloop()

run_vbs_script()

#creating a calculator for Arthemetic operations
import tkinter as tk
def button_click(char):
    current_input = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current_input + str(char))
def clear_input():
    input_field.delete(0, tk.END)
def compute_result():
    try:
        expression = input_field.get()
        result = str(eval(expression))
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, result)
    except Exception as e:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error")
root = tk.Tk()
root.title("CALCULATOR")
input_field = tk.Entry(root, font=("Helvetica", 20))
input_field.grid(row=0, column=0, columnspan=4)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]
row_val = 1
col_val = 0
for button_text in buttons:
    if button_text == "=":
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 16), command=compute_result).grid(row=row_val, column=col_val)
    elif button_text == "C":
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 16), command=clear_input).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 16), command=lambda t=button_text: button_click(t)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
root.mainloop()
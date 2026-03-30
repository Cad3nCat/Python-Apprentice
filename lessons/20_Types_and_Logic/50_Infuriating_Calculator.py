"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().
"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
first_number = simpledialog.askfloat("First Number", "What is your first number")
# Ask the user for the second number
second_number = simpledialog.askfloat("Second Number", "What is your second number")
# Ask the user for the math operation
Math_Operation = simpledialog.askstring("Math Operation", "Please enter *, /, +, or -")
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if Math_Operation == '*':
    messagebox.showinfo(" ", first_number * second_number)
elif Math_Operation == '/':
    messagebox.showinfo(" ", first_number / second_number)
elif Math_Operation == '+':
    messagebox.showinfo(" ", first_number + second_number)
elif Math_Operation == '-':
    messagebox.showinfo(" ", first_number - second_number)
else:
    messagebox.showerror
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
window.mainloop()
# Keep the window open
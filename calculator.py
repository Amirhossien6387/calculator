import tkinter as tk
import os

def press(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        history.insert(tk.END, f"{expression} = {result}")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "خطا")
        history.insert(tk.END, f"{expression} = خطا")

# 🎨 رنگ‌ها
bg_color = "#121212"
btn_color = "#1f1f1f"
txt_color = "#ffffff"
accent_color = "#03dac6"
error_color = "#cf6679"

# 🖼️ ساخت پنجره اصلی
root = tk.Tk()
root.title("Calculator (Project)")

# 📌 ست‌کردن آیکن
if os.path.exists("logo.ico"):
    root.iconbitmap("logo.ico")  # ← آیکن برنامه

root.geometry("500x500")
root.configure(bg=bg_color)

# 🔲 نمایشگر
entry = tk.Entry(root, font=("Arial", 24), bg=btn_color, fg=txt_color,
                 insertbackground=txt_color, justify="right", relief="sunken", bd=4)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipadx=10, ipady=10)

# 🔘 دکمه‌ها
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        cmd = calculate
    else:
        cmd = lambda t=text: press(t)
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
              bg=btn_color, fg=txt_color, activebackground=accent_color,
              command=cmd).grid(row=row, column=col, padx=5, pady=5)

# ❌ پاک‌کردن
tk.Button(root, text="Clear", width=22, height=2, font=("Arial", 14),
          bg=error_color, fg="white", command=clear).grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# 📜 تاریخچه
tk.Label(root, text="History", font=("Arial", 12), bg=bg_color, fg=accent_color).grid(row=0, column=4, sticky="n", padx=10)
history = tk.Listbox(root, width=20, height=20, font=("Courier", 10),
                     bg=btn_color, fg=txt_color, selectbackground=accent_color)
history.grid(row=1, column=4, rowspan=5, padx=5, pady=5, sticky="n")

# 🔗 نسخه کانکتور
tk.Label(root, text="Connector Version 1", font=("Arial", 10, "italic"),
         bg=bg_color, fg="#888").grid(row=6, column=0, columnspan=5, pady=(10, 5))

root.mainloop()

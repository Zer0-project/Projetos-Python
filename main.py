import tkinter as tk

root = tk.Tk()
root.title("Engenharia Informática - Bartolomeu João")
root.geometry("400x200")

label = tk.Label(root, text="Olá, GitHub!\nEste é o meu primeiro projeto real.", font=("Arial", 14))
label.pack(pady=50)

root.mainloop()
import tkinter as tk

window = tk.Tk()
window.title("ravi kishan kuumar")

# Launch maximized
window.state("zoomed")

label = tk.Label(
    window,
    text="This is my first app ravi kishan kumar",
    font=("Segoe UI", 24, "bold")
)

label.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()
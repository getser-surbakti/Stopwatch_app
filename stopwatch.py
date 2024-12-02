import tkinter as tk
from datetime import datetime

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='#f5f5f5')  # Background color
        self.label = tk.Label(self.root, text="00:00:00", font=("Helvetica", 48), bg="#212121", fg="#ffffff", padx=20, pady=20)
        self.label.pack(pady=20)

        button_frame = tk.Frame(self.root, bg='#f5f5f5')
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="Start", command=self.start, font=("Helvetica", 14), bg="#4caf50", fg="#ffffff", activebackground="#45a049", width=10)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop, font=("Helvetica", 14), bg="#f44336", fg="#ffffff", activebackground="#e53935", width=10)
        self.stop_button.grid(row=0, column=1, padx=5, pady=5)

        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset, font=("Helvetica", 14), bg="#2196f3", fg="#ffffff", activebackground="#1e88e5", width=10)
        self.reset_button.grid(row=0, column=2, padx=5, pady=5)

    def start(self):
        if not self.running:
            self.start_time = datetime.now() - datetime.strptime(self.label["text"], '%H:%M:%S')
            self.running = True
            self.update_clock()

    def stop(self):
        if self.running:
            self.running = False
            self.root.after_cancel(self.timer)

    def reset(self):
        self.stop()
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

    def update_clock(self):
        if self.running:
            current_time = datetime.now()
            self.elapsed_time = current_time - self.start_time
            self.label.config(text=str(self.elapsed_time).split(".")[0])
            self.timer = self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Stopwatch 0.0")
    root.geometry("600x300")
    Stopwatch(root)
    root.mainloop()

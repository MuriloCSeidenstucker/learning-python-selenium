import tkinter as tk
from mslookup.interface.main_window import MainWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    app.run()
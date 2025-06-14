import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageGrab
import os

class Whiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Whiteboard")
        self.root.geometry("800x600")

        self.last_x, self.last_y = None, None
        self.brush_color = "black"         # Store brush color separately
        self.color = self.brush_color      # Current drawing color
        self.brush_size = 3
        self.background_color = "white"    # for eraser and canvas bg

        self.canvas = tk.Canvas(self.root, bg=self.background_color, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind('<Button-1>', self.activate_paint)
        self.canvas.bind('<B1-Motion>', self.paint)

        self.create_toolbar()

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, padx=5, pady=5)
        toolbar.pack(fill=tk.X)

        color_btn = tk.Button(toolbar, text="Color", command=self.choose_color)
        color_btn.pack(side=tk.LEFT)

        brush_btn = tk.Button(toolbar, text="Brush", command=self.use_brush)
        brush_btn.pack(side=tk.LEFT)

        eraser_btn = tk.Button(toolbar, text="Eraser", command=self.use_eraser)
        eraser_btn.pack(side=tk.LEFT)

        clear_btn = tk.Button(toolbar, text="Clear", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT)

        save_btn = tk.Button(toolbar, text="Save", command=self.save_canvas)
        save_btn.pack(side=tk.LEFT)

        self.brush_slider = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL, label="Brush Size")
        self.brush_slider.set(self.brush_size)
        self.brush_slider.pack(side=tk.LEFT)

    def activate_paint(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def paint(self, event):
        x, y = event.x, event.y
        self.brush_size = self.brush_slider.get()
        self.canvas.create_line((self.last_x, self.last_y, x, y),
                                fill=self.color,
                                width=self.brush_size,
                                capstyle=tk.ROUND,
                                smooth=True)
        self.last_x, self.last_y = x, y

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color
            self.color = color  # switch current color to new brush color

    def use_eraser(self):
        self.color = self.background_color

    def use_brush(self):
        self.color = self.brush_color

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_canvas(self):
        # Save current canvas content as a .png image
        x = self.root.winfo_rootx() + self.canvas.winfo_x()
        y = self.root.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files", "*.png")])
        if filepath:
            ImageGrab.grab().crop((x, y, x1, y1)).save(filepath)
            print(f"Saved to {filepath}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Whiteboard(root)
    root.mainloop()

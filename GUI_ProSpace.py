import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from datetime import datetime
import random
import matplotlib.pyplot as plt

class QuantumSensingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Sensing Apparatus Interface")

        # Data for real-time plotting
        self.x_data = []
        self.y_data = []

        # Create and configure widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame to hold widgets
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label
        ttk.Label(main_frame, text="Quantum Sensing Apparatus Interface", font=("TkDefaultFont", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Button to start experiment
        ttk.Button(main_frame, text="Start Experiment", command=self.start_experiment).grid(row=1, column=0, pady=10)

        # Button to stop experiment
        ttk.Button(main_frame, text="Stop Experiment", command=self.stop_experiment).grid(row=1, column=1, pady=10)

        # Real-time data display
        self.data_display = ScrolledText(main_frame, wrap=tk.WORD, width=40, height=10)
        self.data_display.grid(row=2, column=0, columnspan=2, pady=10)

        # Matplotlib figure for real-time data visualization
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=main_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=3, column=0, columnspan=2, pady=10)

    def start_experiment(self):
        # Add functionality for starting the experiment and generating random data
        self.x_data = []
        self.y_data = []
        for i in range(10):
            self.x_data.append(i)
            self.y_data.append(random.randint(1, 100))

        self.update_plot()

    def stop_experiment(self):
        # Add functionality for stopping the experiment
        message = "Experiment Stopped - " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data_display.insert(tk.END, message + "\n")

    def update_plot(self):
        # Update the plot with real-time data
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, marker='o')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Sensor Reading')
        self.ax.set_title('Real-time Data Visualization')

        # Redraw the canvas
        self.canvas.draw()

        # Display data in the ScrolledText widget
        message = f"Real-time Data: {self.x_data[-1]}, {self.y_data[-1]}"
        self.data_display.insert(tk.END, message + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumSensingApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
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

        # Experiment parameters
        self.experiment_running = False
        self.sensor_type = tk.StringVar(value="Temperature")
        self.experiment_parameters = {
            "Duration (s)": tk.StringVar(value="10"),
            "Interval (ms)": tk.StringVar(value="500"),
        }

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
        ttk.Label(main_frame, text="Quantum Sensing Apparatus Interface", font=("TkDefaultFont", 16)).grid(row=0, column=0, columnspan=4, pady=10)

        # Sensor type dropdown
        ttk.Label(main_frame, text="Select Sensor Type:").grid(row=1, column=0, sticky=tk.E)
        sensor_type_dropdown = ttk.Combobox(main_frame, textvariable=self.sensor_type, values=["Temperature", "Pressure", "Humidity"])
        sensor_type_dropdown.grid(row=1, column=1, sticky=tk.W)
        sensor_type_dropdown.bind("<<ComboboxSelected>>", self.update_parameters)

        # Experiment parameters
        self.create_parameter_entries(main_frame, row_start=2, row_end=4)

        # Button to start/stop experiment
        ttk.Button(main_frame, text="Start/Stop Experiment", command=self.toggle_experiment).grid(row=5, column=0, columnspan=2, pady=10)

        # Button to save data
        ttk.Button(main_frame, text="Save Data", command=self.save_data).grid(row=5, column=2, columnspan=2, pady=10)

        # Real-time data display
        self.data_display = ScrolledText(main_frame, wrap=tk.WORD, width=60, height=10)
        self.data_display.grid(row=6, column=0, columnspan=4, pady=10)

        # Matplotlib figure for real-time data visualization
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=main_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=7, column=0, columnspan=4, pady=10)

    def create_parameter_entries(self, parent, row_start, row_end):
        ttk.Label(parent, text="Experiment Parameters", font=("TkDefaultFont", 12)).grid(row=row_start, column=0, columnspan=4, pady=5, sticky=tk.W)

        parameters = ["Duration (s)", "Interval (ms)"]

        for i, param in enumerate(parameters):
            ttk.Label(parent, text=param + ":").grid(row=row_start + i + 1, column=0, sticky=tk.E)
            ttk.Entry(parent, textvariable=self.experiment_parameters[param]).grid(row=row_start + i + 1, column=1, sticky=tk.W)

    def update_parameters(self, event):
        # Update experiment parameters based on selected sensor type
        selected_sensor = self.sensor_type.get()

        if selected_sensor == "Temperature":
            self.experiment_parameters["Duration (s)"].set("10")
            self.experiment_parameters["Interval (ms)"].set("500")
        elif selected_sensor == "Pressure":
            self.experiment_parameters["Duration (s)"].set("15")
            self.experiment_parameters["Interval (ms)"].set("1000")
        elif selected_sensor == "Humidity":
            self.experiment_parameters["Duration (s)"].set("8")
            self.experiment_parameters["Interval (ms)"].set("300")

    def toggle_experiment(self):
        # Toggle the experiment state (start/stop)
        if not self.experiment_running:
            self.start_experiment()
        else:
            self.stop_experiment()

    def start_experiment(self):
        # Add functionality for starting the experiment and generating sensor data
        try:
            duration = int(self.experiment_parameters["Duration (s)"].get())
            interval = int(self.experiment_parameters["Interval (ms)"].get())

            self.x_data = []
            self.y_data = []

            for i in range(duration * 1000 // interval):
                self.x_data.append(i * interval / 1000)
                self.y_data.append(random.randint(1, 100))

                self.update_plot()
                self.root.update_idletasks()
                self.root.after(interval)

            self.experiment_running = False
            messagebox.showinfo("Experiment Complete", "Experiment completed successfully.")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values for experiment parameters.")

    def stop_experiment(self):
        # Add functionality for stopping the experiment
        self.experiment_running = False
        messagebox.showinfo("Experiment Stopped", "Experiment stopped manually.")

    def update_plot(self):
        # Update the plot with real-time data
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, marker='o')
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Sensor Reading')
        self.ax.set_title(f'Real-time Data Visualization - {self.sensor_type.get()} Sensor')

        # Redraw the canvas
        self.canvas.draw()

        # Display data in the ScrolledText widget
        message = f"Real-time Data: {self.x_data[-1]:.2f}s, {self.y_data[-1]}"
        self.data_display.insert(tk.END, message + "\n")

    def save_data(self):
        # Save recorded data to a text file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, "w") as file:
                file.write("Time (s), Sensor Reading\n")
                for i in range(len(self.x_data)):
                    file.write(f"{self.x_data[i]:.2f}, {self.y_data[i]}\n")

            messagebox.showinfo("Save Data", "Data saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumSensingApp(root)
    root.mainloop()

# Quantum Sensing Apparatus Interface - GUI_Development Prospace

## Overview

The Quantum Sensing Apparatus Interface is a GUI application developed to streamline the experimentation process in the PQuest lab at IIT Bombay, specifically in the domain of quantum sensing. The current codebase, which involves running scripts for data acquisition, is being transitioned to a graphical user interface to facilitate faster experimentation and real-time visualization of recorded data.

## Features

- **Start/Stop Experimentation:** Initiate and halt experiments with the click of a button.
- **Real-time Data Visualization:** Visualize sensor data in real-time using `matplotlib`.
- **Save Data:** Save recorded data to a text file for further analysis.

## Getting Started

### Prerequisites

- Python 3.x
- `matplotlib` library (install with `pip install matplotlib`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/quantum-sensing-interface.git
    ```

2. Change into the project directory:

    ```bash
    cd quantum-sensing-interface
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## Usage

1. Click "Start Experiment" to initiate the experiment. For demonstration purposes, random data will be generated.
2. Observe the real-time data visualization in the plot.
3. Click "Stop Experiment" to halt the experiment.
4. Save the recorded data using the "Save Data" button.

## Future Work

- Implement data acquisition from actual sensors.
- Enhance the GUI for a more user-friendly experience.
- Integrate the GUI code with the existing codebase.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

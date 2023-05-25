import tkinter as tk
import math
import matplotlib.pyplot as plt

def run_code():
    # Get the values from the entries
    set1_a = float(entry_set1_a.get())
    set1_b = float(entry_set1_b.get())
    set1_c = float(entry_set1_c.get())
    set2_a = float(entry_set2_a.get())
    set2_b = float(entry_set2_b.get())
    set2_c = float(entry_set2_c.get())
    start_P = float(entry_Pressure.get())
    y_1 = float(entry_set1_y.get())
    y_2 = 1 - y_1
    num_iterations = float(entry_iterations.get())

    # Run your code using the collected values

    A = [set1_a, set2_a]
    B = [set1_b, set2_b]
    C = [set1_c, set2_c]
    y = [y_1, y_2]
    P = [start_P, start_P]

    iteration = 0
    max_iterations = num_iterations

    T_values = []
    Temperature = []
    Temperature_new = []
    total = 0
    keep_looping = True

    for i in range(2):
        t = (B[i] / (A[i] - math.log(P[i]))) - C[i]
        total = total + t
        Temperature.append(t)

    avg = total / 2
    avg1 = total / 2

    while keep_looping:
        p1 = math.exp(A[0] - (B[0] / (avg + C[0])))
        x1 = (y[0] * P[0]) / p1
        x2 = 1 - x1
        p2 = y[1] * P[1] / x2
        T_new = (B[1] / (A[1] - math.log(p2))) - C[1]
        Temperature_new.append(T_new)
        avg = T_new

        if iteration < max_iterations:
            iteration += 1
            T_values.append(T_new)
        else:
            keep_looping = False

    convergence = f"The graph converges to {T_values[-1]} after {iteration} loops"
    difference = f"The difference between the 2 final temperature values: {abs(T_values[-2] - T_values[-1])}"
    composition = f"the liquid phase composition: x1 = {x1} and x2 = {x2}"
    text_area.delete(1.0, tk.END)  # Clear previous content
    text_area.insert(tk.END, convergence + "\n" + difference + "\n" + composition)

    # Set the backend to TkAgg
    plt.switch_backend('TkAgg')
    plt.plot(range(iteration), T_values, label='Temperature values', color='purple')
    # Get the current figure manager
    manager = plt.get_current_fig_manager()
    # Set the window name
    manager.window.title("Dew Temperature Calculation")
    plt.title('Temperature value throughout iterations', fontweight='bold')
    plt.xlabel('Number of times iterated')
    plt.ylabel('Temperature (°K)')
    plt.grid(True)
    plt.legend()

    # Display the graph and convergence information at the same time
    plt.show()

# Create the main window
window = tk.Tk()
window.title("Dew Temperature iteration")

# Get the screen width and height
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()

# Set the window's dimensions and location
window_w = 700
window_h = 800

# Calculate the x and y coordinates for the middle of the screen
x = int((screen_w / 2) - (window_w / 2))
y = int((screen_h / 2) - (window_h / 2))

window.resizable(True, True)
window.configure(bg="white")
window.geometry(f"{window_w}x{window_h}+{x}+{y}")

# Create the entries for set 1
label_set1 = tk.Label(window, text="First set of Antoine Values:", bg="white", font="bold")
label_set1.pack()
label_set1_a = tk.Label(window, text="A value", bg="white")
label_set1_a.pack()
entry_set1_a = tk.Entry(window)
entry_set1_a.pack()
label_set1_b = tk.Label(window, text="B value", bg="white")
label_set1_b.pack()
entry_set1_b = tk.Entry(window)
entry_set1_b.pack()
label_set1_c = tk.Label(window, text="C value", bg="white")
label_set1_c.pack()
entry_set1_c = tk.Entry(window)
entry_set1_c.pack()

# Create the entries for set 2
label_set2 = tk.Label(window, text="Second set of Antoine Values:", bg="white", font="bold")
label_set2.pack()
label_set2_a = tk.Label(window, text="A value", bg="white")
label_set2_a.pack()
entry_set2_a = tk.Entry(window)
entry_set2_a.pack()
label_set2_b = tk.Label(window, text="B value", bg="white")
label_set2_b.pack()
entry_set2_b = tk.Entry(window)
entry_set2_b.pack()
label_set2_c = tk.Label(window, text="C value", bg="white")
label_set2_c.pack()
entry_set2_c = tk.Entry(window)
entry_set2_c.pack()

# Create the entry for the Pressure of the system
label_Pressure = tk.Label(window, text="Pressure of the system", bg="white", font="bold")
label_Pressure.pack()
entry_Pressure = tk.Entry(window)
entry_Pressure.pack()

# Create the entry for the composition of the vapour phase
label_set1_y = tk.Label(window, text="Mole fractions in the vapour phase", bg="white", font="bold")
label_set1_y.pack()
label_set1_y = tk.Label(window, text="y1 value", bg="white")
label_set1_y.pack()
entry_set1_y = tk.Entry(window)
entry_set1_y.pack()

def update_number(*args):
    try:
        number = 1 - float(entry_set1_y.get())  # Perform the mathematical operation

        if number < 0 or number > 1:
            entry_set1_y.config(bg="red")
            error_label.config(text="Invalid input: Entry must be between 0 and 1")
            number_label.config(text="")
        else:
            entry_set1_y.config(bg="white")
            error_label.config(text="")
            number_label.config(text=str(number))

    except ValueError:
        entry_set1_y.config(bg="red")
        error_label.config(text="Invalid input")
        number_label.config(text="")

# Create a label for displaying the calculated number
label_number = tk.Label(window, text="y2:", bg="white")
label_number.pack()

# Create a label to display the calculated number
number_label = tk.Label(window, text="", bg="white")
number_label.pack()

# Create the entry for number of iterations
label_iterations = tk.Label(window, text="Number of Iterations:", bg="white", font="bold")
label_iterations.pack()
entry_iterations = tk.Entry(window)
entry_iterations.pack()

# Create the button to run the code
button_run = tk.Button(window, text="Calculate", command=run_code)
button_run.pack()

# Create a label to display error messages
error_label = tk.Label(window, text="", fg="red", bg="white")
error_label.pack()

# Bind the update_number function to the entry_set1_y
entry_set1_y.bind("<KeyRelease>", update_number)

# Create a text area to display the convergence information
text_area = tk.Text(window)
text_area.pack(side=tk.BOTTOM)

# Start the Tkinter event loop
window.mainloop()
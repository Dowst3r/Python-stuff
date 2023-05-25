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
    y_2 = float(entry_set2_y.get())
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
        for i in range(2):
            x1 = (y[0] * P[0]) / p1
            x2 = 1 - x1
            p2 = y[1] * P[1] / x2
            T_new = (B[1] / (A[1] - math.log(p2))) - C[1]
            Temperature_new.append(T_new)
            avg = 0
            avg = avg + T_new

        if iteration < max_iterations:
            iteration += 1
            T_values.append(T_new)
        else:
            keep_looping = False

    convergence_text = f"The graph converges to {T_values[-1]} after {iteration} loops"
    difference_text = f"The difference between the 2 final temperature values: {abs(T_values[-2] - T_values[-1])}"
    text_area.delete(1.0, tk.END)  # Clear previous content
    text_area.insert(tk.END, convergence_text + "\n" + difference_text)

    plt.plot(range(iteration), T_values, label='Temperature values', color='purple')
    plt.title('Temperature value throughout iterations', fontweight='bold')
    plt.xlabel('Number of times iterated')
    plt.ylabel('Temperature (°K)')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Display the graph and convergence information at the same time
    plt.show(block=False)

# Create the main window
window = tk.Tk()
window.title("Antoine Equation iteration")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window's dimensions and location
window_width = 700
window_height = 600

# Calculate the x and y coordinates for the middle of the screen
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.resizable(True, True)
window.configure(bg="white")
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

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
label_set1_y = tk.Label(window, text="Mole fractions in the liquid phase", bg="white", font="bold")
label_set1_y.pack()
label_set1_y = tk.Label(window, text="y1 value", bg="white")
label_set1_y.pack()
entry_set1_y = tk.Entry(window)
entry_set1_y.pack()
label_set2_y = tk.Label(window, text="y2 value", bg="white")
label_set2_y.pack()
entry_set2_y = tk.Entry(window)
entry_set2_y.pack()

# Create the entry for number of iterations
label_iterations = tk.Label(window, text="Number of Iterations:", bg="white", font="bold")
label_iterations.pack()
entry_iterations = tk.Entry(window)
entry_iterations.pack()

# Create the button to run the code
button_run = tk.Button(window, text="Run", command=run_code)
button_run.pack()

# Create a text area to display the convergence information
text_area = tk.Text(window)
text_area.pack(side=tk.BOTTOM)

# Start the Tkinter event loop
window.mainloop()
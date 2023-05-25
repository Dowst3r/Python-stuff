import tkinter as tk
import math
import matplotlib.pyplot as plt

window_Dew = None
window_Bubble = None
current_window = None

def open_window_Dew():
    global window_Dew, current_window
    # Destroy the initial window
    Main.destroy()

    # Set the current window
    current_window = window_Dew

    def go_back():
        global window_Dew
        # Destroy the Dew window
        window_Dew.destroy()
        
        create_main_menu()

    def Calculate():
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
        plt.show()

    # Create the Dew window
    window_Dew = tk.Tk()
    window_Dew.title("Dew Temperature iteration")

    # Create the back button to go back to the Main menu
    back_button = tk.Button(window_Dew, text="Back", command=go_back)
    back_button.pack(anchor=tk.NW, padx=10, pady=10)

    # Get the screen width and height
    screen_w = window_Dew.winfo_screenwidth()
    screen_h = window_Dew.winfo_screenheight()

    # Set the window's dimensions and location
    window_w = 700
    window_h = 800

    # Calculate the x and y coordinates for the middle of the screen
    x = int((screen_w / 2) - (window_w / 2))
    y = int((screen_h / 2) - (window_h / 2))

    window_Dew.resizable(False, False)
    window_Dew.configure(bg="white")
    window_Dew.geometry(f"{window_w}x{window_h}+{x}+{y}")

    # Create the entries for set 1
    label_set1 = tk.Label(window_Dew, text="First set of Antoine Values:", bg="white", font="bold")
    label_set1.pack()
    label_set1_a = tk.Label(window_Dew, text="A value", bg="white")
    label_set1_a.pack()
    entry_set1_a = tk.Entry(window_Dew)
    entry_set1_a.pack()
    label_set1_b = tk.Label(window_Dew, text="B value", bg="white")
    label_set1_b.pack()
    entry_set1_b = tk.Entry(window_Dew)
    entry_set1_b.pack()
    label_set1_c = tk.Label(window_Dew, text="C value", bg="white")
    label_set1_c.pack()
    entry_set1_c = tk.Entry(window_Dew)
    entry_set1_c.pack()

    # Create the entries for set 2
    label_set2 = tk.Label(window_Dew, text="Second set of Antoine Values:", bg="white", font="bold")
    label_set2.pack()
    label_set2_a = tk.Label(window_Dew, text="A value", bg="white")
    label_set2_a.pack()
    entry_set2_a = tk.Entry(window_Dew)
    entry_set2_a.pack()
    label_set2_b = tk.Label(window_Dew, text="B value", bg="white")
    label_set2_b.pack()
    entry_set2_b = tk.Entry(window_Dew)
    entry_set2_b.pack()
    label_set2_c = tk.Label(window_Dew, text="C value", bg="white")
    label_set2_c.pack()
    entry_set2_c = tk.Entry(window_Dew)
    entry_set2_c.pack()

    # Create the entry for the Pressure of the system
    label_Pressure = tk.Label(window_Dew, text="Pressure of the system", bg="white", font="bold")
    label_Pressure.pack()
    entry_Pressure = tk.Entry(window_Dew)
    entry_Pressure.pack()

    # Create the entry for the composition of the vapour phase
    label_set1_y = tk.Label(window_Dew, text="Mole fractions in the vapour phase", bg="white", font="bold")
    label_set1_y.pack()
    label_set1_y = tk.Label(window_Dew, text="y1 value", bg="white")
    label_set1_y.pack()
    entry_set1_y = tk.Entry(window_Dew)
    entry_set1_y.pack()

    def update_number(*args):
        try:
            number = 1 - float(entry_set1_y.get())  # Perform the mathematical operation

            if number < 0 or number > 1:
                entry_set1_y.config(bg="red")
                error_label.config(text="Invalid input: y1 entry must be between 0 and 1")
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
    label_number = tk.Label(window_Dew, text="y2:", bg="white")
    label_number.pack()

    # Create a label to display the calculated number
    number_label = tk.Label(window_Dew, text="", bg="white")
    number_label.pack()

    # Create the entry for number of iterations
    label_iterations = tk.Label(window_Dew, text="Number of Iterations:", bg="white", font="bold")
    label_iterations.pack()
    entry_iterations = tk.Entry(window_Dew)
    entry_iterations.pack()

    # Create the button to run the code
    button_run = tk.Button(window_Dew, text="Calculate", command=Calculate)
    button_run.pack()

    # Create a label to display error messages
    error_label = tk.Label(window_Dew, text="", fg="red", bg="white")
    error_label.pack()

    # Bind the update_number function to the entry_set1_y
    entry_set1_y.bind("<KeyRelease>", update_number)

    # Create a text area to display the convergence information
    text_area = tk.Text(window_Dew)
    text_area.pack(side=tk.BOTTOM)

    # Start the Tkinter event loop
    current_window.mainloop()

# Bubble calculation window

def open_window_Bubble():
    global window_Bubble, current_window
    # Destroy the initial window
    Main.destroy()

    # Set the current window
    current_window = window_Bubble

    def back():
        global window_Bubble
        # Destroy the Bubble window
        window_Bubble.destroy()
        
        create_main_menu()

    def Cal():
        # Get the values from the entries
        set1_a = float(entry_set1_a_Bubble.get())
        set1_b = float(entry_set1_b_Bubble.get())
        set1_c = float(entry_set1_c_Bubble.get())
        set2_a = float(entry_set2_a_Bubble.get())
        set2_b = float(entry_set2_b_Bubble.get())
        set2_c = float(entry_set2_c_Bubble.get())
        start_P = float(entry_Pressure_Bubble.get())
        x_1 = float(entry_set1_x.get())
        x_2 = 1 - x_1
        num_iterations = float(entry_iterations_Bubble.get())

        # Run your code using the collected values
        A = [set1_a, set2_a]
        B = [set1_b, set2_b]
        C = [set1_c, set2_c]
        x = [x_1, x_2]
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
            y1 = (x[0] * p1) / P[0]
            y2 = 1 - y1
            p2 = (y2 * P[1]) / x[1]
            T_new = (B[1] / (A[1] - math.log(p2))) - C[1]
            Temperature_new.append(T_new)
            avg = T_new

            if iteration < max_iterations:
                iteration += 1
                T_values.append(T_new)
            else:
                keep_looping = False

        convergence_Bubble = f"The graph converges to {T_values[-1]} after {iteration} loops"
        difference_Bubble = f"The difference between the 2 final temperature values: {abs(T_values[-2] - T_values[-1])}"
        composition_Bubble = f"the vapour phase composition: y1 = {y1} and y2 = {y2}"
        text_area_Bubble.delete(1.0, tk.END)  # Clear previous content
        text_area_Bubble.insert(tk.END, convergence_Bubble + "\n" + difference_Bubble + "\n" + composition_Bubble)

        # Set the backend to TkAgg
        plt.switch_backend('TkAgg')
        plt.plot(range(iteration), T_values, label='Temperature values', color='purple')
        # Get the current figure manager
        manager = plt.get_current_fig_manager()
        # Set the window name
        manager.window.title("Bubble Temperature Calculation")
        plt.title('Temperature value throughout iterations', fontweight='bold')
        plt.xlabel('Number of times iterated')
        plt.ylabel('Temperature (°K)')
        plt.grid(True)
        plt.legend()
        plt.show()

    # Create the Bubble window
    window_Bubble = tk.Tk()
    window_Bubble.title("Bubble Temperature iteration")

    # Create the back button to go back to the Main menu
    backk = tk.Button(window_Bubble, text="Back", command=back)
    backk.pack(anchor=tk.NW, padx=10, pady=10)

    # Get the screen width and height
    screen_width = window_Bubble.winfo_screenwidth()
    screen_height = window_Bubble.winfo_screenheight()

    # Set the window's dimensions and location
    window_width = 700
    window_height = 800

    # Calculate the x and y coordinates for the middle of the screen
    x_Bubble = int((screen_width / 2) - (window_width / 2))
    y_Bubble = int((screen_height / 2) - (window_height / 2))

    window_Bubble.resizable(False, False)
    window_Bubble.configure(bg="white")
    window_Bubble.geometry(f"{window_width}x{window_height}+{x_Bubble}+{y_Bubble}")

    # Create the entries for set 1
    label_set1_Bubble = tk.Label(window_Bubble, text="First set of Antoine Values:", bg="white", font="bold")
    label_set1_Bubble.pack()
    label_set1_a_Bubble = tk.Label(window_Bubble, text="A value", bg="white")
    label_set1_a_Bubble.pack()
    entry_set1_a_Bubble = tk.Entry(window_Bubble)
    entry_set1_a_Bubble.pack()
    label_set1_b_Bubble = tk.Label(window_Bubble, text="B value", bg="white")
    label_set1_b_Bubble.pack()
    entry_set1_b_Bubble = tk.Entry(window_Bubble)
    entry_set1_b_Bubble.pack()
    label_set1_c_Bubble = tk.Label(window_Bubble, text="C value", bg="white")
    label_set1_c_Bubble.pack()
    entry_set1_c_Bubble = tk.Entry(window_Bubble)
    entry_set1_c_Bubble.pack()

    # Create the entries for set 2
    label_set2_Bubble = tk.Label(window_Bubble, text="Second set of Antoine Values:", bg="white", font="bold")
    label_set2_Bubble.pack()
    label_set2_a_Bubble = tk.Label(window_Bubble, text="A value", bg="white")
    label_set2_a_Bubble.pack()
    entry_set2_a_Bubble = tk.Entry(window_Bubble)
    entry_set2_a_Bubble.pack()
    label_set2_b_Bubble = tk.Label(window_Bubble, text="B value", bg="white")
    label_set2_b_Bubble.pack()
    entry_set2_b_Bubble = tk.Entry(window_Bubble)
    entry_set2_b_Bubble.pack()
    label_set2_c_Bubble = tk.Label(window_Bubble, text="C value", bg="white")
    label_set2_c_Bubble.pack()
    entry_set2_c_Bubble = tk.Entry(window_Bubble)
    entry_set2_c_Bubble.pack()

    # Create the entry for the Pressure of the system
    label_Pressure_Bubble = tk.Label(window_Bubble, text="Pressure of the system", bg="white", font="bold")
    label_Pressure_Bubble.pack()
    entry_Pressure_Bubble = tk.Entry(window_Bubble)
    entry_Pressure_Bubble.pack()

    # Create the entry for the composition of the vapour phase
    label_set1_x = tk.Label(window_Bubble, text="Mole fractions in the liquid phase", bg="white", font="bold")
    label_set1_x.pack()
    label_set1_x = tk.Label(window_Bubble, text="x1 value", bg="white")
    label_set1_x.pack()
    entry_set1_x = tk.Entry(window_Bubble)
    entry_set1_x.pack()

    def update_number(*args):
        try:
            number = 1 - float(entry_set1_x.get())  # Perform the mathematical operation

            if number < 0 or number > 1:
                entry_set1_x.config(bg="red")
                error_label_Bubble.config(text="Invalid input: x1 entry must be between 0 and 1")
                number_label_Bubble.config(text="")
            else:
                entry_set1_x.config(bg="white")
                error_label_Bubble.config(text="")
                number_label_Bubble.config(text=str(number))

        except ValueError:
            entry_set1_x.config(bg="red")
            error_label_Bubble.config(text="Invalid input")
            number_label_Bubble.config(text="")

    # Create a label for displaying the calculated number
    label_number_Bubble = tk.Label(window_Bubble, text="x2:", bg="white")
    label_number_Bubble.pack()

    # Create a label to display the calculated number
    number_label_Bubble = tk.Label(window_Bubble, text="", bg="white")
    number_label_Bubble.pack()

    # Create the entry for number of iterations
    label_iterations_Bubble = tk.Label(window_Bubble, text="Number of Iterations:", bg="white", font="bold")
    label_iterations_Bubble.pack()
    entry_iterations_Bubble = tk.Entry(window_Bubble)
    entry_iterations_Bubble.pack()

    # Create the button to run the code
    button_run_Bubble = tk.Button(window_Bubble, text="Calculate", command=Cal)
    button_run_Bubble.pack()

    # Create a label to display error messages
    error_label_Bubble = tk.Label(window_Bubble, text="", fg="red", bg="white")
    error_label_Bubble.pack()

    # Bind the update_number function to the entry_set1_y
    entry_set1_x.bind("<KeyRelease>", update_number)

    # Create a text area to display the convergence information
    text_area_Bubble = tk.Text(window_Bubble)
    text_area_Bubble.pack(side=tk.BOTTOM)

    # Start the Tkinter event loop
    current_window.mainloop()



def create_main_menu():
    global Main
    # Create the main window
    Main = tk.Tk()
    Main.title("Main menu")

    # Get the screen width and height
    screen_w = Main.winfo_screenwidth()
    screen_h = Main.winfo_screenheight()

    # Set the window's dimensions and location
    window_w = 700
    window_h = 400

    # Calculate the x and y coordinates for the middle of the screen
    x = int((screen_w / 2) - (window_w / 2))
    y = int((screen_h / 2) - (window_h / 2))

    Main.resizable(True, True)
    Main.configure(bg="white")
    Main.geometry(f"{window_w}x{window_h}+{x}+{y}")

    # Create the Dew Temperature Button
    button1 = tk.Button(Main, text="Dew Temperature", command=open_window_Dew)
    button1.pack(pady=20)

    # Create Bubble Temperature Button
    button2 = tk.Button(Main, text="Bubble Temperature", command=open_window_Bubble)
    button2.pack(pady=10)

    Main.mainloop()

# Create the main menu window
create_main_menu()
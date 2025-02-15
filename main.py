import tkinter as tk
from tkinter import messagebox
from calculations import calculate_water_intake, calculate_bmi, calculate_body_fat_percentage

def on_calculate_body_fat_percentage():
    try:
        gender = gender_var.get()
        waist = float(waist_entry.get())
        neck = float(neck_entry.get())
        height = float(height_entry.get())
        hip = float(hip_entry.get()) if gender == "female" else 0  # Erkekler için kalça çevresi gereksiz

        body_fat_percentage = calculate_body_fat_percentage(gender, waist, neck, height, hip)
        result_label.config(text=f"Your Body Fat Percentage is: {body_fat_percentage:.2f}%")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Please enter valid numbers for all fields. {e}")

def show_menu():
    global menu_window
    menu_window = tk.Toplevel(window)
    menu_window.title("Choose Health Metric")
    menu_window.geometry("400x200")

    label = tk.Label(menu_window, text="What would you like to measure?", font=("Arial", 14))
    label.pack(pady=20)

    water_button = tk.Button(menu_window, text="Water Intake", command=choose_water_intake, font=("Arial", 12))
    water_button.pack(pady=10)

    bmi_button = tk.Button(menu_window, text="BMI Calculator", command=choose_bmi_calculator, font=("Arial", 12))
    bmi_button.pack(pady=10)

    body_fat_button = tk.Button(menu_window, text="Body Fat Percentage", command=choose_body_fat_calculator, font=("Arial", 12))
    body_fat_button.pack(pady=10)

def choose_water_intake():
    menu_window.destroy()
    water_input_window()

def choose_bmi_calculator():
    menu_window.destroy()
    bmi_input_window()

def choose_body_fat_calculator():
    menu_window.destroy()
    body_fat_input_window()

def water_input_window():
    global weight_entry, result_label
    water_input_window = tk.Toplevel(window)
    water_input_window.title("Water Intake Calculation")
    water_input_window.geometry("400x300")

    weight_label = tk.Label(water_input_window, text="Enter your weight (kg):", font=("Arial", 14))
    weight_label.pack(pady=10)

    weight_entry = tk.Entry(water_input_window, font=("Arial", 14))
    weight_entry.pack(pady=10)

    calculate_button = tk.Button(water_input_window, text="Calculate Water Intake", command=on_calculate_water_intake, font=("Arial", 14))
    calculate_button.pack(pady=20)

    result_label = tk.Label(water_input_window, text="Your recommended water intake is:", font=("Arial", 14))
    result_label.pack(pady=10)

def bmi_input_window():
    global weight_entry, height_entry, result_label
    bmi_input_window = tk.Toplevel(window)
    bmi_input_window.title("BMI Calculator")
    bmi_input_window.geometry("400x300")

    weight_label = tk.Label(bmi_input_window, text="Enter your weight (kg):", font=("Arial", 14))
    weight_label.pack(pady=10)

    weight_entry = tk.Entry(bmi_input_window, font=("Arial", 14))
    weight_entry.pack(pady=10)

    height_label = tk.Label(bmi_input_window, text="Enter your height (m):", font=("Arial", 14))
    height_label.pack(pady=10)

    height_entry = tk.Entry(bmi_input_window, font=("Arial", 14))
    height_entry.pack(pady=10)

    calculate_button = tk.Button(bmi_input_window, text="Calculate BMI", command=on_calculate_bmi, font=("Arial", 14))
    calculate_button.pack(pady=20)

    result_label = tk.Label(bmi_input_window, text="Your BMI is:", font=("Arial", 14))
    result_label.pack(pady=10)

def body_fat_input_window():
    global gender_var, waist_entry, neck_entry, height_entry, hip_entry, result_label
    body_fat_input_window = tk.Toplevel(window)
    body_fat_input_window.title("Body Fat Percentage")
    body_fat_input_window.geometry("400x400")

    gender_label = tk.Label(body_fat_input_window, text="Select your gender:", font=("Arial", 14))
    gender_label.pack(pady=10)

    gender_var = tk.StringVar()
    male_button = tk.Radiobutton(body_fat_input_window, text="Male", variable=gender_var, value="male", font=("Arial", 12))
    female_button = tk.Radiobutton(body_fat_input_window, text="Female", variable=gender_var, value="female", font=("Arial", 12))
    male_button.pack(pady=5)
    female_button.pack(pady=5)

    waist_label = tk.Label(body_fat_input_window, text="Enter your waist circumference (cm):", font=("Arial", 14))
    waist_label.pack(pady=10)
    waist_entry = tk.Entry(body_fat_input_window, font=("Arial", 14))
    waist_entry.pack(pady=10)

    neck_label = tk.Label(body_fat_input_window, text="Enter your neck circumference (cm):", font=("Arial", 14))
    neck_label.pack(pady=10)
    neck_entry = tk.Entry(body_fat_input_window, font=("Arial", 14))
    neck_entry.pack(pady=10)

    height_label = tk.Label(body_fat_input_window, text="Enter your height (cm):", font=("Arial", 14))
    height_label.pack(pady=10)
    height_entry = tk.Entry(body_fat_input_window, font=("Arial", 14))
    height_entry.pack(pady=10)

    hip_label = tk.Label(body_fat_input_window, text="Enter your hip circumference (cm):", font=("Arial", 14))
    hip_label.pack(pady=10)
    hip_entry = tk.Entry(body_fat_input_window, font=("Arial", 14))
    hip_entry.pack(pady=10)

    calculate_button = tk.Button(body_fat_input_window, text="Calculate Body Fat Percentage", command=on_calculate_body_fat_percentage, font=("Arial", 14))
    calculate_button.pack(pady=20)

    result_label = tk.Label(body_fat_input_window, text="Your Body Fat Percentage is:", font=("Arial", 14))
    result_label.pack(pady=10)

def show_calorie_calculator():
    global calorie_result_label
    calorie_window = tk.Toplevel(window)
    calorie_window.title("Calorie Needs Calculator")
    calorie_window.geometry("400x400")

    # Gender selection
    gender_label = tk.Label(calorie_window, text="Select your gender:", font=("Arial", 14))
    gender_label.pack(pady=10)
    
    gender_var = tk.StringVar()
    male_button = tk.Radiobutton(calorie_window, text="Male", variable=gender_var, value="male", font=("Arial", 12))
    female_button = tk.Radiobutton(calorie_window, text="Female", variable=gender_var, value="female", font=("Arial", 12))
    male_button.pack(pady=5)
    female_button.pack(pady=5)

    # Weight input
    weight_label = tk.Label(calorie_window, text="Enter your weight (kg):", font=("Arial", 14))
    weight_label.pack(pady=10)
    weight_entry = tk.Entry(calorie_window, font=("Arial", 14))
    weight_entry.pack(pady=10)

    # Height input
    height_label = tk.Label(calorie_window, text="Enter your height (cm):", font=("Arial", 14))
    height_label.pack(pady=10)
    height_entry = tk.Entry(calorie_window, font=("Arial", 14))
    height_entry.pack(pady=10)

    # Age input
    age_label = tk.Label(calorie_window, text="Enter your age:", font=("Arial", 14))
    age_label.pack(pady=10)
    age_entry = tk.Entry(calorie_window, font=("Arial", 14))
    age_entry.pack(pady=10)

    # Activity level selection
    activity_label = tk.Label(calorie_window, text="Select your activity level:", font=("Arial", 14))
    activity_label.pack(pady=10)

    activity_var = tk.StringVar()
    sedentary_button = tk.Radiobutton(calorie_window, text="Sedentary (little to no exercise)", variable=activity_var, value="sedentary", font=("Arial", 12))
    light_button = tk.Radiobutton(calorie_window, text="Lightly active (light exercise or sports 1-3 days/week)", variable=activity_var, value="light", font=("Arial", 12))
    moderate_button = tk.Radiobutton(calorie_window, text="Moderately active (moderate exercise or sports 3-5 days/week)", variable=activity_var, value="moderate", font=("Arial", 12))
    active_button = tk.Radiobutton(calorie_window, text="Very active (hard exercise or sports 6-7 days a week)", variable=activity_var, value="active", font=("Arial", 12))
    
    sedentary_button.pack(pady=5)
    light_button.pack(pady=5)
    moderate_button.pack(pady=5)
    active_button.pack(pady=5)

    # Calculate button
    def calculate_calories_button():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            age = int(age_entry.get())
            gender = gender_var.get()
            activity_level = activity_var.get()

            calories_needed = calculate_calories(weight, height / 100, age, gender, activity_level)  # height'i cm'den m'ye çeviriyoruz
            calorie_result_label.config(text=f"Your daily calorie needs: {calories_needed:.2f} kcal")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Please enter valid numbers. {e}")

    calculate_button = tk.Button(calorie_window, text="Calculate Calorie Needs", command=calculate_calories_button, font=("Arial", 14))
    calculate_button.pack(pady=20)

    calorie_result_label = tk.Label(calorie_window, text="Your daily calorie needs: ", font=("Arial", 14))
    calorie_result_label.pack(pady=10)

def show_menu():
    global menu_window
    menu_window = tk.Toplevel(window)
    menu_window.title("Choose Health Metric")
    menu_window.geometry("400x200")

    label = tk.Label(menu_window, text="What would you like to measure?", font=("Arial", 14))
    label.pack(pady=20)

    water_button = tk.Button(menu_window, text="Water Intake", command=choose_water_intake, font=("Arial", 12))
    water_button.pack(pady=10)

    bmi_button = tk.Button(menu_window, text="BMI Calculator", command=choose_bmi_calculator, font=("Arial", 12))
    bmi_button.pack(pady=10)

    calorie_button = tk.Button(menu_window, text="Calorie Needs", command=show_calorie_calculator, font=("Arial", 12))
    calorie_button.pack(pady=10)

window = tk.Tk()
window.title("VitalStats")
window.geometry("400x200")

start_button = tk.Button(window, text="Start Health Metric", command=show_menu, font=("Arial", 14))
start_button.pack(pady=50)

window.mainloop()

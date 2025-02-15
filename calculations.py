import math

def calculate_water_intake(weight):
    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")
    return weight * 0.033  # Kilo başına 33 ml su önerilir

def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be greater than zero.")
    return weight / (height ** 2)

def calculate_body_fat_percentage(gender, waist, neck, height, hip=0):
    if gender == "male":
        return 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
    elif gender == "female":
        return 495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.22100 * math.log10(height)) - 450
    else:
        raise ValueError("Invalid gender. Please select either 'male' or 'female'.")

def calculate_calories(weight, height, age, gender, activity_level):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender")

    if activity_level == "sedentary":
        calorie_intake = bmr * 1.2
    elif activity_level == "light":
        calorie_intake = bmr * 1.375
    elif activity_level == "moderate":
        calorie_intake = bmr * 1.55
    elif activity_level == "active":
        calorie_intake = bmr * 1.725
    else:
        raise ValueError("Invalid activity level")

    return calorie_intake

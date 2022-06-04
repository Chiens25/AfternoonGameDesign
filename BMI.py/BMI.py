# Sydney Chien

mass= int(input("input weight in kg:")) # Input weight
height= int(input("input height in m:")) # Input height
m2 = mass * mass # Find m^2
bmi = m2 / height # Calculate BMI
print("bmi =", bmi) 

print(m2 / height) # Another way to print BMI

if bmi < 14.5: # If less than
    print("you're underweight")
if bmi >= 14.5 and bmi <= 50: ## In between
    print("you're normal")
if bmi > 50: # If greater than
    print("you're overweight")
if bmi > 50 or bmi < 14.5: # Practice "or" statements
    print("you're unhealthy")


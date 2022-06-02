# Sydney Chien

mass= int(input("input weight in kg:"))
height= int(input("input height in m:"))
m2 = mass * mass
bmi = m2 / height
print("bmi", bmi) 
print(m2 / height)

if bmi < 14.5:
    print("you're underweight")
if bmi == 40:
    print("you're normal")
if bmi > 50:
    print("you're overweight")

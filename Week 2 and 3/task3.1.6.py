height=input("Enter height in cm : ")
weight=input("Enter weight in kg : ")
BMI = (float(weight) / float(height) / float(height)) * 10000

if(float(BMI)<=18.5):
    print("Underweight")
elif(float(BMI)>18.5 and float(BMI)<=24.9):
    print("Normal weight")
elif(float(BMI)>24.9 and float(BMI)<=29.9):
    print("Overweight")
else:
    print("Obesity")
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2,2)
if(bmi < 18.5):
  print(f"BMI is {bmi}. You are underweight")
elif(bmi>=18.5 and bmi <= 25.0):
  print(f"BMI is {bmi}. You have a normal weight")
elif(bmi>25.0 and bmi <= 30.0):
  print(f"BMI is {bmi}. You are overweight")
elif(bmi>30.0 and bmi < 35.0):
  print(f"BMI is {bmi}. You are obese")
else:
  print(f"BMI is {bmi}.You are clinically obese")



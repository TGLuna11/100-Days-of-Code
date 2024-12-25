height = 1.81
weight = 75

# Calculates the bmi using weight and height.
bmi = weight / (height ** 2)

print(bmi)

print(int(bmi))  # This will print the integer part of the bmi (flooring the value)
print(round(bmi, 2))  # This will round the bmi to 2 decimal places

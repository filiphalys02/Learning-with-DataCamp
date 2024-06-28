H = float(input('Write your height in meters'))
W = float(input('Write your weight in kilograms '))

BMI = W/H**2

print(f'Your BMI: {BMI}')

if BMI < 18.5:
    print('Underweight')
elif BMI <= 25:
    print('Correct')
elif BMI <= 30:
    print('Overweight')
elif BMI <= 35:
    print('First degree obesity')
elif BMI <= 40:
    print('Second degree obesity')
else:
    print('Third degree obesity')

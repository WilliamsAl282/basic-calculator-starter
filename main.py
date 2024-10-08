# Alex and Josh
# 10/8/2024
# Web and app development

print("""Hello, welcome to my Basic Calulator 
This script will promt you to enter two numbers
and then add, subtract, multiply, or divide the numbers
depending on the menu option you select""")

print()
print()

print('''Choose a math operation to perform
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)''')
math_choice = int(input("Enter your choice (1-4): \n"))
first_num = float(input("Enter the first number: \n"))
second_num = float(input('Enter the second number: \n'))




if math_choice == 1:
    print(f'{first_num} + {second_num} = {first_num + second_num}')
elif math_choice == 2:
    print(f'{first_num} - {second_num} = {first_num - second_num}')
elif math_choice == 3:
    print(f'{first_num} * {second_num} = {first_num * second_num}')
elif math_choice == 4:
    print(f'{first_num} / {second_num} = {first_num / second_num}')
else:
    print ('The number you put for your math choice is not valid, please enter a valid number')




# Lab task 5:
temp = input("Enter '1' to convert celsius to fahrenheit\nEnter '2' to convert fahrenheit to celsius ")
if "1" in temp:
    celsius = float(input("Enter temp in celsius: "))
    fahrenheit = celsius*1.8+32
    print(celsius, "celsius is equivalent to", fahrenheit, "fahrenheit")
elif "2" in temp:
    fahrenheit = float(input("Enter temp in fahrenheit: "))
    celsius = ((fahrenheit - 32) *5 / 9)
    print(fahrenheit, "fahrenheit is equivalent to", celsius, "celsius")

# This one im stuck on. "enter 1 for, enter 2 for, and enter 3 for" HOW?
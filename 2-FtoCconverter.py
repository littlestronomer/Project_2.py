pause = False
while not pause:
    type = input("Type f to convert Fahrenheit to Celcius, Type c to reverse direction.\n")
    if type == "f":
        fahrenheit = float(input("Type the degree: "))
        celcius = (fahrenheit - 32)*5/9
        print(f"Typed fahrenheit's equivelent is {celcius}C")
        pause = True

    elif type == "c":
        celcius = float(input("Type the degree: "))
        fahrenheit = celcius*9/5 + 32
        print(f"Typed celcius' equivelent is {fahrenheit}F")
        pause = True
        
    else:
        print("You have typed unexpected letter or number.")

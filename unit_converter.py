# advanced_unit_converter.py

def length_conversion():
    print("\nLength Conversion:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        meters = float(input("Enter meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is {feet:.2f} feet")
    elif choice == 2:
        feet = float(input("Enter feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is {meters:.2f} meters")
    elif choice == 3:
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is {miles:.2f} miles")
    elif choice == 4:
        miles = float(input("Enter miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is {km:.2f} kilometers")
    else:
        print("Invalid choice!")

def weight_conversion():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Ounces")
    print("4. Ounces to Grams")
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        kg = float(input("Enter kilograms: "))
        pounds = kg * 2.20462
        print(f"{kg} kilograms is {pounds:.2f} pounds")
    elif choice == 2:
        pounds = float(input("Enter pounds: "))
        kg = pounds / 2.20462
        print(f"{pounds} pounds is {kg:.2f} kilograms")
    elif choice == 3:
        grams = float(input("Enter grams: "))
        ounces = grams / 28.3495
        print(f"{grams} grams is {ounces:.2f} ounces")
    elif choice == 4:
        ounces = float(input("Enter ounces: "))
        grams = ounces * 28.3495
        print(f"{ounces} ounces is {grams:.2f} grams")
    else:
        print("Invalid choice!")

def temperature_conversion():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        celsius = float(input("Enter Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    elif choice == 2:
        fahrenheit = float(input("Enter Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    elif choice == 3:
        celsius = float(input("Enter Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius}°C is {kelvin:.2f} K")
    elif choice == 4:
        kelvin = float(input("Enter Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin} K is {celsius:.2f}°C")
    else:
        print("Invalid choice!")

def volume_conversion():
    print("\nVolume Conversion:")
    print("1. Liters to Gallons")
    print("2. Gallons to Liters")
    print("3. Milliliters to Fluid Ounces")
    print("4. Fluid Ounces to Milliliters")
    choice = int(input("Choose an option: "))
    
    if choice == 1:
        liters = float(input("Enter liters: "))
        gallons = liters * 0.264172
        print(f"{liters} liters is {gallons:.2f} gallons")
    elif choice == 2:
        gallons = float(input("Enter gallons: "))
        liters = gallons / 0.264172
        print(f"{gallons} gallons is {liters:.2f} liters")
    elif choice == 3:
        ml = float(input("Enter milliliters: "))
        fl_oz = ml / 29.5735
        print(f"{ml} milliliters is {fl_oz:.2f} fluid ounces")
    elif choice == 4:
        fl_oz = float(input("Enter fluid ounces: "))
        ml = fl_oz * 29.5735
        print(f"{fl_oz} fluid ounces is {ml:.2f} milliliters")
    else:
        print("Invalid choice!")

def main():
    while True:
        print("\nAdvanced Unit Converter")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Volume Conversion")
        print("5. Exit")
        
        choice = int(input("Choose a category: "))
        
        if choice == 1:
            length_conversion()
        elif choice == 2:
            weight_conversion()
        elif choice == 3:
            temperature_conversion()
        elif choice == 4:
            volume_conversion()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


def convert_length(value, from_unit, to_unit):
    conversions = {
        'inches_to_cm': value * 2.54,
        'cm_to_inches': value / 2.54,
        'feet_to_meters': value * 0.3048,
        'meters_to_feet': value / 0.3048,
        'inches_to_meters': value * 0.0254,
        'meters_to_inches': value / 0.0254,
        'feet_to_cm': value * 30.48,
        'cm_to_feet': value / 30.48,
        'meters_to_cm': value * 100,
        'cm_to_meters': value / 100,
        'feet_to_inches': value * 12,
        'inches_to_feet': value / 12
    }
    return conversions.get(f'{from_unit}_to_{to_unit}')

def convert_weight(value, from_unit, to_unit):
    conversions = {
        'pounds_to_kg': value * 0.453592,
        'kg_to_pounds': value / 0.453592,
        'ounces_to_grams': value * 28.3495,
        'grams_to_ounces': value / 28.3495,
        'pounds_to_grams': value * 453.592,
        'grams_to_pounds': value / 453.592,
        'kg_to_ounces': value * 35.274,
        'ounces_to_kg': value / 35.274,
        'pounds_to_ounces': value * 16,
        'ounces_to_pounds': value / 16,
        'kg_to_grams': value * 1000,
        'grams_to_kg': value / 1000
    }
    return conversions.get(f'{from_unit}_to_{to_unit}')

def convert_temperature(value, from_unit, to_unit):
    conversions = {
        'celsius_to_fahrenheit': (value * 9/5) + 32,
        'fahrenheit_to_celsius': (value - 32) * 5/9,
        'celsius_to_kelvin': value + 273.15,
        'kelvin_to_celsius': value - 273.15,
        'fahrenheit_to_kelvin': (value - 32) * 5/9 + 273.15,
        'kelvin_to_fahrenheit': (value - 273.15) * 9/5 + 32
    }
    return conversions.get(f'{from_unit}_to_{to_unit}')

def display_project_name():
    project_name = """
     _   _   ___    _   _   _____        ______   _____   ___    _  __      __  _____   _____  _____   _____   _____
    | | | | |   \  | | | | |__  _|      /  ____| /  _  \ |   \  | | \ \    / / |  ___| |  _  ||__  _| |  ___| |  _  |
    | | | | | |\ \ | | | |   | |       |  /      | | | | | |\ \ | |  \ \  / /  | |___  | |_| |  | |   | |___  | |_| |
    | |_| | | | \ \| | | |   | |       | |_____  | |_| | | | \ \| |   \ \/ /   |  ___| |   __|  | |   |  ___| |   __|
    \_____/ |_|  \___| |_|   |_|        \______| \_____/ |_|  \___|    \__/    |_____| |_|\_\   |_|   |_____| |_|\_\

    """
    print(project_name)


def main():
    display_project_name()
    print("Welcome to the Unit Converter!")
    print("Please select the type of conversion:")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == '1':
        print("\nLength Conversion")
        from_unit = input("Enter the unit you are converting from (inches, cm, feet, meters): ").lower()

        if from_unit == 'inches':
            valid_units = ['cm', 'meters', 'feet']
            to_unit = input("Convert inches to (cm, meters, feet): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert inches to (cm, meters, feet): ").lower()

        elif from_unit == 'cm':
            valid_units = ['inches', 'feet', 'meters']
            to_unit = input("Convert cm to (inches, feet, meters): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert cm to (inches, feet, meters): ").lower()

        elif from_unit == 'feet':
            valid_units = ['cm', 'meters', 'inches']
            to_unit = input("Convert feet to (cm, meters, inches): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert feet to (cm, meters, inches): ").lower()

        elif from_unit == 'meters':
            valid_units = ['cm', 'feet', 'inches']
            to_unit = input("Convert meters to (cm, feet, inches): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert meters to (cm, feet, inches): ").lower()

        else:
            print("Invalid unit. Please restart the program.")
            return

        value = float(input(f"Enter the value in {from_unit} to convert to {to_unit}: "))
        result = convert_length(value, from_unit, to_unit)

    elif choice == '2':
        print("\nWeight Conversion")
        from_unit = input("Enter the unit you are converting from (pounds, kg, ounces, grams): ").lower()

        if from_unit == 'pounds':
            valid_units = ['kg', 'grams', 'ounces']
            to_unit = input("Convert pounds to (kg, grams, ounces): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert pounds to (kg, grams, ounces): ").lower()

        elif from_unit == 'kg':
            valid_units = ['pounds', 'grams', 'ounces']
            to_unit = input("Convert kg to (pounds, grams, ounces): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert kg to (pounds, grams, ounces): ").lower()

        elif from_unit == 'ounces':
            valid_units = ['grams', 'pounds', 'kg']
            to_unit = input("Convert ounces to (grams, pounds, kg): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert ounces to (grams, pounds, kg): ").lower()

        elif from_unit == 'grams':
            valid_units = ['ounces', 'pounds', 'kg']
            to_unit = input("Convert grams to (ounces, pounds, kg): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert grams to (ounces, pounds, kg): ").lower()

        else:
            print("Invalid unit. Please restart the program.")
            return

        value = float(input(f"Enter the value in {from_unit} to convert to {to_unit}: "))
        result = convert_weight(value, from_unit, to_unit)

    elif choice == '3':
        print("\nTemperature Conversion")
        from_unit = input("Enter the unit you are converting from (celsius, fahrenheit, kelvin): ").lower()

        if from_unit == 'celsius':
            valid_units = ['fahrenheit', 'kelvin']
            to_unit = input("Convert celsius to (fahrenheit, kelvin): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert celsius to (fahrenheit, kelvin): ").lower()

        elif from_unit == 'fahrenheit':
            valid_units = ['celsius', 'kelvin']
            to_unit = input("Convert fahrenheit to (celsius, kelvin): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert fahrenheit to (celsius, kelvin): ").lower()

        elif from_unit == 'kelvin':
            valid_units = ['celsius', 'fahrenheit']
            to_unit = input("Convert kelvin to (celsius, fahrenheit): ").lower()
            while to_unit not in valid_units:
                print(f"Invalid unit. Please choose from {valid_units}.")
                to_unit = input("Convert kelvin to (celsius, fahrenheit): ").lower()

        else:
            print("Invalid unit. Please restart the program.")
            return

        value = float(input(f"Enter the value in {from_unit} to convert to {to_unit}: "))
        result = convert_temperature(value, from_unit, to_unit)

    else:
        print("Invalid choice. Please restart the program.")
        return

    if result is not None:
        print(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")
    else:
        print("Conversion not supported. Please check your input units.")

if __name__ == "__main__":
    main()

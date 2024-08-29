# Unit Converter
## [Video Demo](https://youtu.be/rt8GsCjWCWc)
### Description:
This program allows users to convert between various units of measurement for length, weight, and temperature. This project was developed as a final project of the "Harvard CS50 Introduction to Programming with Python" course. It is designed to offer a simple and intuitive way to perform common unit conversions, ensuring accurate results while handling various edge cases and invalid inputs.

The Unit Converter supports three main types of conversions:
- **Length**: Convert between inches, centimeters (cm), feet, and meters.
- **Weight**: Convert between pounds, kilograms (kg), ounces, and grams.
- **Temperature**: Convert between Celsius, Fahrenheit, and Kelvin.

#### How the Program Works?
1. **User Interaction**: The program starts by displaying a welcome message and prompts the user to choose the type of conversion they wish to perform (Length, Weight, or Temperature).
2. **Input Validation**: Once a conversion type is selected, the user is prompted to enter the unit they are converting from, the unit they are converting to, and the value to be converted. The program validates the input to ensure that the units and value are valid.
3. **Conversion Calculation**: Based on the user input, the program calculates the converted value using predefined conversion formulas.
4. **Output**: The converted value is then displayed to the user.

#### Files in the Project:
- **project.py**: This is the main script that contains the core functionality of the Unit Converter. It includes the following functions:
  - `convert_length(value, from_unit, to_unit)`: Converts length from one unit to another.
  - `convert_weight(value, from_unit, to_unit)`: Converts weight from one unit to another.
  - `convert_temperature(value, from_unit, to_unit)`: Converts temperature from one unit to another.
  - `display_project_name()`: Displays the project name in a stylized ASCII format.
  - `main()`: The main function that drives the user interaction and calls the appropriate conversion functions.

- **test_project.py**: This file contains the test cases for the conversion functions in `project.py`. The tests are implemented using `pytest` and ensure that each conversion function returns accurate results. The following test functions are included:
  - `test_convert_length()`
  - `test_convert_weight()`
  - `test_convert_temperature()`

- **requirements.txt**: This file lists the external libraries that the project depends on. Installing these dependencies can be done using pip.

#### Design Choices:
- **Dictionary-Based Conversion**: The conversion logic is implemented using dictionaries that map unit pairs to their respective conversion formulas. This approach simplifies the code and makes it easy to add new units or conversion types in the future.
- **User-Friendly Input Validation**: The program includes input validation to ensure that users enter valid units and values, reducing the likelihood of errors during conversion.
- **Test Coverage**: The project includes comprehensive test coverage to ensure the accuracy of conversions across all supported units. The tests are designed to handle typical conversion scenarios, providing confidence in the program's reliability.


### TODO:
#### Download
Clone the repository or download zip with the project files
```
git clone [https://github.com/albertovalcarcelcrespo/project.git](https://github.com/me50/AlbertoValcarcelCrespo.git)
```

#### Installation
After downloading, open the command line and go to the project directory:
```
cd project
```

Use pip to install the necessary dependencies:
```
pip install -r requirements.txt
```

#### Usage
Run the program by executing the project.py script with Python:
```
python project.py
```

Test the program by executing the test_project.py script with pytest:
```
pytest test_project.py
```

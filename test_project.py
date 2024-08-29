from project import convert_length, convert_weight, convert_temperature

def test_convert_length():
    assert convert_length(10, 'inches', 'cm') == 25.4
    assert convert_length(25.4, 'cm', 'inches') == 10
    assert convert_length(10, 'feet', 'meters') == 3.048
    assert convert_length(3.048, 'meters', 'feet') == 10
    assert convert_length(100, 'cm', 'meters') == 1
    assert convert_length(1, 'meters', 'cm') == 100
    assert convert_length(1, 'feet', 'cm') == 30.48
    assert convert_length(30.48, 'cm', 'feet') == 1
    assert convert_length(12, 'inches', 'feet') == 1
    assert convert_length(1, 'feet', 'inches') == 12

def test_convert_weight():
    assert convert_weight(10, 'pounds', 'kg') == 4.53592
    assert convert_weight(4.53592, 'kg', 'pounds') == 10
    assert convert_weight(10, 'ounces', 'grams') == 283.495
    assert convert_weight(283.495, 'grams', 'ounces') == 10
    assert convert_weight(1, 'pounds', 'grams') == 453.592
    assert convert_weight(453.592, 'grams', 'pounds') == 1
    assert convert_weight(1, 'kg', 'grams') == 1000
    assert convert_weight(1000, 'grams', 'kg') == 1
    assert convert_weight(16, 'ounces', 'pounds') == 1
    assert convert_weight(1, 'pounds', 'ounces') == 16

def test_convert_temperature():
    assert convert_temperature(0, 'celsius', 'fahrenheit') == 32
    assert convert_temperature(32, 'fahrenheit', 'celsius') == 0
    assert convert_temperature(0, 'celsius', 'kelvin') == 273.15
    assert convert_temperature(273.15, 'kelvin', 'celsius') == 0
    assert convert_temperature(32, 'fahrenheit', 'kelvin') == 273.15
    assert convert_temperature(273.15, 'kelvin', 'fahrenheit') == 32

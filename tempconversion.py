## "f" for Fahrenheit, "C" for Celsius, "K" for Kelvin
def temp_conversion(temp, current_unit, convert_to):
    current_unit = current_unit.upper()
    convert_to = convert_to.upper()
    if current_unit == convert_to:
        return temp  

    try:
        temp = float(temp) 
    except ValueError:
        return None

    if current_unit == 'C':
        if convert_to == 'F':
            return round((temp * 9/5) + 32, 2) 
        elif convert_to == 'K':
            return round(temp + 273.15, 2)  
    elif current_unit == 'F':
        if convert_to == 'C':
            return round((temp - 32) * 5/9, 2)  
        elif convert_to == 'K':
            return round((temp - 32) * 5/9 + 273.15, 2)  
    elif current_unit == 'K':
        if convert_to == 'C':
            return round(temp - 273.15, 2) 
        elif convert_to == 'F':
            return round((temp - 273.15) * 9/5 + 32, 2)  
    else:
        return None
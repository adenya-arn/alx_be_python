def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)

        answer = num1 / num2
        return f"The result of the division is {answer}"
    
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
    
    except ValueError:
        return f"Error:  Please enter numeric values only."
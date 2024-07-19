# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        
        if den == 0:
            return "Error: Cannot divide by zero."
        
        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."

# Testing the function directly
if __name__ == "__main__":
    print(safe_divide(10, 5))  # The result of the division is 2.0
    print(safe_divide(10, 0))  # Error: Cannot divide by zero.
    print(safe_divide("ten", 5))  # Error: Please enter numeric values only.




# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()


def quadratic(a, b, c, x):
    """Calculate the value of the quadratic function ax^2 + bx + c."""
    return a * (x ** 2) + b * x + c

if __name__ == "__main__":
    # Get user input
    try:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        x = float(input("Enter the value of x: "))
        
        result = quadratic(a, b, c, x)
        print(f"The value of the quadratic function for x={x} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

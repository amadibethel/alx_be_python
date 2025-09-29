def safe_divide(numerator, denominator):
    """Perform division while handling division by zero and non-numeric inputs."""
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

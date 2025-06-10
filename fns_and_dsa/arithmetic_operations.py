def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations.
    Args:
        num1: First operand (float/integer)
        num2: Second operand (float/integer)
        operation: One of 'add', 'subtract', 'multiply', or 'divide'
    Returns:
        Result of operation as float, or error message string
    """
    try:
        operation = operation.strip().lower()
        if operation == 'add':
            return float(num1 + num2)
        elif operation == 'subtract':
            return float(num1 - num2)
        elif operation == 'multiply':
            return float(num1 * num2)
        elif operation == 'divide':
            if num2 == 0:
                return "Cannot divide by zero"
            return float(num1 / num2)
        else:
            return "Invalid operation"
    except (TypeError, ValueError, AttributeError):
        return "Invalid input"
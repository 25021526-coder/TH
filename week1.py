# Week 1 Python Examples

def calculate_sum(a, b):
    """Calculate the sum of two numbers"""
    return a + b

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}!"

# Example of list operations
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]

# Main program
if __name__ == "__main__":
    # Test the functions
    print(calculate_sum(10, 20))  # Should print: 30
    print(greet("Python"))        # Should print: Hello, Python!
    print("Squares:", squares)    # Should print: Squares: [1, 4, 9, 16, 25]
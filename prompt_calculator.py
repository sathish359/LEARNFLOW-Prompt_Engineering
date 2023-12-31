def prompt_calculator(query):
    # Convert query to lowercase for case-insensitivity
    query = query.lower()

    # Define supported operations
    operations = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }

    # Initialize variables
    operation = None
    numbers = []

    # Identify operation and numbers
    for word in query.split():
        if word in operations:
            operation = operations[word]
        elif word.isdigit() or (word[0] == '-' and word[1:].isdigit()):
            numbers.append(float(word))

    # Perform calculation
    if operation and len(numbers) == 2:
        try:
            if operation == '/':
                result = numbers[0] / numbers[1]
            else:
                result = eval(f'{numbers[0]} {operation} {numbers[1]}')
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
    else:
        return "Error: Invalid input"

# usage
user_query = input()
result = prompt_calculator(user_query)
print(result)

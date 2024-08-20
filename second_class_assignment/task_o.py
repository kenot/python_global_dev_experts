def get_number_from_user():
    """Function to get a number from the user."""
    while True:
        try:
            number = int(input("Please enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def sum_of_digits(number):
    """Function to compute the sum of the digits of the given number."""
    number = abs(number)  # In case of negative numbers
    total_sum = 0
    while number > 0:
        total_sum += number % 10  # Add the last digit to the sum
        number = number // 10  # Remove the last digit
    return total_sum

# Main program
number = get_number_from_user()
sum_digits = sum_of_digits(number)
print(f"The sum of the digits of {number} is {sum_digits}.")

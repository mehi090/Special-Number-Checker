from timeit import default_timer as time
# Function to check if a number is prime

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
# Function to check if a number is a palindromic number

def is_a_palindromic(number):
    return str(number) == str(number)[::-1]
# Function to check if a number is a special number (prime and palindromic)

def is__a_special_number(number):
    return is_prime(number) and is_a_palindromic(number)

# Function to find all special numbers within a given range [m, n]

def find_special_number(m, n):
    special_number = [number for number in range(m, n + 1) if is__a_special_number(number)]
    return special_number

# Main function to get user input and find special numbers

def main():
    m = int(input("Enter small number (m): "))
    n = int(input("Enter large number (n): "))

    if m >= n:
        print("Invalid input")
        return

    special_number = find_special_number(m, n)

    print(f"Special number between {m} and {n} :")
    if special_number:
        print(special_number)
        print(f"Total number: {len(special_number)}")
    else:
        print("Not found.")

# Measure execution time

if __name__ == "__main__":
    start = time()
    main()
    print("Taken", time() - start)
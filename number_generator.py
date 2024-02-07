import random

def generate_series(count):
    for _ in range(count):
        # Generate 5 numbers between 1 and 50
        series_1_to_50 = sorted(random.sample(range(1, 51), 5))
        # Generate 2 numbers between 1 and 12
        series_1_to_12 = sorted(random.sample(range(1, 13), 2))
        
        # Print the series
        print(f"Series 1-50: {series_1_to_50}")
        print(f"Series 1-12: {series_1_to_12}")
        print()  # Print a newline for better readability between series

if __name__ == "__main__":
    count = int(input("Enter how many series you want to generate: "))
    generate_series(count)

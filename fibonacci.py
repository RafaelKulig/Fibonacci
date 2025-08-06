import sys
import argparse

def fibonacci(occurrence: int) -> str:
    """
    Generate the Fibonacci sequence up to the given number of elements.

    Parameters:
        occurrence (int): Number of elements to generate

    Returns:
        str: Comma-separated string of Fibonacci numbers
    """
    fib_list = [0]
    while len(fib_list) < occurrence:
        if len(fib_list) == 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])
    return ', '.join(str(i) for i in fib_list)

def main():
    parser = argparse.ArgumentParser(description="Show the Fibonacci sequence up to the desired number of elements.")
    parser.add_argument('-n', type=int, help='Number of elements in the Fibonacci sequence to be shown')
    args = parser.parse_args()

    if args.n is not None:
        entry = args.n
    else:
        while True:
            print("Enter the number of elements of the Fibonacci sequence to show or type 'quit' to exit:")
            entry = input(">>> ").strip()
            if entry.lower() == "quit":
                return
            if not entry.isdigit():
                print("Please enter a valid positive integer.")
                continue
            entry = int(entry)
            break

    if entry < 1:
        print("Please enter a number greater than 0.")
        sys.exit(1)

    print(fibonacci(entry))

if __name__ == "__main__":
    main()
def generate_squared_dict(n):
    squared_dict = {}
    for i in range(1, n+1):
        squared_dict[i] = i*i
    return squared_dict

def main():
    try:
        n = int(input("Enter an integral number (n): "))
        if n < 1:
            print("Please enter a positive integral number.")
            return
        result_dict = generate_squared_dict(n)
        print("Generated dictionary:", result_dict)
    except ValueError:
        print("Invalid input. Please enter a valid integral number.")

if __name__ == "__main__":
    main()

def generate_list_and_tuple(input_sequence):
    numbers = input_sequence.split(',')
    
    num_list = numbers
    
    num_tuple = tuple(numbers)
    
    return num_list, num_tuple

def main():
    try:
        input_sequence = input("Enter a sequence of comma-separated numbers: ")
        result_list, result_tuple = generate_list_and_tuple(input_sequence)
        
        print("Generated List:", result_list)
        print("Generated Tuple:", result_tuple)
    except ValueError:
        print("Invalid input. Please enter a valid sequence of comma-separated numbers.")

if __name__ == "__main__":
    main()

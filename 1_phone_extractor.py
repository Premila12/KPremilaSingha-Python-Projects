# Concepts: Sets, File Handling, Functions

def read_phone_numbers(filename):
    """
    Reads phone numbers from a file and returns them as a list
    """
    try:
        with open(filename, 'r') as file:
            numbers = [line.strip() for line in file if line.strip()]
        return numbers
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return []

def extract_unique_numbers(numbers):
    """
    Extracts unique phone numbers using a set
    """
    return set(numbers)

def display_unique_numbers(unique_numbers):
    """
    Displays unique phone numbers in a formatted way
    """
    print("\n" + "="*50)
    print("Unique Phone Numbers Found:")
    print("="*50)
    
    for idx, number in enumerate(sorted(unique_numbers), 1):
        print(f"{idx}. {number}")
    
    print("-"*50)
    print(f"Total Unique Numbers: {len(unique_numbers)}")
    print("="*50)

def save_unique_numbers(unique_numbers, output_file):
    """
    Saves unique phone numbers to a file
    """
    with open(output_file, 'w') as file:
        file.write("Unique Phone Numbers\n")
        file.write("="*50 + "\n")
        for idx, number in enumerate(sorted(unique_numbers), 1):
            file.write(f"{idx}. {number}\n")
        file.write("-"*50 + "\n")
        file.write(f"Total Unique Numbers: {len(unique_numbers)}\n")
    
    print(f"\n✓ Results saved to '{output_file}'")

def main():
    """
    Main function to orchestrate the program
    """
    print("\n Phone Number Extractor")
    print("Author: K Premila Singha\n")
    
    input_file = "input_files/phones.txt"
    output_file = "output_files/unique_phones.txt"
    
    # Read phone numbers from file
    all_numbers = read_phone_numbers(input_file)
    
    if not all_numbers:
        return
    
    print(f"Total numbers read: {len(all_numbers)}")
    
    # Extract unique numbers
    unique_numbers = extract_unique_numbers(all_numbers)
    
    # Display results
    display_unique_numbers(unique_numbers)
    
    # Save to file
    save_unique_numbers(unique_numbers, output_file)

if __name__ == "__main__":
    main()